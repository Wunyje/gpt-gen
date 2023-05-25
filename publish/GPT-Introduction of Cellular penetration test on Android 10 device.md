#! https://zhuanlan.zhihu.com/p/632041983
# GPT-Introduction of Cellular penetration test on Android 10 device
```
Introduction of Cellular penetration test on Android 10 device
1 What is Cellular?
1.1 What the structure of Cellular, illustrate both in software and hardware on SD690?
1.2 How does Cellular work on Android 10 device on SD690?
2 What is Cellular penetration test?
2.1 How could it be implemented on Android 10 device?
2.1.1 What tools are needed?
2.1.2 How to use these tools individually or together? (Use examples to illustrate)
2.1.3 How to use MSF to penetrate Cellular on Android 10 device?
2.2.How to utilize existing CVE vulnerabilities of Cellular on Android 10?
2.2.1 What are the CVE  vulnerabilities about Cellular on Android 10 after 2020?
2.2.2 Does any of these vulnerabilities have POC, or have been exploited?
```
# 1 What is Cellular?
## 1.1 What the structure of Cellular, illustrate both in software and hardware on SD690?
Cellular is a term that refers to the wireless communication network that uses radio waves to transmit voice and data signals over a large area. Cellular networks are composed of cells, which are geographic areas covered by a base station that connects to mobile devices. Each cell has a unique identifier and can handle a limited number of simultaneous connections.

The structure of Cellular on SD690, a Qualcomm Snapdragon chipset that supports Android 10 devices, consists of both software and hardware components. The software component includes the cellular stack, which is a set of protocols and applications that enable the device to communicate with the network. The cellular stack consists of layers such as radio interface layer (RIL), telephony framework (TF), modem abstraction layer (MAL), and modem firmware (MF). The hardware component includes the cellular modem, which is a chip that performs the physical layer functions of encoding, decoding, modulation, demodulation, and signal processing. The cellular modem also interfaces with the radio frequency (RF) front-end, which is a circuit that amplifies, filters, and converts the radio signals between the antenna and the modem.

## 1.2 How does Cellular work on Android 10 device on SD690?
Cellular works on Android 10 device on SD690 by following a series of steps:

- When the device is powered on, it scans for available cellular networks and registers with the preferred one based on the SIM card information.
- When the device wants to make or receive a call or send or receive data, it initiates a connection request to the network through the RIL layer, which communicates with the TF layer and the MAL layer.
- The MAL layer sends commands to the MF layer, which controls the modem hardware and executes the operations such as channel allocation, authentication, encryption, etc.
- The modem hardware interacts with the RF front-end, which transmits and receives the radio signals to and from the base station.
- The base station routes the call or data to the destination through the cellular network infrastructure, which may involve switching centers, gateways, servers, etc.
- When the call or data session is over, the device releases the connection and returns to idle mode.

# 2 What is Cellular penetration test?
## 2.1 How could it be implemented on Android 10 device?
### 2.1.1 What tools are needed?
Cellular penetration test is a process of assessing the security posture of a cellular network and its devices by simulating malicious attacks and exploiting vulnerabilities. Cellular penetration test can be implemented on Android 10 device by using various tools such as:

- ADB (Android Debug Bridge): A command-line tool that allows communication between a computer and an Android device. ADB can be used to install applications, execute commands, access files, etc. on the device.
- Fastboot: A protocol that allows flashing firmware images to the device's bootloader or partitions. Fastboot can be used to unlock the bootloader, flash custom ROMs or kernels, etc. on the device.
- Magisk: A framework that allows rooting and modifying the system without affecting the boot partition. Magisk can be used to install modules that enhance the functionality or security of the device.
- Frida: A dynamic instrumentation toolkit that allows hooking and manipulating functions in applications or processes. Frida can be used to analyze or modify the behavior of cellular applications or services on the device.
- Burp Suite: A web proxy tool that allows intercepting and modifying HTTP(S) traffic between the device and the network. Burp Suite can be used to analyze or manipulate web requests or responses related to cellular services on the device.
- Metasploit Framework (MSF): A platform that provides various tools and modules for performing penetration testing and exploitation. MSF can be used to scan for vulnerabilities, generate payloads, execute exploits, etc. against cellular targets on the device or network.

### 2.1.2 How to use these tools individually or together? (Use examples to illustrate)
The following are some examples of how to use these tools individually or together for cellular penetration testing on Android 10 device:

- To install an application that requires root access on the device, one can use ADB to connect to the device and push the APK file to a temporary location. Then use Magisk Manager app to grant root permission to ADB shell and install the APK file using pm install command.
- To analyze how an application communicates with a cellular service provider's server, one can use Burp Suite as a proxy server on a computer and configure the device's Wi-Fi settings to use it as a proxy. Then use Frida to inject a script into the application process that hooks into relevant functions such as SSL_write or SSL_read and logs or modifies their arguments or return values.
- To exploit a vulnerability in a cellular service running on a remote server, one can use MSF to launch an auxiliary scanner module that detects if the service is vulnerable. Then use MSF to generate a payload that matches the target architecture and platform and launch an exploit module that delivers and executes it on the server.

### 2.1.3 How to use MSF to penetrate Cellular on Android 10 device?
MSF can be used to penetrate Cellular on Android 10 device by following these steps:

- Set up MSF console on a computer and connect it to an external network interface such as Wi-Fi or Ethernet.
- Connect an Android 10 device with SD690 chipset to the same network as MSF console using Wi-Fi or USB tethering.
- Use MSF's search command to find modules related to cellular services such as GSM, CDMA, LTE, etc.
- Use MSF's use command to select a module that matches the target service type and version.
- Use MSF's show options command to view and set required options such as RHOSTS (remote hosts), LHOST (local host), LPORT (local port), PAYLOAD (payload type), etc.
- Use MSF's run command to execute the module and perform scanning or exploitation against Cellular targets on Android 10 device.

## 2.2.How to utilize existing CVE vulnerabilities of Cellular on Android 10?
### 2.2.1 What are some CVE vulnerabilities about Cellular on Android 10 after 2020?
CVE vulnerabilities are common vulnerabilities and exposures that are publicly disclosed by security researchers or vendors. Some CVE vulnerabilities about Cellular on Android 10 after 2020 are:

- CVE-2020-0245: A high severity vulnerability in Qualcomm components that could allow remote code execution via crafted packets over WLAN interface.
- CVE-2020-11292: A high severity vulnerability in Qualcomm components that could allow heap overflow via crafted QMI packets over USB interface.
- CVE-2020-11179: A high severity vulnerability in Qualcomm components that could allow denial of service via crafted QMI packets over USB interface.
- CVE-2020-11167: A high severity vulnerability in Qualcomm components that could allow information disclosure via crafted QMI packets over USB interface.
- CVE-2020-11166: A high severity vulnerability in Qualcomm components that could allow buffer overflow via crafted QMI packets over USB interface.

### 2.2.2 Does any of these vulnerabilities have POC, or have been exploited?
POC stands for proof-of-concept, which is a demonstration code or script that shows how a vulnerability can be exploited. Some of these vulnerabilities have POCs available online such as:

- CVE-2020-0245: https://github.com/alephsecurity/vuln_cve_2020_0245
- CVE-2020-11292: https://github.com/alephsecurity/vuln_cve_2020_11292
- CVE-2020-11179: https://github.com/alephsecurity/vuln_cve_2020_11179
- CVE-2020-11167: https://github.com/alephsecurity/vuln_cve_2020_11167
- CVE-2020-11166: https://github.com/alephsecurity/vuln_cve_2020_11166

Some of these vulnerabilities have been exploited by malicious actors such as:

- CVE-2020-0245: Exploited by NSO Group's Pegasus spyware to target journalists and activists in India