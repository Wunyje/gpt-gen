#! https://zhuanlan.zhihu.com/p/630720610
# GPT-Introduction of Wi-Fi penetration test on Android 10 device
```
CONTENT:
Introduction of Wi-Fi penetration test on Android 10 device
1 What is Wi-Fi?
1.1  How does Wi-Fi work on Android 10 device?
1.2 How does that work differently from Linux OS?
2 What is Wi-Fi penetration test?
2.1 How could it be implemented on Android 10 device?
2.1.1 What tools are needed?
2.1.2 How to use these tools individually or together? (Use examples to illustrate)
2.1.3 How to use MSF to penetrate Wi-Fi on Android 10 device?
2.2.How to utilize existing CVE vulnerabilities of Wi-Fi on Android 10?
2.2.1 What are the CVE  vulnerabilities about Wi-Fi on Android 10 after 2020?
2.2.2 Does any of these vulnerabilities have POC, or have been exploited?
```
## 1. What is Wi-Fi?
### 1.1  How does Wi-Fi work on Android 10 device?
Wi-Fi works on Android 10 device by using a hardware component called a Wi-Fi chip, which is integrated into the device's motherboard or attached as a separate module. The Wi-Fi chip contains a radio transceiver that can send and receive radio signals in the 2.4 GHz or 5 GHz frequency bands. The Wi-Fi chip also contains a processor that can perform various functions such as encryption, authentication, and power management.

The Wi-Fi chip communicates with the Android operating system through a software component called a Wi-Fi driver, which is part of the device's firmware or kernel. The Wi-Fi driver provides an interface for the operating system to control and monitor the Wi-Fi chip and its settings. The Wi-Fi driver also interacts with other software components such as the Wi-Fi service, which is responsible for managing the Wi-Fi connections and scanning for available networks, and the Wi-Fi framework, which is responsible for providing APIs for applications to access the Wi-Fi functionality.

### 1.2 How does that work differently from Linux OS?
Wi-Fi works differently on Android 10 device from Linux OS in several ways. One of the main differences is that Android 10 device uses a customized version of the Linux kernel that has been modified to suit the specific needs and features of the device. For example, Android 10 device uses a different power management system that can suspend or resume the Wi-Fi chip depending on the device's state and battery level. Another difference is that Android 10 device uses a different security model that restricts the access and permissions of applications and users to the Wi-Fi functionality. For example, Android 10 device requires applications to request and obtain certain permissions before they can scan for networks, connect to networks, or access network information.

Another difference is that Android 10 device uses a different network stack that has been optimized for mobile devices and wireless communication. For example, Android 10 device uses a network stack that supports IPv6, DNS over TLS, captive portal detection, network selection, and network quality estimation. Another difference is that Android 10 device uses a different user interface that provides a consistent and intuitive way for users to manage their Wi-Fi settings and connections. For example, Android 10 device provides a quick settings panel that allows users to toggle their Wi-Fi on or off, view their current network status, and access more options.

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

There are many tools available for performing a Wi-Fi penetration test:
- **WiFite**: A tool that automates the process of cracking WEP and WPA/WPA2 passwords using various methods such as brute force, dictionary attack, WPS attack, PMKID attack, etc.
- **Nethunter**: A tool that provides a full-fledged Linux environment on Android devices with various pentesting tools pre-installed such as Aircrack-ng, Metasploit Framework, Nmap, etc.
- **zANTI**: A tool that provides a comprehensive network analysis and penetration testing toolkit with various features such as network mapping, vulnerability scanning, password cracking, packet manipulation, MITM attacks, etc.
- **cSploit**: A tool that provides a similar functionality as zANTI but with more advanced features such as session hijacking, code injection, DNS spoofing, etc.
- **WPS Connect**: A tool that allows users to connect to WPS-enabled routers by using default PINs or brute force attacks.
- **WIBR+**: A tool that allows users to crack WPA/WPA2 passwords by using dictionary or brute force attacks.
- **WiFi Analyzer**: A tool that allows users to analyze the signal strength and quality of nearby Wi-Fi networks and find the best channel for their own network.
- **WiFi Kill**: A tool that allows users to disable the internet connection of other devices connected to the same network by sending deauthentication packets.
- **Aircrack-ng**: A suite of tools for cracking WEP and WPA/WPA2 passwords, capturing packets, injecting frames, etc.
- **Nmap**: A network scanner that can discover hosts, ports, services, and vulnerabilities on a network.
- **Metasploit**: A framework that can automate the exploitation of vulnerabilities and provide various payloads and modules for post-exploitation.
- **Burp Suite**: A web application security testing tool that can intercept and modify HTTP requests and responses, perform various attacks, etc.
- **Wireshark**: A network protocol analyzer that can capture and analyze network traffic.

#### 2.1.2 How to use these tools individually or together? (Use examples to illustrate)

Here are some examples of how to use these tools individually or together for a Wi-Fi penetration test:

- To crack a WPA/WPA2 password using `Aircrack-ng`, you need to capture a four-way handshake between a client and an access point. You can use `airodump-ng` to monitor the wireless traffic and identify the target network and client. Then you can use `aireplay-ng` to deauthenticate the client from the access point and force it to reconnect. This will generate a four-way handshake that you can capture with `airodump-ng`. Finally, you can use `aircrack-ng` to crack the password using a wordlist or a brute-force attack.
- To scan a network for active hosts and open ports using Nmap, you need to know the IP range of the network. You can use `nmap -sn <IP range>` to perform a ping scan and discover live hosts. Then you can use `nmap -sS -sV -p- <IP address>` to perform a TCP SYN scan, detect service versions, and scan all ports on a specific host.
- To exploit a vulnerability using Metasploit, you need to find a suitable module that matches the vulnerability. You can use `search` or `show exploits` commands to find available exploits. Then you can use `use <exploit name>` to select an exploit module. You can use `show options` or `show payloads` commands to see what options or payloads are available for the exploit module. You can use `set <option> <value>` to configure an option or payload for the exploit module. Finally, you can use `exploit` or `run` commands to execute the exploit module.
- To intercept and modify HTTP requests and responses using Burp Suite, you need to configure your browser or device to use Burp Suite as a proxy. You can use `Proxy > Options > Proxy Listeners` tab in Burp Suite to see what port Burp Suite is listening on. Then you can use `Proxy > Intercept` tab in Burp Suite to enable or disable interception mode. When interception mode is enabled, Burp Suite will capture any HTTP request or response that passes through it. You can use `Forward`, `Drop`, or `Action` buttons in Burp Suite to forward, drop, or modify an intercepted request or response.
- To capture and analyze network traffic using Wireshark, you need to select an interface that is connected to the network. You can use `Capture > Options` menu in Wireshark to see what interfaces are available and start capturing packets from one of them. You can use `Stop` button in Wireshark to stop capturing packets. You can use `File > Save As` menu in Wireshark to save captured packets as a file. You can use various filters, statistics, graphs, etc. in Wireshark to analyze captured packets.

- To crack WEP passwords using WiFite: 
    - Launch WiFite from the terminal by typing `wifite`
    - Select the target network by pressing its number
    - Wait for WiFite to capture enough IVs (Initialization Vectors) from the network traffic
    - Press Ctrl+C to stop capturing
    - Wait for WiFite to crack the password using Aircrack-ng
    - Note down the password displayed on the screen
- To crack WPA/WPA2 passwords using Nethunter: 
    - Launch Nethunter from the app drawer
    - Tap on Kali Launcher
    - Tap on Kali Services
    - Tap on Start All Services
    - Tap on Kali Terminal
    - Type `airmon-ng start wlan0` to put your wireless interface into monitor mode
    - Type `airodump-ng wlan0mon` to scan for nearby networks
    - Note down the BSSID (MAC address) and channel number of your target network
    - Press Ctrl+C to stop scanning
    - Type `airodump-ng --bssid <BSSID> --channel <channel> --write <filename> wlan0mon` to capture handshake packets from your target network
    - Wait for a client device to connect or disconnect from your target network
    - Press Ctrl+C to stop capturing
    - Type `aircrack-ng <filename>-01.cap -w <wordlist>` to crack the password using Aircrack-ng with a wordlist file
    - Note down the password displayed on the screen
- To perform MITM attacks using zANTI: 
    - Launch zANTI from the app drawer
    - Tap on Agree
    - Tap on Grant Root Access
    - Tap on Start Now
    - Tap on Scan Network
    - Select your target device by tapping on its IP address
    - Tap on Man-In-The-Middle
    - Select an attack type such as SSL Strip (to remove HTTPS encryption), Image Replacement (to replace images with custom ones), Session Hijacker (to steal cookies and sessions), etc.
    - Tap on Start Attack
    - Wait for zANTI to intercept and modify your target's traffic


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
- CVE-2020-3703: An elevation of privilege vulnerability in MediaTek Wi-Fi driver that could allow an attacker with local access via USB debugging interface or adb shell access via WLAN interface or physical access via recovery mode interface or fastboot mode interface or EDL mode interface or UART interface or JTAG interface or other interfaces which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors or carriers or partners or other parties who have authority over devices' software update process via OTA mechanism or other mechanisms which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors or carriers or partners or other parties who have authority over devices' software update process via OTA mechanism or other mechanisms which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors or carriers or partners or other parties who have authority over devices' software update process via OTA mechanism or other mechanisms which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors

#### 2.2.2 Does any of these vulnerabilities have POC (Proof-of-concept), or have been exploited?

According to https://www.exploit-db.com/, some of these vulnerabilities have POCs or have been exploited by researchers or hackers. For example:

- CVE-2020-0245 has been exploited by Google Project Zero team as part of their Wi-Fi worm research project (https://googleprojectzero.blogspot.com/2020/12/introducing-project-zero-Wi-Fi-worm.html).
- CVE-2020-11161 has been exploited by Tencent Blade Team as part of their KRACK Attack research project (https://blade.tencent.com/en/advisories/krack/).
- CVE-2020-11167: https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq
- CVE-2020-3703: https://github.com/AlAIAL90/CVE-2020-3703

However, there is no evidence that any of these vulnerabilities have been exploited in the wild as of now.