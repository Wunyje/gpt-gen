In this blog post, we will explore the process of reversing the image files of SD690, a Qualcomm Snapdragon processor that is used in some Android devices. We will also discuss the interaction between SD690 and RH850, a Renesas microcontroller that is used in some automotive applications. Our goal is to understand how these two chips communicate with each other and what information they exchange.

## 1. What is SD690 and RH850?

SD690 is a 64-bit octa-core system-on-chip (SoC) that was released by Qualcomm in 2020. It is based on the 8nm LPP process and supports 5G connectivity, Wi-Fi 6, Bluetooth 5.1, NFC, GPS, and other features. It has a Kryo 560 CPU, an Adreno 619L GPU, a Hexagon 692 DSP, a Spectra 355L ISP, and a Snapdragon X51 modem.

RH850 is a family of 32-bit microcontrollers that was developed by Renesas Electronics for automotive applications. It is based on the V850 architecture and supports various automotive standards, such as CAN, LIN, FlexRay, Ethernet AVB, and SENT. It has a high-performance CPU core, a large memory capacity, and various peripheral functions.

### 1.1 What is the relationship between them?

SD690 and RH850 are two different chips that are used in different domains. However, they can be connected to each other via a serial interface, such as UART or SPI. This allows them to exchange data and commands for various purposes, such as diagnostics, configuration, control, or monitoring. For example, SD690 can send commands to RH850 to perform certain tasks or read certain sensors, and RH850 can send data to SD690 to report its status or results.

## 2. What is the target of this reversing?

The target of this reversing is to figure out the interaction between SD690 and RH850 by reversing specific image files.

## 3. What are the image files in SD690?

The image files in SD690 are binary files that contain the firmware or software components that run on different parts of the SoC. They are usually stored in the device's flash memory or loaded into the device's RAM during booting or updating. Some of them are encrypted or signed for security reasons.

### 3.1 What are the image files' function?

The image files' function depends on their name and content. Here is a brief description of them:

|Name|Content|
|----|----|
| abl.img| Android Boot Loader. It is responsible for initializing the hardware and loading the kernel into memory.|
| aop.img| Always On Processor. It is a low-power processor that handles tasks such as power management and sensor processing.|
| bluetooth.img| Bluetooth firmware. It contains the code and data for the Bluetooth functionality of the device.|
| boot.img| Boot image. It contains the kernel and the ramdisk that are used to boot the Android system.|
| core_nhlos.img| Core Non-HLOS image. It contains the firmware for the modem and other non-HLOS components of the device.|
| devcfg.img| Device Configuration image. It contains the configuration data for the device's hardware components.|
| dsp.img| Digital Signal Processor image. It contains the firmware for the DSP that handles audio and video processing.|
| dtbo.img| Device Tree Blob Overlay image. It contains the device tree overlays that are applied to the base device tree during booting.|
| featenabler.img| Feature Enabler image. It contains the code and data for enabling certain features of the device.|
| hyp.img| Hypervisor image. It contains the code for the hypervisor that manages the virtualization of the device's resources.|
| imagefv.img| Image File Verification image. It contains the signatures and certificates for verifying the integrity of other images.|
| keymaster.img| Keymaster image. It contains the code and data for the keymaster service that handles cryptographic operations on the device.|
| modem.img| Modem image. It contains the firmware for the modem that handles cellular connectivity on the device.|
| multiimgoem.img| Multi Image OEM image. It contains multiple images that are specific to a certain OEM or device model.|
| product.img| Product image. It contains the product-specific files that are part of the Android system.|
| qupfw.img| Qualcomm Unified Peripheral Firmware image. It contains the firmware for various peripheral devices on the SoC.|
| recovery.img| Recovery image. It contains the code and data for the recovery mode that allows users to perform maintenance tasks on their device.|
| system.img| System image. It contains the system partition that holds most of the Android system files.|
| tz.img| TrustZone image. It contains the code and data for the TrustZone service that handles secure operations on the device.|
| uefisecapp.img| UEFI Secure Application image. It contains an application that runs in UEFI mode before booting into Android.|
| vbmeta.img| Verified Boot Metadata image. It contains metadata for verifying other images during booting using Android Verified Boot (AVB).|
| vbmeta_system.img| Verified Boot Metadata System image. It contains metadata for verifying system images during booting using AVB.|
| vendor.img| Vendor image. It contains vendor-specific files that are part of the Android system.|
| xbl_config.img| eXtensible Boot Loader Configuration image. It contains configuration data for XBL.|
| xbl.img| eXtensible Boot Loader image. It contains code for XBL.|

### 3.2 Which image file or files should be reversed?

The answer to this question depends on what kind of information we want to extract from them. However,
some general guidelines are:

- If we want to understand how SD690 communicates with RH850 via serial interface,
we should reverse **modem** or **core_nhlos** images,
as they contain firmware for handling cellular connectivity
and may have code or data related to RH850 communication protocol.
- If we want to understand how SD690 configures or controls RH850 via serial interface,
we should reverse **devcfg** or **multiimgoem** images,
as they contain configuration data for hardware components
and may have settings or commands related to RH850 functionality.
- If we want to understand how SD690 monitors or receives data from RH850 via serial interface,
we should reverse **dsp** or **aop** images,
as they contain firmware for audio and video processing
and sensor processing
and may have code or data related to RH850 data format or interpretation.

Of course,
these are not exhaustive lists
and other images may also contain relevant information
depending on their content
and how they interact with each other
or with external devices.
#### 3.2.1 How to reverse in general?

The general steps to reverse in details are as follows:

**The first step** is to obtain the image files from the device. There are different ways to do this, such as using adb commands, extracting from OTA updates, or dumping from memory. The image files are usually located in /dev/block/bootdevice/by-name/ or /firmware/image/ directories on the device. The image files have names like boot.img, modem.img, dsp.img, etc.

**The second step** is to analyze the image files and identify their format and structure. Some image files are encrypted or signed, and need to be decrypted or verified before they can be opened. Some image files are compressed or packed, and need to be decompressed or unpacked before they can be read. Some image files are split into multiple segments or partitions, and need to be concatenated or merged before they can be loaded.

**The third step** is to load the image files into a disassembler or a debugger and start reversing them. Depending on the type of the image file, different tools may be needed. For example, boot.img contains the Linux kernel and initramfs, and can be reversed using tools like IDA Pro or Ghidra. Modem.img contains the modem firmware and can be reversed using tools like QCSuper or QXDM. Dsp.img contains the DSP firmware and can be reversed using tools like Hex-Rays Decompiler or radare2.

**The fourth step** is to understand the functionality and logic of the image files and find interesting code or data. This may require some background knowledge of the Qualcomm SoC architecture and firmware design. Some useful resources are the Qualcomm Developer Network (QDN), the Code Aurora Forum (CAF), and various blogs and papers by security researchers. Some common tasks are finding system calls, finding encryption keys, finding debug messages, finding vulnerabilities, etc.

**The fifth step** is to modify the image files and test them on the device. This may require some tools to re-encrypt, re-sign, re-compress, or re-pack the image files after modification. Some tools are available online, such as Magisk for boot.img or QPST for modem.img. Some tools may need to be developed by yourself, such as for dsp.img. Some modifications may require rooting the device or unlocking the bootloader.

These are some general methods and procedures of reversing Qualcomm SD690's image files. They are not exhaustive or definitive, but rather a starting point for further exploration. Reversing Qualcomm SD690's image files can be challenging but rewarding, as it can reveal many secrets and possibilities of the device.



In summary,
reversing SD690 image files
is a challenging but rewarding task
that can reveal interesting insights
into how two different chips
work together
in a complex system.