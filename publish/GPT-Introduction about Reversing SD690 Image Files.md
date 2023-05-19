#! https://zhuanlan.zhihu.com/p/630570012
# GPT-Introduction about `Reversing SD690 Image Files`

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
#### 3.2.1 How to reverse in details

The general steps to reverse in details are as follows:

1. Extract each image file from SD690 using tools such as fastboot or dd.
2. Identify each image file's format using tools such as binwalk or file.
3. Decompress or unpack each image file using tools such as simg2img or unsparse if needed.
4. Disassemble each image file using tools such as IDA Pro or Ghidra if it contains executable code.
5. Analyze each image file using tools such as hex editor or strings if it contains data or configuration information.
6. Identify each image file's function using tools such as QEMU or Android emulator if it can be executed or loaded on a virtual device.
7. Trace each image file's interaction with RH850 using tools such as JTAG or UART if it can be debugged or monitored on a physical device.


In summary,
reversing SD690 image files
is a challenging but rewarding task
that can reveal interesting insights
into how two different chips
work together
in a complex system.