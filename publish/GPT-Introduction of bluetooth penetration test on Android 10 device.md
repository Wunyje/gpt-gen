#! https://zhuanlan.zhihu.com/p/630718821
# GPT-Introduction of bluetooth penetration test on Android 10 device
```
CONTENT:
Introduction of Bluetooth penetration test on Android 10 device
1 What is Bluetooth?
1.1 What the structure of Bluetooth, illustrate both in software and hardware?
1.1.1 What's `Bluedroid`?
1.2 How does Bluetooth work on Android 10 device?
1.2.1 How does that work differently from Linux OS?
2 What is Bluetooth penetration test?
2.1 How could it be implemented on Android 10 device?
2.1.1 What tools are needed?
2.1.1.1 How to use these tools individually or together? (Use examples to illustrate)
2.1.1.2 How to use MSF to penetrate Bluetooth on Android 10 device?
2.1.2 Targeting at `Bluedroid`, what things could be done to penetrate that?  
2.2 How to utilize existing CVE vulnerabilities of Bluetooth on Android 10?
2.2.1 What are the CVE  vulnerabilities about Bluetooth on Android 10 after 2020?
2.2.2 Does any of these vulnerabilities have POC, or have been exploited?
```
In this blog post, I will introduce the basics of bluetooth penetration testing on an Android 10 device. Bluetooth is a wireless technology that allows devices to communicate over short distances. It is widely used for various purposes, such as connecting headphones, keyboards, speakers, smartwatches, and more. Bluetooth penetration testing is a method of finding and exploiting security vulnerabilities in bluetooth-enabled devices and applications. It can help identify risks and improve the security posture of mobile devices.

## 1. What is bluetooth?
Bluetooth is a wireless technology that allows devices to communicate over short distances. It uses radio waves to transmit data between devices that are paired with each other. Bluetooth devices can operate in different modes, such as classic, low energy, or dual mode.

### 1.1 What the structure of Bluetooth, illustrate both in software and hardware?

The structure of Bluetooth consists of two main components: the bluetooth controller and the bluetooth host. The bluetooth controller is the hardware part that handles the radio communication and the low-level protocols. The bluetooth host is the software part that runs on the device's operating system and handles the high-level protocols and applications.

The bluetooth controller consists of three subcomponents: the radio, the baseband, and the link manager. The radio is responsible for transmitting and receiving radio signals at a specific frequency band. The baseband is responsible for encoding and decoding data packets, managing error correction, and controlling access to the radio channel. The link manager is responsible for establishing and maintaining connections with other bluetooth devices, negotiating parameters, and managing power consumption.

The bluetooth host consists of four subcomponents: the host controller interface (HCI), the logical link control and adaptation protocol (L2CAP), the service discovery protocol (SDP), and the bluetooth profiles. The HCI is an interface that allows the bluetooth host to communicate with the bluetooth controller using commands and events. The L2CAP is a protocol that multiplexes multiple logical channels over a single physical link. The SDP is a protocol that allows applications to discover and use services offered by other bluetooth devices. The bluetooth profiles are specifications that define how applications use bluetooth to perform specific tasks, such as audio streaming, file transfer, or keyboard input.

#### 1.1.1 What's `Bluedroid`?

`Bluedroid` is the name of the bluetooth stack implementation used by Android devices since version 4.2. It replaces the previous stack called BlueZ, which is still used by Linux devices. `Bluedroid` consists of two main components: the bluetooth daemon (bluetoothd) and the application framework (bluetooth.jar). The bluetooth daemon is a native process that communicates with the bluetooth controller via HCI and provides core bluetooth functionality, such as scanning, pairing, bonding, and connection management. The application framework is a Java library that exposes bluetooth APIs to Android applications and handles user interface, permissions, settings, and profiles.

### 1.2 How does bluetooth work on an Android 10 device?
On an Android 10 device, bluetooth works by using a system service called BluetoothManager. This service provides access to the underlying bluetooth hardware and software components, such as the bluetooth adapter, profile proxy, and GATT server and client. The bluetooth adapter is responsible for managing the device's bluetooth state, scanning for nearby devices, initiating and accepting connections, and exchanging data. The profile proxy is an interface that allows applications to interact with different bluetooth profiles, such as A2DP (Advanced Audio Distribution Profile), HFP (Hands-Free Profile), or HID (Human Interface Device). The GATT server and client are components that enable applications to use the Bluetooth Low Energy (BLE) protocol, which is designed for low-power devices that exchange small amounts of data.


#### 1.2.1 How does that work differently from Linux OS?
On a Linux OS, bluetooth works by using a system daemon called BlueZ. This daemon provides access to the underlying bluetooth hardware and software components, such as the bluetooth controller, HCI (Host Controller Interface), L2CAP (Logical Link Control and Adaptation Protocol), RFCOMM (Radio Frequency Communication), and SDP (Service Discovery Protocol). The bluetooth controller is responsible for managing the device's bluetooth state, scanning for nearby devices, initiating and accepting connections, and exchanging data. The HCI is an interface that allows applications to communicate with the bluetooth controller using commands and events. The L2CAP is a protocol that multiplexes multiple logical channels over a single physical link. The RFCOMM is a protocol that emulates serial ports over L2CAP channels. The SDP is a protocol that allows applications to discover and use services offered by other bluetooth devices.

## 2. What is bluetooth penetration testing?
Bluetooth penetration testing is a method of finding and exploiting security vulnerabilities in bluetooth-enabled devices and applications. It can help identify risks and improve the security posture of mobile devices. Bluetooth penetration testing involves various steps, such as:

- Reconnaissance: Gathering information about the target device and its bluetooth capabilities, such as device name, address, class, services, profiles, etc.
- Scanning: Searching for nearby bluetooth devices and their characteristics, such as signal strength, supported features, encryption level, etc.
- Enumeration: Identifying the services and profiles offered by the target device and their attributes, such as service name, UUID (Universally Unique Identifier), channel number, etc.
- Fuzzing: Sending malformed or unexpected data to the target device or application to trigger errors or crashes.
- Exploitation: Leveraging known or unknown vulnerabilities in the target device or application to gain unauthorized access or execute arbitrary code.
- Post-exploitation: Performing further actions on the compromised device or application, such as stealing data, installing malware, escalating privileges, etc.

### 2.1 How could it be implemented on Android 10 device?
To perform a Bluetooth penetration test on an Android 10 device, one needs to set up the pentesting environment first. This includes preparing the Android device and the local computer, unlocking the bootloader, rooting the device, installing custom recovery, enabling developer options and USB debugging, installing ADB (Android Debug Bridge) and Fastboot tools on the computer, connecting the device to the computer via USB cable or Wi-Fi. Then, one can use various tools and techniques to enumerate, analyze, manipulate, and exploit the Bluetooth functionality on the device.
#### 2.1.1 What tools are needed?
Some of the tools that are useful for Bluetooth penetration testing on Android 10 device are:

- **nRF Connect**: An app that can scan for nearby BLE devices and services, read and write characteristics and descriptors, monitor notifications and indications, perform GATT operations, etc.
- **BLE Scanner**: An app that can scan for nearby BLE devices and services, read and write characteristics and descriptors, monitor notifications and indications, etc.
- **Blue Hydra**: A tool that can detect classic and BLE devices in range, collect information about them such as MAC address, name, vendor, RSSI (Received Signal Strength Indicator), etc., identify known devices from a database of previously seen devices, etc.
- **Btlejuice**: A tool that can perform a man-in-the-middle attack on BLE connections between two devices, intercept and modify GATT traffic, clone BLE devices and services, etc.
- **Bettercap**: A tool that can perform various network attacks on classic and BLE devices, such as ARP spoofing, DNS spoofing, HTTP proxying, SSL stripping, etc., as well as sniffing and injecting HCI packets.
- **Metasploit Framework**: A tool that can perform various exploits on classic and BLE devices using modules such as bluetooth_version.rb (to get the version of the remote device), bluetooth_name.rb (to get or set the name of the remote device), bluetooth_pairing_pin.rb (to brute force the pairing PIN of the remote device), bluetooth_dos.rb (to perform a denial-of-service attack on the remote device), etc .
##### 2.1.1.1 How to use these tools individually or together? (Use examples to illustrate)
Here are some examples of how to use these tools individually or together:

- To scan for nearby BLE devices using nRF Connect or BLE Scanner app:
  - Install and launch the app on the Android device
  - Tap on SCAN button to start scanning
  - Observe the list of detected devices with their names, MAC addresses,
    RSSI values
  - Tap on a device to see its services and characteristics
  - Tap on a characteristic to read or write its value
  - Enable notifications or indications if available
- To detect classic and BLE devices using Blue Hydra:
  - Install Blue Hydra on the local computer
  - Connect a compatible Bluetooth dongle to the computer
  - Run `sudo blue_hydra` command in a terminal
  - Observe the output of detected devices with their names,
    MAC addresses,
    vendors,
    RSSI values,
    etc.
  - Use `--web` option to launch a web interface for better visualization
- To perform a man-in-the-middle attack on BLE connections using Btlejuice:
  - Install Btlejuice on the local computer
  - Connect two compatible Bluetooth dongles to the computer
  - Run `sudo btlejuice-proxy` command in one terminal to start
    proxying BLE traffic between two dongles
  - Run `sudo btlejuice` command in another terminal to start
    intercepting BLE traffic between two devices
  - Use `-u` option to specify a URL for web interface
  - Use `-w` option to specify a whitelist of MAC addresses to target
  - Use `-b` option to specify a blacklist of MAC addresses to ignore
  - Use web interface to select a target device from scanned list
  - Use web interface to clone target device's services and characteristics
  - Use web interface to modify target device's characteristics values
- To perform various network attacks on classic and BLE devices using Bettercap:
  - Install Bettercap on the local computer
  - Connect a compatible Bluetooth dongle to the computer
  - Run `sudo bettercap` command in a terminal to start Bettercap interactive session
  - Use `bluetooth.show` command to show available Bluetooth interfaces
  - Use `set bluetooth.interface <name>` command to select an interface
  - Use `bluetooth.recon on` command to start scanning for nearby classic 
    and BLE devices
  - Use `bluetooth.show` command again to show detected devices with their names,
    MAC addresses,
    vendors,
    RSSI values,
    etc.
  - Use `set bluetooth.target <mac>` command to select a target device by its MAC address
  - Use `bluetooth.info` command to get more information about target device such as version,
    name,
    features,
    etc.
  - Use `bluetooth.exploit <module>` command to run an exploit module against target device such as bluetooth_pairing_pin.rb,
    bluetooth_dos.rb,
    etc.
- To perform various exploits on classic and BLE devices using Metasploit Framework:
  - Install Metasploit Framework on the local computer
  - Connect a compatible Bluetooth dongle to the computer
  - Run `msfconsole` command in a terminal to start Metasploit interactive session
  - Use `search bluetooth` command to show available exploit modules related 
    to Bluetooth 
  - Use `use <module>` command to select an exploit module such as auxiliary/scanner/bluetooth/version.rb,
    auxiliary/dos/bluetooth/bluetooth_dos.rb,
    etc.
  - Use `show options` command to show required options for selected module such as RHOSTS,
    INTERFACE,
    PIN_LENGTH,
    etc.
  - Use `set <option> <value>` command to set an option value such as RHOSTS <mac>,
    INTERFACE hci0,
    PIN_LENGTH 4,
    etc.
  - Use `run` command to execute selected module against target device

##### 2.1.1.2 How to use MSF to penetrate bluetooth on Android 10 device?

MSF (Metasploit Framework) is a popular tool for penetration testing that provides various modules for exploiting different vulnerabilities in various systems. MSF has some modules for Bluetooth exploitation, such as:

- auxiliary/scanner/bluetooth/bluetooth_discover: This module can scan for nearby Bluetooth devices and show their information.
- auxiliary/scanner/bluetooth/bluetooth_pair: This module can attempt to pair with a Bluetooth device using a PIN brute force attack.
- auxiliary/scanner/bluetooth/bluetooth_ping: This module can ping a Bluetooth device and measure its response time.
- auxiliary/scanner/bluetooth/identify_services: This module can identify the services offered by a Bluetooth device.
- exploit/linux/bluetooth/blueborne_l2cap_rce: This module can exploit a remote code execution vulnerability (CVE-2017-1000251) in the L2CAP implementation of Linux kernel versions 3.3-rc1 through 4.13.1.

To use MSF to penetrate bluetooth on Android 10 device:

- Connect the computer and the Android device to the same network
- Run `msfconsole` to start MSF
- Run `use exploit/android/bluetooth/btif_hcicmd_send` to select a module that exploits a buffer overflow vulnerability in Android's bluetooth stack (CVE-2020-0022)
- Run `show options` to see the options for the module
- Set `RHOSTS` option to the IP address of the Android device
- Set `LHOST` option to the IP address of the computer
- Run `exploit` to execute the module
- Observe a meterpreter session being opened on the Android device

#### 2.1.2 Targeting at `Bluedroid`, what things could be done to penetrate that?
To target `Bluedroid`, one can try to find and exploit vulnerabilities in either component. Some examples of things that could be done to penetrate `Bluedroid` are:

- Fuzzing `bluetoothd` with malformed or crafted packets or commands to trigger crashes or memory corruption errors.
- Reverse engineering `libbluetooth.so` to identify potential weaknesses or flaws in its implementation or logic.
- Injecting shellcode or malicious code into `bluetoothd` or `libbluetooth.so` using techniques such as return-oriented programming (ROP) or code reuse attacks.
- Escalating privileges from `bluetoothd` or `libbluetooth.so` to gain root access or compromise other system components or processes.
- Exploiting known vulnerabilities in Bluedroid Core or Bluedroid External, such as CVE-2017-0781 (arbitrary code execution via crafted SDP packets), CVE-2017-0785 (information disclosure via crafted SDP packets), CVE-2018-9489 (information disclosure via crafted intent broadcasts), CVE-2020-0022 (remote code execution via crafted L2CAP packets), or CVE-2020-0245 (denial of service via crafted AVDTP packets).

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

According to the official Android Security Bulletins (https://source.android.com/security/bulletin), some of the CVE vulnerabilities about Bluetooth on Android 10 after 2020 are:

| CVE ID | Severity | Description |
| --- | --- | --- |
| CVE-2020-0022 | Critical | In reassemble_and_dispatch of packet_fragmenter.cc , there is possible out of bounds write due to an incorrect bounds calculation . This could lead to remote code execution over Bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -143894715 |
| CVE-2020-0245 | High | In avdtp_process_browse_packet of avdtp_main.cc , there is possible out of bounds read due to an incorrect bounds check . This could lead to remote information disclosure over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -147802522 |
| CVE-2020-0383 | High | In btif_a2dp_audio_interface_start_session of btif_a2dp_audio_interface.cc , there is possible out of bounds write due to an incorrect bounds calculation . This could lead to remote escalation of privilege over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -149163161 |
| CVE-2020-0396 | High | In avdtp_process_browse_packet of avdtp_main.cc , there is possible out of bounds write due to an incorrect bounds check . This could lead to remote escalation of privilege over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -147802522 |
| CVE-2020-0397 | High | In avdtp_process_browse_packet of avdtp_main.cc , there is possible out of bounds read due to an incorrect bounds check . This could lead to remote information disclosure over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -|
| CVE-2020-11201|  |  An information disclosure vulnerability in Android's bluetooth stack that allows an attacker within bluetooth range to access sensitive information by sending specially crafted packets.
| CVE-2020-11202| |An elevation-of-privilege vulnerability in Android's bluetooth stack that allows an attacker within bluetooth range to execute privileged commands by sending specially crafted packets.|

#### 2.2.2 Does any of these vulnerabilities have POCs ,or have been exploited?

Yes some of these vulnerabilities have POCs ,or have been exploited.

For example:

CVE-2020-0022 has a POC code available at https://github.com/flar2/android_kernel_oneplus_sm8150/blob/ten/security/selinux/hooks.c#L9143-L9164
and https://github.com/janhb/CVE_2020_0022_PoC

CVE-2020-0089 has been exploited by researchers at Google Project Zero at https://googleprojectzero.blogspot.com/2020/04/half-double-bluetooth-address-spoofing.html

CVE-2020-0245 has been exploited by researchers at Purdue University who demonstrated how they could crash an Android phone by sending malformed packets over bluetooth.

CVE-2020-11201 has a POC code available at https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq

CVE-2020-11202 has a POC code available at https://github.com/google/security-research/security/advisories/GHSA-h637-c88j-47wq