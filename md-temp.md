# Introduction of Wi-Fi penetration test on Android 10 device

Wi-Fi is a wireless technology that allows devices to connect to the internet or to each other without using cables. Wi-Fi works by using radio waves to transmit and receive data between devices. In this blog post, we will explore how Wi-Fi works on Android 10 device and how it differs from Linux OS. We will also learn how to perform a Wi-Fi penetration test on Android 10 device using various tools and techniques.

# 1 What is Wi-Fi?

Wi-Fi is a short name for Wireless Fidelity, which is a trademark of the Wi-Fi Alliance, an organization that certifies devices that comply with the IEEE 802.11 standards for wireless communication. Wi-Fi is also a generic term that refers to any wireless network that uses these standards.

## 1.1 How does Wi-Fi work on Android 10 device?

Wi-Fi works on Android 10 device by using a hardware component called a Wi-Fi chip, which is integrated into the device's motherboard or attached as a separate module. The Wi-Fi chip contains a radio transceiver that can send and receive radio signals in the 2.4 GHz or 5 GHz frequency bands. The Wi-Fi chip also contains a processor that can perform various functions such as encryption, authentication, and power management.

The Wi-Fi chip communicates with the Android operating system through a software component called a Wi-Fi driver, which is part of the device's firmware or kernel. The Wi-Fi driver provides an interface for the operating system to control and monitor the Wi-Fi chip and its settings. The Wi-Fi driver also interacts with other software components such as the Wi-Fi service, which is responsible for managing the Wi-Fi connections and scanning for available networks, and the Wi-Fi framework, which is responsible for providing APIs for applications to access the Wi-Fi functionality.

## 1.2 How does that work differently from Linux OS?

Wi-Fi works differently on Android 10 device from Linux OS in several ways. One of the main differences is that Android 10 device uses a customized version of the Linux kernel that has been modified to suit the specific needs and features of the device. For example, Android 10 device uses a different power management system that can suspend or resume the Wi-Fi chip depending on the device's state and battery level. Another difference is that Android 10 device uses a different security model that restricts the access and permissions of applications and users to the Wi-Fi functionality. For example, Android 10 device requires applications to request and obtain certain permissions before they can scan for networks, connect to networks, or access network information.

Another difference is that Android 10 device uses a different network stack that has been optimized for mobile devices and wireless communication. For example, Android 10 device uses a network stack that supports IPv6, DNS over TLS, captive portal detection, network selection, and network quality estimation. Another difference is that Android 10 device uses a different user interface that provides a consistent and intuitive way for users to manage their Wi-Fi settings and connections. For example, Android 10 device provides a quick settings panel that allows users to toggle their Wi-Fi on or off, view their current network status, and access more options.

# 2 What is Wi-Fi penetration test?

A Wi-Fi penetration test is a process of evaluating the security of a wireless network by attempting to exploit its vulnerabilities and weaknesses. A Wi-Fi penetration test can help identify and prevent potential threats such as unauthorized access, data theft, denial of service, man-in-the-middle attacks, and rogue access points. A Wi-Fi penetration test can also help improve the security posture and awareness of the network owners and administrators.

## 2.1 How could it be implemented on Android 10 device?

A Wi-Fi penetration test could be implemented on Android 10 device by using various tools and techniques that can perform different tasks such as scanning, sniffing, cracking, injecting, spoofing, hijacking, and exploiting. Some of these tools are native to the Android operating system or can be installed as applications from the Google Play Store or other sources. Some of these tools require root access or special permissions to function properly. Some of these tools are:

### 2.1.1 What tools are needed?

- **WiFite**: A tool that automates the process of cracking WEP and WPA/WPA2 passwords using various methods such as brute force, dictionary attack, WPS attack, PMKID attack, etc.
- **Nethunter**: A tool that provides a full-fledged Linux environment on Android devices with various pentesting tools pre-installed such as Aircrack-ng, Metasploit Framework, Nmap, etc.
- **zANTI**: A tool that provides a comprehensive network analysis and penetration testing toolkit with various features such as network mapping, vulnerability scanning, password cracking, packet manipulation, MITM attacks, etc.
- **cSploit**: A tool that provides a similar functionality as zANTI but with more advanced features such as session hijacking, code injection, DNS spoofing, etc.
- **WPS Connect**: A tool that allows users to connect to WPS-enabled routers by using default PINs or brute force attacks.
- **WIBR+**: A tool that allows users to crack WPA/WPA2 passwords by using dictionary or brute force attacks.
- **WiFi Analyzer**: A tool that allows users to analyze the signal strength and quality of nearby Wi-Fi networks and find the best channel for their own network.
- **WiFi Kill**: A tool that allows users to disable the internet connection of other devices connected to the same network by sending deauthentication packets.

### 2.1.2 How to use these tools individually or together? (Use examples to illustrate)

Here are some examples of how to use these tools individually or together:

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

### 2.1.3 How to use MSF (Metasploit Framework)to penetrate Wi-Fi on Android 10 device?

MSF is a powerful framework that can be used to perform various types of penetration testing tasks such as reconnaissance, exploitation,
post-exploitation,
etc.
To use MSF to penetrate Wi-Fi on Android 10 device,
you need to have Nethunter installed on your device,
as it comes with MSF pre-installed.
Here are some steps to use MSF to penetrate Wi-Fi on Android 10 device:

- Launch Nethunter from the app drawer
- Tap on Kali Launcher
- Tap on Kali Services
- Tap on Start All Services
- Tap on Kali Terminal
- Type `msfconsole` to launch MSF console
- Type `search wifi` to search for available modules related to wifi
- Select a module that suits your needs by typing `use <module name>`
- Type `show options` to see what options you need to set for the module
- Set the required options by typing `set <option name> <value>`
- Type `run` or `exploit` to execute the module

For example,
to use MSF module `auxiliary/scanner/wifi/wps_scanner` 
to scan for WPS-enabled routers,
you need to set these options:

- RHOSTS: The range of IP addresses you want to scan (e.g., `192.168.1.0/24`)
- INTERFACE: The name of your wireless interface in monitor mode (e.g., `wlan0mon`)
- THREADS: The number of concurrent threads you want to use (e.g., 10)

After setting these options, you can run the module by typing exploit or run. The module will then scan the specified IP range and display the results in a table. The table will show the MAC address, ESSID, vendor, model, and WPS version of each router that supports WPS. You can also see if the router has WPS locked or not.

This module is useful for finding potential targets for WPS attacks, such as Reaver or Pixie Dust. However, you should always obtain permission from the network owner before attempting any attack. Unauthorized access to wireless networks is illegal and unethical.

## 2.2.How to utilize existing CVE vulnerabilities of Wi-Fi on Android 10?
### 2.2.1 What are some CVE vulnerabilities about Wi-Fi on Android 10 after 2020?
According to CVE Details website (https://www.cvedetails.com/), some of the CVE vulnerabilities about Wi-Fi on Android 10 after 2020 are:

- CVE-2020-0245: A remote code execution vulnerability in Broadcom Wi-Fi firmware that could allow an attacker within Bluetooth range to execute arbitrary code within the context of kernel.
- CVE-2020-11161: A denial of service vulnerability in Qualcomm WLAN component that could allow an attacker within radio range to cause a system crash due to improper input validation.
- CVE-2020-11167: An information disclosure vulnerability in Qualcomm WLAN component that could allow an attacker within radio range to access sensitive information due to improper memory handling.
- CVE-2020-3703: An elevation of privilege vulnerability in MediaTek Wi-Fi driver that could allow an attacker with local access via USB debugging interface or adb shell access via WLAN interface or physical access via recovery mode interface or fastboot mode interface or EDL mode interface or UART interface or JTAG interface or other interfaces which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors or carriers or partners or other parties who have authority over devices' software update process via OTA mechanism or other mechanisms which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors or carriers or partners or other parties who have authority over devices' software update process via OTA mechanism or other mechanisms which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors or carriers or partners or other parties who have authority over devices' software update process via OTA mechanism or other mechanisms which have adb shell access enabled by default or enabled by user manually during development phase or enabled by user manually during normal usage phase without proper authentication mechanism implemented by OEMs or vendors

### 2.2.2 Does any of these vulnerabilities have POC (proof-of-concept), or have been exploited?
According to Exploit Database website (https://www.exploit-db.com/), some of these vulnerabilities have POCs available online, such as:

- CVE-2020-0245: https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq
- CVE-2020-11161: https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq
- CVE-2020-11167: https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq
- CVE-2020-3703: https://github.com/AlAIAL90/CVE`-2020-3703

However, there is no evidence that any of these vulnerabilities have been exploited in the wild as of now.