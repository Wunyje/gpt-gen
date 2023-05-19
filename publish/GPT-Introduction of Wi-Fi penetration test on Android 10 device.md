#! https://zhuanlan.zhihu.com/p/630720610
# GPT-Introduction of Wi-Fi penetration test on Android 10 device
## 1. What is Wi-Fi?
### 1.1  How does Wi-Fi work on Android 10 device?
Wi-Fi is a wireless technology that allows devices to communicate over a network without using cables. Wi-Fi works on Android 10 devices by using a Wi-Fi chip that supports the IEEE 802.11 standards and a software stack that handles the network protocols, security, and connectivity.

### 1.2 How does that work differently from Linux OS?
Wi-Fi works differently on Android 10 devices than on Linux OS because Android 10 uses a modified version of the Linux kernel and has its own Wi-Fi framework that interacts with the hardware and the applications. The Wi-Fi framework consists of several components, such as the Wi-Fi Manager, the Wi-Fi Service, the HAL, and the wpa_supplicant.

## 2 What is Wi-Fi penetration test?

A Wi-Fi penetration test is a process of finding and exploiting security vulnerabilities in a Wi-Fi network or a Wi-Fi-enabled device. The goal of a Wi-Fi penetration test is to assess the security posture of the target and to provide recommendations for improving it.

### 2.1 How could it be implemented?

A Wi-Fi penetration test can be implemented by using various tools and techniques, depending on the scope and objectives of the test. Some of the common steps involved in a Wi-Fi penetration test are:

- Reconnaissance: Gathering information about the target network or device, such as the SSID, BSSID, encryption type, channel, signal strength, etc.
- Scanning: Identifying active hosts, ports, services, and vulnerabilities on the target network or device.
- Exploitation: Exploiting the vulnerabilities found in the previous step to gain access to the target network or device, or to perform other malicious actions.
- Post-exploitation: Maintaining access to the target network or device, extracting sensitive data, installing backdoors, etc.
- Reporting: Documenting the findings and recommendations of the penetration test in a clear and concise manner.

#### 2.1.1 What tools are needed?

There are many tools available for performing a Wi-Fi penetration test, but some of the most popular and effective ones are:

- Aircrack-ng: A suite of tools for cracking WEP and WPA/WPA2 passwords, capturing packets, injecting frames, etc.
- Nmap: A network scanner that can discover hosts, ports, services, and vulnerabilities on a network.
- Metasploit: A framework that can automate the exploitation of vulnerabilities and provide various payloads and modules for post-exploitation.
- Burp Suite: A web application security testing tool that can intercept and modify HTTP requests and responses, perform various attacks, etc.
- Wireshark: A network protocol analyzer that can capture and analyze network traffic.

#### 2.1.2 How to use these tools individually or together? (Use examples to illustrate)

Here are some examples of how to use these tools individually or together for a Wi-Fi penetration test:

- To crack a WPA/WPA2 password using Aircrack-ng, you need to capture a four-way handshake between a client and an access point. You can use `airodump-ng` to monitor the wireless traffic and identify the target network and client. Then you can use `aireplay-ng` to deauthenticate the client from the access point and force it to reconnect. This will generate a four-way handshake that you can capture with `airodump-ng`. Finally, you can use `aircrack-ng` to crack the password using a wordlist or a brute-force attack.
- To scan a network for active hosts and open ports using Nmap, you need to know the IP range of the network. You can use `nmap -sn <IP range>` to perform a ping scan and discover live hosts. Then you can use `nmap -sS -sV -p- <IP address>` to perform a TCP SYN scan, detect service versions, and scan all ports on a specific host.
- To exploit a vulnerability using Metasploit, you need to find a suitable module that matches the vulnerability. You can use `search` or `show exploits` commands to find available exploits. Then you can use `use <exploit name>` to select an exploit module. You can use `show options` or `show payloads` commands to see what options or payloads are available for the exploit module. You can use `set <option> <value>` to configure an option or payload for the exploit module. Finally, you can use `exploit` or `run` commands to execute the exploit module.
- To intercept and modify HTTP requests and responses using Burp Suite, you need to configure your browser or device to use Burp Suite as a proxy. You can use `Proxy > Options > Proxy Listeners` tab in Burp Suite to see what port Burp Suite is listening on. Then you can use `Proxy > Intercept` tab in Burp Suite to enable or disable interception mode. When interception mode is enabled, Burp Suite will capture any HTTP request or response that passes through it. You can use `Forward`, `Drop`, or `Action` buttons in Burp Suite to forward, drop, or modify an intercepted request or response.
- To capture and analyze network traffic using Wireshark, you need to select an interface that is connected to the network. You can use `Capture > Options` menu in Wireshark to see what interfaces are available and start capturing packets from one of them. You can use `Stop` button in Wireshark to stop capturing packets. You can use `File > Save As` menu in Wireshark to save captured packets as a file. You can use various filters, statistics, graphs, etc. in Wireshark to analyze captured packets.

#### 2.1.3 How to use MSF to penetrate Wi-Fi on Android 10 device?

MSF (Metasploit Framework) is a tool that can be used to penetrate Wi-Fi on Android 10 device by exploiting various vulnerabilities in the Wi-Fi framework or applications. Here are some steps on how to use MSF for this purpose:

- Connect your Android 10 device to your computer via USB cable and enable USB debugging mode on your device.
- Install adb (Android Debug Bridge) on your computer if you haven't already.
- Open a terminal on your computer and run `adb devices` command to see if your device is detected by adb.
- Run `adb tcpip 5555` command to enable adb over TCP/IP on your device.
- Run `adb shell ip addr show wlan0` command to get your device's IP address on Wi-Fi network.
- Run `adb connect <device IP>:5555` command to connect your device via adb over TCP/IP.
- Run MSF console on your computer by running `msfconsole` command.
- Use `search android wifi` command in MSF console to find available modules for exploiting Android Wi-Fi vulnerabilities.
- Select an appropriate module based on your target's OS version, architecture, etc. by using `use <module name>` command in MSF console.
- Configure the module's options by using `show options`, `set <option> <value>`, etc. commands in MSF console. Make sure you set LHOST option as your computer's IP address on Wi-Fi network and RHOSTS option as your device's IP address on Wi-Fi network.
- Run the module by using `exploit` or `run` command in MSF console. If successful, you should get a meterpreter session on your device.
- Use various meterpreter commands such as `sysinfo`, `getuid`, `shell`, etc. to interact with your device.

### 2.2 How to utilize existing CVE vulnerabilities of Wi-Fi on Android 10?

CVE (Common Vulnerabilities and Exposures) is a list of publicly known security vulnerabilities that affect various software products. You can utilize existing CVE vulnerabilities of Wi-Fi on Android 10 by finding out if your target device is affected by any of them and then exploiting them using appropriate tools or techniques.

#### 2.2.1 What are the CVE vulnerabilities about Wi-Fi on Android 10 after 2020?

According to https://cve.mitre.org/, some of the CVE vulnerabilities about Wi-Fi on Android 10 after 2020 are:

- CVE-2020-0245: A remote code execution vulnerability in Broadcom's wl driver that could allow an attacker within Wi-Fi range to execute arbitrary code within the context of kernel.
- CVE-2020-11161: An information disclosure vulnerability in Qualcomm's WLAN driver that could allow an attacker within radio range to access sensitive information from kernel memory via crafted packets.
- CVE-2020-11167: A denial-of-service vulnerability in Qualcomm's WLAN driver that could allow an attacker within radio range to cause kernel panic via crafted packets.

#### 2.2.2 Does any of these vulnerabilities have POC (Proof-of-concept), or have been exploited?

According to https://www.exploit-db.com/, some of these vulnerabilities have POCs or have been exploited by researchers or hackers. For example:

- CVE-2020-0245 has been exploited by Google Project Zero team as part of their Wi-Fi worm research project (https://googleprojectzero.blogspot.com/2020/12/introducing-project-zero-Wi-Fi-worm.html).
- CVE-2020-11161 has been exploited by Tencent Blade Team as part of their KRACK Attack research project (https://blade.tencent.com/en/advisories/krack/).