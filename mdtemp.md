# Indroduction about `Reversing SD690 Image Files`:

## 1. What is SD690 and RH850?

SD690 is a system-on-chip (SoC) developed by Qualcomm for mid-range 5G smartphones. It integrates an octa-core CPU, an Adreno 619L GPU, a Snapdragon X51 5G modem, and other components on a single chip.

RH850 is a microcontroller family designed by Renesas for automotive applications. It features a 32-bit RISC core, various peripherals, and a real-time operating system.

### 1.1 What is the relationship between them?

SD690 and RH850 can communicate with each other through a serial interface or a CAN bus. They can exchange data and commands for different functions, such as navigation, entertainment, diagnostics, and safety.

## 2. What is the target of this reversing?

The target of this reversing is to figure out the interaction between SD690 and RH850 by reversing specific image files in information delimited by double backticks.

## 3. What are the image files in SD690?

The image files in SD690 are binary files that contain the firmware, bootloader, kernel, system partition, vendor partition, and other components of the Android operating system.

### 3.1 What are the image files' function?

The image files' function are as follows:

- abl.img: Android Bootloader (ABL), which initializes the hardware and loads the kernel.
- aop.img: Always-On Processor (AOP), which handles low-power tasks such as sensor processing and power management.
- bluetooth.img: Bluetooth firmware, which provides the Bluetooth functionality for the device.
- boot.img: Boot image, which contains the kernel and the ramdisk.
- core_nhlos.img: Core non-high-level operating system (NHLOS) image, which contains the firmware for the modem and other subsystems.
- devcfg.img: Device configuration image, which contains the configuration data for the device.
- dsp.img: Digital signal processor (DSP) image, which contains the firmware for the audio and video processing.
- dtbo.img: Device tree blob overlay (DTBO) image, which contains the device tree overlays that modify the device tree at boot time.
- featenabler.img: Feature enabler image, which contains the feature flags that enable or disable certain features on the device.
- hyp.img: Hypervisor image, which contains the hypervisor that manages the virtualization of the hardware resources.
- imagefv.img: Image file verification (IFV) image, which contains the signatures and hashes of the other image files for verification purposes.
- keymaster.img: Keymaster image, which contains the firmware for the keymaster module that handles cryptographic operations and key management.
- modem.img: Modem image, which contains the firmware for the Snapdragon X51 5G modem.
- multiimgoem.img: Multi-image OEM image, which contains the OEM-specific firmware and data.
- product.img: Product image, which contains the product-specific system partition.
- qupfw.img: Qualcomm Unified Peripheral Firmware (QUPFW) image, which contains the firmware for the QUP peripheral interface that connects to various sensors and devices.
- recovery.img: Recovery image, which contains the recovery mode that allows users to perform factory reset, update, or troubleshoot their device.
- system.img: System image, which contains the system partition that holds the core Android framework and applications.
- tz.img: TrustZone image, which contains the firmware for the TrustZone module that provides a secure execution environment for sensitive tasks.
- uefisecapp.img: UEFI Secure Application (UEFI SecApp) image, which contains the firmware for the UEFI SecApp module that provides secure boot and authentication services.
- vbmeta.img: Verified boot metadata (VBMeta) image, which contains the metadata for verified boot that checks the integrity of the boot chain.
- vbmeta_system.img: VBMeta system image, which contains the VBMeta data for the system partition.
- vendor.img: Vendor image, which contains the vendor-specific system partition that holds the drivers and libraries for the hardware components.
- xbl_config.img: Extensible Bootloader Configuration (XBL Config) image, which contains the configuration data for the extensible bootloader (XBL).
- xbl.img: XBL image, which contains the XBL that loads and verifies the ABL.

### 3.2 Which image file or files should be reversed?

The answer to this question depends on what kind of information or functionality one wants to extract from the interaction between SD690 and RH850. For example:

- If one wants to analyze how SD690 communicates with RH850 through a serial interface or a CAN bus, one should reverse **core_nhlos.img**, **devcfg.img**, **dsp.img**, **qupfw.img**, **tz.img**, **uefisecapp.img**, **xbl_config.img**, and **xbl.img**. These images contain
the firmware and configuration data for various subsystems that handle serial or CAN communication protocols.

- If one wants to understand how SD690 controls or monitors RH850's functions such as navigation,
entertainment,
diagnostics,
and safety,
one should reverse **abl.img**,
**aop.img**,
**boot.img**,
**dtbo.img**,
**featenabler.img**,
**hyp.img**,
**keymaster.img**,
**modem.img**,
**multiimgoem.img**,
**product.img**,
**recovery.img**,
**system.img**,
**vbmeta_system.img**, 
and **vendor.img**. These images contain
the bootloader,
kernel,
ramdisk,
device tree overlays,
feature flags,
hypervisor,
keymaster module,
modem firmware,
OEM-specific firmware and data,
product-specific system partition,
recovery mode,
system partition,
VBMeta data for system partition,
and vendor-specific system partition
that implement or interact with RH850's functions.

#### 3.2.1 How to reverse in details

The general steps to reverse in details are as follows:

1. Extract each image file from SD690 using tools such as fastboot or dd.
2. Identify each image file's format using tools such as binwalk or file.
3. Decompress or unpack each image file using tools such as simg2img or unsparse if needed.
4. Disassemble each image file using tools such as IDA Pro or Ghidra if it contains executable code.
5. Analyze each image file using tools such as hex editor or strings if it contains data or configuration information.
6. Identify each image file's function using tools such as QEMU or Android emulator if it can be executed or loaded on a virtual device.
7. Trace each image file's interaction with RH850 using tools such as JTAG or UART if it can be debugged or monitored on a physical device.

