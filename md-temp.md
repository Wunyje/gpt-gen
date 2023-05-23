`
# Bluetooth Penetration Testing on Android 10 Device

Bluetooth penetration testing is a method of finding and exploiting security vulnerabilities in bluetooth-enabled devices and applications. It can help identify risks and improve the security posture of mobile devices. Bluetooth penetration testing involves various steps, such as:

## 2 What is Bluetooth penetration test?

A Bluetooth penetration test is a type of security assessment that aims to discover and exploit weaknesses in the Bluetooth protocol stack, the Bluetooth services, and the Bluetooth applications on a target device. A Bluetooth penetration test can reveal information leakage, unauthorized access, denial of service, or remote code execution vulnerabilities.

### 2.1 How could it be implemented on Android 10 device?

To perform a Bluetooth penetration test on an Android 10 device, one needs to have a compatible Bluetooth adapter, a Linux system with BlueZ installed, and some tools for scanning, sniffing, and attacking Bluetooth devices.

#### 2.1.1 What tools are needed?

Some of the tools that are needed for Bluetooth penetration testing are:

##### 2.1.1.1 How to use these tools individually or together? (Use examples to illustrate)

- hcitool: This tool can be used to scan for nearby Bluetooth devices, inquire their information, and send commands to them. For example, `hcitool scan` can list the MAC addresses and names of nearby devices, `hcitool info <MAC>` can show the device class and supported features of a device, and `hcitool cc <MAC>` can create a connection with a device.
- bluetoothctl: This tool can be used to interact with Bluetooth devices using an interactive shell. For example, `bluetoothctl` can launch the shell, `scan on` can start scanning for devices, `pair <MAC>` can pair with a device, `connect <MAC>` can connect to a device, and `info <MAC>` can show the device information.
- bettercap: This tool can be used to perform various attacks on Bluetooth devices, such as spoofing, hijacking, jamming, or exploiting vulnerabilities. For example, `bettercap -iface <interface>` can launch bettercap with a specific interface, `ble.recon on` can start scanning for BLE devices, `ble.show` can show the discovered devices and their services and characteristics, `ble.connect <MAC>` can connect to a BLE device, `ble.enum <MAC>` can enumerate the services and characteristics of a BLE device, and `ble.write <MAC> <UUID> <value>` can write a value to a characteristic of a BLE device.
- bluediving: This tool is a suite of exploits for Bluetooth devices, such as Bluebug, BlueSnarf, BlueSnarf++, or BlueSmack. For example, `bluediving -b <MAC>` can launch bluediving with a specific target device, `bluebug` can access the AT commands of the target device, `bluesnarf` can download files from the target device, `bluesnarf++` can upload files to the target device, and `bluesmack` can send L2CAP packets to crash the target device.

##### 2.1.1.2 How to use MSF to penetrate Bluetooth on Android 10 device?

MSF (Metasploit Framework) is a popular tool for exploiting vulnerabilities in various systems and applications. MSF has some modules for Bluetooth exploitation, such as:

- auxiliary/scanner/bluetooth/bluetooth_discover: This module can scan for nearby Bluetooth devices and show their information.
- auxiliary/scanner/bluetooth/bluetooth_pair: This module can attempt to pair with a Bluetooth device using a PIN brute force attack.
- auxiliary/scanner/bluetooth/bluetooth_ping: This module can ping a Bluetooth device and measure its response time.
- auxiliary/scanner/bluetooth/identify_services: This module can identify the services offered by a Bluetooth device.
- exploit/linux/bluetooth/blueborne_l2cap_rce: This module can exploit a remote code execution vulnerability (CVE-2017-1000251) in the L2CAP implementation of Linux kernel versions 3.3-rc1 through 4.13.1.

To use MSF for Bluetooth penetration testing on an Android 10 device, one needs to have MSF installed on a Linux system with BlueZ and Ruby installed. Then, one can launch MSF with `msfconsole`, load a module with `use <module>`, set the options with `set <option> <value>`, and run the module with `run` or `exploit`.

#### 2.1.2 Targeting at Bluedroid, what things could be done to penetrate that?

Bluedroid is the default Bluetooth stack implementation on Android devices since version 4.2. It consists of two components: Bluedroid Core and Bluedroid External.

Bluedroid Core is responsible for managing the Bluetooth controller and handling HCI commands and events. It runs as part of the system_server process with high privileges.

Bluedroid External is responsible for providing Bluetooth profiles and services to applications. It runs as part of the com.android.bluetooth process with low privileges.

To penetrate Bluedroid, one could try to find and exploit vulnerabilities in either component or in their communication channel.

Some examples of things that could be done to penetrate Bluedroid are:

- Fuzzing Bluedroid Core with malformed HCI packets or commands and looking for crashes or memory corruption.
- Fuzzing Bluedroid External with malformed SDP requests or responses and looking for crashes or memory corruption.
- Sniffing or spoofing HCI packets or commands between Bluedroid Core and Bluedroid External and looking for information leakage or logic flaws.
- Exploiting known vulnerabilities in Bluedroid Core or Bluedroid External, such as CVE-2017-0781 (arbitrary code execution via crafted SDP packets), CVE-2017-0785 (information disclosure via crafted SDP packets), CVE-2018-9489 (information disclosure via crafted intent broadcasts), CVE-2020-0022 (remote code execution via crafted L2CAP packets), or CVE-2020-0245 (denial of service via crafted AVDTP packets).

### 2.2 How to utilize existing CVE vulnerabilities of Bluetooth on Android 10?

To utilize existing CVE vulnerabilities of Bluetooth on Android 10, one needs to have access to the details of the vulnerabilities, such as their impact, affected versions, attack vectors, exploit code, patches, or mitigations.

One could use various sources to find such information, such as:

- The official Android Security Bulletins: https://source.android.com/security/bulletin
- The official CVE database: https://cve.mitre.org
- The NVD database: https://nvd.nist.gov
- The Exploit Database: https://www.exploit-db.com
- The Metasploit Framework: https://www.metasploit.com

Once one has obtained the information about a vulnerability, one could try to reproduce it on an Android 10 device using the provided exploit code or creating one's own based on the vulnerability description.

#### 2.2.1 What are the CVE vulnerabilities about Bluetooth on Android 10 after 2020?

According to the official Android Security Bulletins (https://source.android.com/security/bulletin), some of the CVE vulnerabilities about Bluetooth on Android 10 after 2020 are:

| CVE ID | Severity | Description |
| --- | --- | --- |
| CVE-2020-0022 | Critical | In reassemble_and_dispatch of packet_fragmenter.cc , there is possible out of bounds write due to an incorrect bounds calculation . This could lead to remote code execution over Bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -143894715 |
| CVE-2020-0245 | High | In avdtp_process_browse_packet of avdtp_main.cc , there is possible out of bounds read due to an incorrect bounds check . This could lead to remote information disclosure over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -147802522 |
| CVE-2020-0383 | High | In btif_a2dp_audio_interface_start_session of btif_a2dp_audio_interface.cc , there is possible out of bounds write due to an incorrect bounds calculation . This could lead to remote escalation of privilege over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -149163161 |
| CVE-2020-0396 | High | In avdtp_process_browse_packet of avdtp_main.cc , there is possible out of bounds write due to an incorrect bounds check . This could lead to remote escalation of privilege over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -147802522 |
| CVE-2020-0397 | High | In avdtp_process_browse_packet of avdtp_main.cc , there is possible out of bounds read due to an incorrect bounds check . This could lead to remote information disclosure over bluetooth with no additional execution privileges needed . User interaction is not needed for exploitation . Product : Android Versions : Android -10 Android ID : A -