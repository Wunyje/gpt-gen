`
Introduction of Bluetooth penetration test on Android 10 device
# 1 What is Bluetooth?
Bluetooth is a wireless technology that allows devices to communicate over short distances. It uses radio waves to transmit data between devices that are paired with each other. Bluetooth devices can operate in different modes, such as classic, low energy, or dual mode.
## 1.1  How does Bluetooth work on Android 10 device?
On an Android 10 device, Bluetooth works by using a system service called BluetoothManager. This service provides access to the underlying Bluetooth hardware and software components, such as the Bluetooth adapter, profile proxy, and GATT server and client. The Bluetooth adapter is responsible for managing the device's Bluetooth state, scanning for nearby devices, initiating and accepting connections, and exchanging data. The profile proxy is an interface that allows applications to interact with different Bluetooth profiles, such as A2DP (Advanced Audio Distribution Profile), HFP (Hands-Free Profile), or HID (Human Interface Device). The GATT server and client are components that enable applications to use the Bluetooth Low Energy (BLE) protocol, which is designed for low-power devices that exchange small amounts of data.
## 1.1.1 Have heared about `Bluedroid`? What's that?
Bluedroid is the name of the Bluetooth stack implementation on Android devices. It consists of two main components: the Bluedroid daemon (bluetoothd) and the Bluedroid library (libbluetooth). The Bluedroid daemon handles the communication with the Bluetooth controller using the HCI (Host Controller Interface) protocol. The Bluedroid library provides the APIs for applications to use the Bluetooth functionality.
## 1.2 How does that work differently from Linux OS?
On a Linux OS, Bluetooth works by using a system daemon called BlueZ. This daemon provides access to the underlying Bluetooth hardware and software components, such as the Bluetooth controller, HCI (Host Controller Interface), L2CAP (Logical Link Control and Adaptation Protocol), RFCOMM (Radio Frequency Communication), and SDP (Service Discovery Protocol). The Bluetooth controller is responsible for managing the device's Bluetooth state, scanning for nearby devices, initiating and accepting connections, and exchanging data. The HCI is an interface that allows applications to communicate with the Bluetooth controller using commands and events. The L2CAP is a protocol that multiplexes multiple logical channels over a single physical link. The RFCOMM is a protocol that emulates serial ports over L2CAP channels. The SDP is a protocol that allows applications to discover and use services offered by other Bluetooth devices.
# 2 What is Bluetooth penetration test?
Bluetooth penetration testing is a method of finding and exploiting security vulnerabilities in Bluetooth-enabled devices and applications. It can help identify risks and improve the security posture of mobile devices.
## 2.1 How could it be implemented on Android 10 device?
To perform a Bluetooth penetration test on an Android 10 device, one needs to set up the pentesting environment first. This includes preparing the Android device and the local computer, unlocking the bootloader, rooting the device, installing custom recovery, enabling developer options and USB debugging, installing ADB (Android Debug Bridge) and Fastboot tools on the computer, connecting the device to the computer via USB cable or Wi-Fi. Then, one can use various tools and techniques to enumerate, analyze, manipulate, and exploit the Bluetooth functionality on the device.
## 2.1.1 What tools are needed?
Some of the tools that are useful for Bluetooth penetration testing on Android 10 device are:

- nRF Connect: An app that can scan for nearby BLE devices and services, read and write characteristics and descriptors, monitor notifications and indications, perform GATT operations, etc.
- BLE Scanner: An app that can scan for nearby BLE devices and services, read and write characteristics and descriptors, monitor notifications and indications, etc.
- Blue Hydra: A tool that can detect classic and BLE devices in range, collect information about them such as MAC address, name, vendor, RSSI (Received Signal Strength Indicator), etc., identify known devices from a database of previously seen devices, etc.
- Btlejuice: A tool that can perform a man-in-the-middle attack on BLE connections between two devices, intercept and modify GATT traffic, clone BLE devices and services, etc.
- Bettercap: A tool that can perform various network attacks on classic and BLE devices, such as ARP spoofing, DNS spoofing, HTTP proxying, SSL stripping, etc., as well as sniffing and injecting HCI packets.
- Metasploit Framework: A tool that can perform various exploits on classic and BLE devices using modules such as bluetooth_version.rb (to get the version of the remote device), bluetooth_name.rb (to get or set the name of the remote device), bluetooth_pairing_pin.rb (to brute force the pairing PIN of the remote device), bluetooth_dos.rb (to perform a denial-of-service attack on the remote device), etc .
## 2.1.1.1 How to use these tools individually or together? (Use examples to illustrate)
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