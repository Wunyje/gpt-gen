|ID| Value|Description|
|---| --- |---|
| DEVICE_PROVISIONED | 1 | A flag that indicates whether the device has been provisioned or not. Provisioning is the process of setting up a device for use with a carrier network and a Google account. |
| aaudio.hw_burst_min_usec | 2000 | The minimum burst size in microseconds for AAudio, a low-latency audio API for Android. |
| aaudio.mmap_exclusive_policy | 2 | The policy for using exclusive mode with memory-mapped (mmap) audio streams. Exclusive mode allows an app to directly access the hardware resources of an audio device for better performance and lower latency. |
| aaudio.mmap_policy | 2 | The policy for using mmap audio streams. Mmap streams can bypass some of the audio framework processing and reduce latency and CPU usage. |
| af.fast_track_multiplier | 1 | The multiplier factor for calculating the fast track buffer size for audio playback. Fast track is a special type of audio track that can bypass some of the audio framework processing and reduce latency. |
| apps.setting.product.inswver | Di4.0_1for2_USER_SIGN_SD122_202208230003_Q0311 | The internal software version of the product. |
| apps.setting.product.outswver | 21.1.2.2208230.1 | The external software version of the product. |
| audio.deep_buffer.media | TRUE | A flag that indicates whether to use deep buffer output for media playback. Deep buffer output can increase battery life by allowing the system to enter sleep mode more often, but it can also increase latency and affect audio effects. |
| audio.offload.buffer.size.kb | 32 | The buffer size in kilobytes for offloading audio playback to a dedicated hardware module. Offloading can reduce CPU usage and power consumption, but it can also limit the supported formats and effects. |
| audio.offload.gapless.enabled | TRUE | A flag that indicates whether to enable gapless playback for offloaded audio tracks. Gapless playback can eliminate the silence or noise between consecutive tracks, but it can also increase memory usage and processing time. |
| audio.offload.min.duration.secs | 30 | The minimum duration in seconds for an audio track to be eligible for offloading. Shorter tracks may not benefit from offloading and may incur additional overhead. |
| audio.offload.video | TRUE | A flag that indicates whether to offload audio tracks from video files. |
| audio.sys.mute.latency.factor | 2 | The factor for calculating the mute latency for system sounds. Mute latency is the time it takes for the system to mute or unmute a sound when requested by an app or the user. |
| audio.sys.noisy.broadcast.delay | 500 | The delay in milliseconds before sending a broadcast intent when an audio device is connected or disconnected. The intent notifies apps that the audio configuration has changed and that they may need to adjust their output or input accordingly. |
| audio.sys.offload.pstimeout.secs | 3 | The timeout in seconds for pausing an offloaded audio track. If an offloaded track is paused for longer than this timeout, it will be stopped and released from the hardware module. |
| audio.sys.routing.latency | 0 | The latency in milliseconds for routing an audio stream to a different output or input device. Routing latency is the time it takes for the system to switch the audio path when requested by an app or the user. |
| av.offload.enable | TRUE | A flag that indicates whether to enable offloading video playback to a dedicated hardware module. Offloading can reduce CPU usage and power consumption, but it can also limit the supported formats and effects. |
| config.disable_rtt | TRUE | A flag that indicates whether to disable round-trip time (RTT) measurement for Wi-Fi networks. RTT measurement can provide accurate distance estimation between devices, but it can also consume more battery and bandwidth. |
| config.disable_vibrator | TRUE | A flag that indicates whether to disable the vibrator on the device. |
| crashlogd.token | 1 | A token that identifies the device for crash logging purposes. Crash logging is a feature that collects and reports information about system crashes and errors to help developers improve their apps and services. |
| dalvik.vm.appimageformat | lz4 | The format of the app image file that contains precompiled code and data for an app. App images can improve app startup time and memory usage by reducing the need for just-in-time (JIT) compilation and garbage collection. |
| dalvik.vm.dex2oat-Xms | 64m | The initial heap size in bytes for dex2oat, a tool that converts Dalvik executable (DEX) files into executable and linkable format (ELF) files containing native code. |
| dalvik.vm.dex2oat-Xmx | 512m | The maximum heap size in bytes for dex2oat. |
| dalvik.vm.dex2oat-max-image-block-size | 524288 | The maximum size in bytes of a single image block in an app image file. Image blocks are contiguous regions of memory that contain code and data for an app. |
| dalvik.vm.dex2oat-minidebuginfo | TRUE | A flag that indicates whether to generate minimal debug information for native code in ELF files. Minimal debug information can reduce file size and disk space usage, but it can also limit debugging capabilities. |
| dalvik.vm.dex2oat-resolve-startup-strings | TRUE | A flag that indicates whether to resolve string literals at compile time for native code in ELF files. Resolving string literals can improve performance by avoiding runtime lookups, but it can also increase file size and memory usage. |
| dalvik.vm.dexopt.secondary | TRUE | A flag that indicates whether to store secondary DEX files in a different directory from primary DEX files. Secondary DEX files are additional DEX files that are loaded by an app at runtime. Storing them separately can improve security by preventing unauthorized modification or execution of code. |
| dalvik.vm.heapgrowthlimit | 256m | The maximum size that the Dalvik heap can grow to before garbage collection is triggered. |
| dalvik.vm.heapmaxfree | 8m | The maximum amount of free memory that can be left in the Dalvik heap after garbage collection. |
| dalvik.vm.heapminfree | 512k | The minimum amount of free memory that must be left in the Dalvik heap after garbage collection. |
| dalvik.vm.heapsize | 512m | The initial size of the Dalvik heap at process start. |
| dalvik.vm.heapstartsize | 8m | The initial size of the Dalvik heap at process start. |
| dalvik.vm.heaptargetutilization | 0.75 | The fraction of the Dalvik heap that should be used after garbage collection. |
| dalvik.vm.image-dex2oat-Xms | 64m | The initial heap size for dex2oat when compiling an app image. |
| dalvik.vm.image-dex2oat-Xmx | 64m | The maximum heap size for dex2oat when compiling an app image. |
| dalvik.vm.isa.arm.features | default | The features supported by the ARM instruction set architecture. |
| dalvik.vm.isa.arm.variant | cortex-a75 | The variant of the ARM instruction set architecture. |
| dalvik.vm.isa.arm64.features | default | The features supported by the ARM64 instruction set architecture. |
| dalvik.vm.isa.arm64.variant | kryo300 | The variant of the ARM64 instruction set architecture. |
| dalvik.vm.minidebuginfo | TRUE | Whether to generate minimal debug information for native libraries. |
| dalvik.vm.usejit | TRUE | Whether to enable just-in-time compilation for Dalvik bytecode. |
| dalvik.vm.usejitprofiles | TRUE | Whether to use profile-guided optimization for just-in-time compilation. |
| debug.atrace.tags.enableflags | 0 | The flags that control which tracing tags are enabled for systrace. |
| debug.egl.hw | 0 | Whether to enable hardware acceleration for OpenGL ES rendering. |
| debug.force_rtl | FALSE | Whether to force right-to-left layout direction for all locales. |
| debug.mdpcomp.logs | 0 | The level of logging for MDP composition. |
| debug.ro.serialno | 6d1bd7bc | The serial number of the device. |
| debug.sf.enable_advanced_sf_phase_offset | 1 | Whether to enable advanced phase offset calculation for SurfaceFlinger. |
| debug.sf.enable_hwc_vds | 1 | Whether to enable virtual display support in Hardware Composer. |
| debug.sf.high2_fps_early_gl_phase_offset_ns | -3000000 | The phase offset in nanoseconds for early GL composition at high frame rate 2 mode. |
| debug.sf.high2_fps_early_phase_offset_ns | -3000000 | The phase offset in nanoseconds for early app composition at high frame rate 2 mode. |
| debug.sf.high2_fps_late_sf_phase_offset_ns | -3000000 | The phase offset in nanoseconds for late SurfaceFlinger composition at high frame rate 2 mode. |
| debug.sf.high_fps_early_gl_phase_offset_ns | -4000000 | The phase offset in nanoseconds for early GL composition at high frame rate mode. |
| debug.sf.high_fps_early_phase_offset_ns | -4000000 | The phase offset in nanoseconds for early app composition at high frame rate mode. |
| debug.sf.high_fps_late_app_phase_offset_ns | 1000000 | The phase offset in nanoseconds for late app composition at high frame rate mode. |
| debug.sf.high_fps_late_sf_phase_offset_ns | -4000000 | The phase offset in nanoseconds for late SurfaceFlinger composition at high frame rate mode. |
| debug.sf.hw | 0 | Whether to enable hardware acceleration for SurfaceFlinger rendering. |
| debug.sf.latch_unsignaled | 0 | Whether to latch buffers that are not signaled by the producer yet. |
| debug.sf.perf_fps_early_gl_phase_offset_ns | -5000000 | The phase offset in nanoseconds for early GL composition at performance frame rate mode. |
| debug.sf.perf_fps_early_phase_offset_ns | -5000000 | The phase offset in nanoseconds for early app composition at performance frame rate mode. |
| debug.sf.perf_fps_late_sf_phase_offset_ns | -5000000 | The phase offset in nanoseconds for late SurfaceFlinger composition at performance frame rate mode. |
| debug.stagefright.ccodec | 1 | Whether to enable CCodec, a component-based codec implementation based on Codec 2.0 API. |
| debug.stagefright.omx_default_rank | 0 | This ID controls the default rank of the OpenMAX IL (OMX) components that are used for multimedia processing. A higher rank means a higher priority for selecting the component. |
| debug.stagefright.omx_default_rank.sw-audio | 1 | This ID controls the default rank of the OMX software audio components. It is similar to the previous ID, but only applies to audio components. |
| dev.bootcomplete | 1 | This ID indicates whether the device has completed booting or not. It is set to 1 when the boot animation finishes and all the services are started. |
| dev.mnt.blk.collect | sda | This ID is used to collect the block devices that are mounted on the device. It is a comma-separated list of device names, such as /dev/block/sda1, /dev/block/sda2, etc. |
| dev.mnt.blk.collect2 | sda | This ID is similar to the previous one, but it also includes the block devices that are not mounted on the device, such as /dev/block/sdb1, /dev/block/sdb2, etc. |
| dev.mnt.blk.data | sda | This ID is the name of the block device that corresponds to the /data partition on the device. It is usually something like /dev/block/sda12 or /dev/block/dm-0. |
| dev.mnt.blk.data.logs.host.clusterlogs | sda | This ID is the name of the block device that corresponds to the /data/logs/host/clusterlogs directory on the device. It is used to store logs related to cluster operations, such as switching between cores or power modes. |
| dev.mnt.blk.data.logs.host.logs | sda | This ID is the name of the block device that corresponds to the /data/logs/host/logs directory on the device. It is used to store logs related to host operations, such as booting, shutdown, or system events. |
| dev.mnt.blk.data.logs.host.spilogs | sda | This ID is the name of the block device that corresponds to the /data/logs/host/spilogs directory on the device. It is used to store logs related to SPI (Serial Peripheral Interface) communications, such as transferring data between devices or sensors. |
| dev.mnt.blk.data.logs.host.tombstones | sda | This ID is the name of the block device that corresponds to the /data/logs/host/tombstones directory on the device. It is used to store logs related to crashes or errors that occur on the device, such as kernel panics or application faults. |
| dev.mnt.blk.data.wormhole | sda | This ID is the name of the block device that corresponds to the /data/wormhole directory on the device. It is used to store data that needs to be preserved across reboots or updates, such as calibration data or user preferences. |
| dev.mnt.blk.metadata | sda | This ID is the name of the block device that corresponds to the /metadata partition on the device. It is used to store metadata related to encryption, authentication, or security features on the device. |
| dev.mnt.blk.mnt | sda | This ID is the name of the block device that corresponds to the /mnt partition on the device. It is used to mount external storage devices, such as SD cards or USB drives. |
| dev.mnt.blk.mnt.vendor.persist | sda | This ID is the name of the block device that corresponds to the /mnt/vendor/persist directory on the device. It is used to store persistent data that is specific to the vendor or manufacturer of the device, such as firmware versions or custom settings. |
| dev.mnt.blk.odm | dm-6 | This ID is the name of the block device that corresponds to the /odm partition on the device. It is used to store data that is related to the original design manufacturer (ODM) of the device, such as hardware configurations or drivers. |
| dev.mnt.blk.product | dm-7 | This ID is the name of the block device that corresponds to the /product partition on the device. It is used to store data that is related to the product name or model of the device, such as branding images or features. |
| dev.mnt.blk.system | dm-6 | This ID is the name of the block device that corresponds to the /system partition on the device. It is used to store data that is related to the operating system or framework of the device, such as system apps or libraries. |
| dev.mnt.blk.vendor | dm-8 | This ID is the name of the block device that corresponds to the /vendor partition on the device. It is used to store data that is related to the vendor or manufacturer of the device, such as vendor apps or services. |
| dev.mnt.blk.vendor.bt_firmware | sde | This ID is the name of the block device that corresponds to the /vendor/bt_firmware directory on the device. It is used to store data that is related to the Bluetooth firmware of the device, such as version information or patches. |
| dev.mnt.blk.vendor.dsp | sde | This ID is the name of the block device that corresponds to the /vendor dsp directory on the device. It is used to store data that is related to the digital signal processor (DSP) of the device, such as audio codecs or algorithms. Here is a possible text that describes the Android device information IDs in a professional tone and a medium length
| dev.mnt.blk.vendor.firmware_mnt | sde | The mount point of the vendor firmware partition. |
| dev.pm.dyn_samplingrate | 1 | The dynamic sampling rate of the power manager. |
| dsp_version | 2208241 | The version of the digital signal processor. |
| dyna_version | 0.00.00 | The version of the dynamic system update. |
| gsm.current.phone-type | 1,2 | The current phone type of the GSM network (GSM, CDMA, SIP, or NONE). |
| gsm.last_drop_time |  | The last time the GSM network connection was dropped. |
| gsm.last_reg_time | 17468 | The last time the GSM network registration was successful. |
| gsm.network.type | LTE,Unknown | The type of the GSM network (EDGE, GPRS, HSPA, etc.). |
| gsm.operator.alpha | CMCC | The name of the GSM network operator. |
| gsm.operator.iso-country | cn, | The ISO country code of the GSM network operator. |
| gsm.operator.isroaming | false,false | Whether the GSM network is roaming or not. |
| gsm.operator.numeric | 4,600,000,000 | The numeric code of the GSM network operator. |
| gsm.radio_state | 1 | The state of the GSM radio (ON, OFF, or UNAVAILABLE). |
| gsm.sim.operator.alpha | CMCC | The name of the SIM card operator. |
| gsm.sim.operator.iso-country | cn | The ISO country code of the SIM card operator. |
| gsm.sim.operator.numeric | 46013 | The numeric code of the SIM card operator. |
| gsm.sim.state | LOADED,ABSENT | The state of the SIM card (ABSENT, PIN_REQUIRED, PUK_REQUIRED, NETWORK_LOCKED, READY, etc.). |
| gsm.version.baseband | MPSS.HI.2.0.1.c6-00411-BITRA_GEN_PACK-1.395755.2.468836.3 | The version of the baseband firmware. |
| gsm.version.ril-impl | Qualcomm RIL 1  | The version of the radio interface layer implementation. |
| hwservicemanager.ready | TRUE | Whether the hardware service manager is ready or not. |
| init.svc.FissionSvcProxyd | running | The status of the Fission service proxy daemon (running or stopped). |
| init.svc.WlanMacAddress | stopped | The status of the WLAN MAC address service (running or stopped). |
| init.svc.accanim | running | The status of the accelerometer animation service (running or stopped). |
| init.svc.acquisitionsrv | running | The status of the acquisition service (running or stopped). |
| init.svc.adbd | running | The status of the Android debug bridge daemon (running or stopped). |
| init.svc.apexd | running | The status of the apex daemon (running or stopped). |
| init.svc.apexd-bootstrap | stopped | The status of the apex bootstrap service (running or stopped). |
| init.svc.apk_logfs | running | The status of the APK log file system service (running or stopped). |
| init.svc.apn1_init | stopped | The status of the APN1 initialization service (running or stopped). |
| init.svc.apn1_server_init | stopped | The status of the APN1 server initialization service (running or stopped). |
| init.svc.apn1stats | stopped | The status of the APN1 statistics service (running or stopped). |
| init.svc.apn3stats | stopped | The status of the APN3 statistics service (running or stopped). |
| init.svc.ashmemd | running | The status of the ashmem daemon (running or stopped). |
| init.svc.audioserver | running | The status of the audio server (running or stopped). |
| init.svc.autoservice | running | The status of the auto service (running or stopped). |
| init.svc.bmmcameraserver | running | The status of the BMM camera server (running or stopped). |
| init.svc.bootanim | stopped | The status of the boot animation service (running or stopped). |
| init.svc.bpfloader | stopped | The status of the BPF loader service (running or stopped). |
| init.svc.cameraserver | running | The status of the camera server (running or stopped). |
| init.svc.carpadinfosrv | running | The status of the car pad info service (running or stopped). |
| init.svc.clear-bcb | stopped | The status of the clear BCB service (running or stopped). |
| init.svc.cloudctrlserv | running | The status of the cloud control service (running or stopped). |
| init.svc.cloudmanager | running | The status of the cloud manager service (running or stopped). |
| init.svc.cnss-daemon | stopped | The status of the CNSS daemon (running or stopped). |
| init.svc.crashdata-sh | stopped | The status of the crash data shell script service (running or stopped). |
| init.svc.crashlogd | running | The status of the crash log daemon (running or stopped). |
| init.svc.cvphalservice | running | The status of the CVP HAL service (running or stopped). |
| init.svc.diagnosticsrv | running | The status of the diagnostic service (running or stopped). |
| init.svc.dpmQmiMgr | running | The status of the DPM QMI manager service (running or stopped). |
| init.svc.dpmd | running | The status of the DPM daemon (running or stopped). |
| init.svc.drm | running | The status of the DRM service (running or stopped). |
| init.svc.feature_enabler_client | running | This ID is used to enable or disable some features on the device, such as Wi-Fi calling or VoLTE. |
| init.svc.fission-poweron-syncprop | stopped | This ID is used to synchronize some properties between the main and secondary processors on devices that support fission technology. |
| init.svc.fission_console | stopped | This ID is used to provide a console interface for debugging fission-related issues on devices that support fission technology. |
| init.svc.gatekeeper-1-0 | running | This ID is used to manage the authentication of users and applications on the device, such as unlocking the screen or verifying app purchases. |
| init.svc.gatekeeperd | running | This ID is used to communicate with the gatekeeper-1-0 service and handle requests from other processes. |
| init.svc.gbacqservice | running | This ID is used to acquire data from the GlobalBoost sensor on devices that support this feature, which enhances the accuracy of location services. |
| init.svc.gnss_service | running | This ID is used to provide access to the Global Navigation Satellite System (GNSS) on the device, which includes GPS, GLONASS, Galileo, and BeiDou. |
| init.svc.gsid | stopped | This ID is used to provide access to the Google Services ID (GSID), which is a unique identifier for each Google account on the device. |
| init.svc.hidl_memory | running | This ID is used to allocate and manage memory for the Hardware Interface Definition Language (HIDL) services on the device, which are used to communicate with hardware components. |
| init.svc.hwservicemanager | running | This ID is used to register and manage the HIDL services on the device and provide a binder interface for clients to access them. |
| init.svc.idmap2d | stopped | This ID is used to create and apply overlay packages on the device, which are used to customize the appearance and behavior of system and app resources. |
| init.svc.incidentd | running | This ID is used to collect and report diagnostic data from the device, such as crash logs, ANR traces, or bug reports. |
| init.svc.installd | running | This ID is used to install, update, and remove applications on the device, as well as manage their data and cache directories. |
| init.svc.iop-hal-2-0 | running | This ID is used to provide access to the Input/Output Prefetcher (IOP) service on the device, which improves the performance and responsiveness of apps by prefetching their data and code before they are launched. |
| init.svc.iorapd | stopped | This ID is used to provide access to the Input/Output Recording and Playback (IORAP) service on the device, which records and replays app launch sequences to optimize their startup time. |
| init.svc.irsc_util | stopped | This ID is used to initialize the modem subsystem on devices that support cellular connectivity, such as setting up network parameters and loading firmware images. |
| init.svc.keystore | running | This ID is used to provide access to the keystore service on the device, which stores and manages cryptographic keys and certificates for encryption, decryption, signing, and verification operations. |
| init.svc.lmkd | running | This ID is used to provide access to the low memory killer daemon (lmkd) on the device, which monitors the memory usage and kills processes that consume too much memory when needed. |
| init.svc.loc_launcher | running | This ID is used to launch and manage location-related services on the device, such as geofencing, geocoding, or activity recognition. |
| init.svc.logd | running | This ID is used to provide access to the log daemon (logd) on the device, which collects and stores various logs from different sources, such as kernel messages, system events, or app outputs. |
| init.svc.logd-auditctl | stopped | This ID is used to control the audit subsystem on devices that support SELinux enforcement, such as enabling or disabling audit logging or setting audit rules. |
| init.svc.logd-reinit | stopped | This ID is used to reinitialize the log daemon (logd) on the device when needed, such as after a system update or a configuration change. |
| init.svc.mdnsd | running | This ID is used to provide access to the multicast DNS (mDNS) daemon (mdnsd) on the device, which enables service discovery and name resolution over local networks using the DNS protocol. |
| init.svc.media | running | This ID is used to provide access to the media service on the device, which handles audio and video playback, recording, encoding, decoding, processing, and streaming operations. |
| init.svc.media.swcodec | running | This ID is used to provide access to the software codec service on the device, which performs audio and video encoding and decoding operations using software implementations when hardware implementations are not available or suitable. |
| init.svc.mediadrm | running | This ID is used to provide access to the media DRM service on
| init.svc.mediaextractor | running | This ID is for the service that extracts metadata from media files. |
| init.svc.mediametrics | running | This ID is for the service that collects and reports media performance metrics. |
| init.svc.mlid | running | This ID is for the service that manages machine learning inference requests. |
| init.svc.mmc_use_info | running | This ID is for the service that monitors and logs the usage of the MultiMediaCard (MMC) storage device. |
| init.svc.mqttserv | running | This ID is for the service that provides MQTT messaging protocol support. |
| init.svc.netd | running | This ID is for the service that handles network configuration and connectivity. |
| init.svc.neuralnetworks_hal_service | running | This ID is for the service that implements the Neural Networks Hardware Abstraction Layer (HAL) interface. |
| init.svc.nqnfcinfo | stopped | This ID is for the service that provides information about the Near Field Communication (NFC) chip on your device. |
| init.svc.perf-hal-2-1 | running | This ID is for the service that implements the Performance HAL interface version 2.1. |
| init.svc.poweropt-service | running | This ID is for the service that optimizes power consumption by controlling CPU frequency and voltage. |
| init.svc.qcom-c_core-sh | stopped | This ID is for the service that runs a shell script to configure Qualcomm's C-core processor. |
| init.svc.qcom-c_main-sh | stopped | This ID is for the service that runs a shell script to configure Qualcomm's C-main processor. |
| init.svc.qcom-post-boot | stopped | This ID is for the service that runs a shell script to perform post-boot operations on Qualcomm devices. |
| init.svc.qcom-sh | stopped | This ID is for the service that runs a shell script to perform general operations on Qualcomm devices. |
| init.svc.qspmhal | running | This ID is for the service that implements the Qualcomm System Power Manager HAL interface. |
| init.svc.qspmsvc | running | This ID is for the service that communicates with the Qualcomm System Power Manager daemon. |
| init.svc.qti-media | stopped | This ID is for the service that provides media-related functionality on Qualcomm devices. |
| init.svc.remove-hid-vr-game-sh | stopped | This ID is for the service that runs a shell script to remove HID VR game controllers from your device. |
| init.svc.servicemanager | running | This ID is for the service that manages communication between Android services and applications. |
| init.svc.soter-1-0 | running | This ID is for the service that implements the Soter HAL interface version 1.0. Soter is a security framework developed by Tencent. |
| init.svc.ssgqmigd | running | This ID is for the service that handles Qualcomm modem interface (QMI) messages from Samsung devices. |
| init.svc.stateservice | running | This ID is for the service that manages device state transitions, such as boot, shutdown, and recovery. |
| init.svc.statsd | running | This ID is for the service that collects and reports system statistics data. |
| init.svc.storaged | running | This ID is for the service that monitors and manages storage devices on your device. |
| init.svc.strategyservice | running | This ID is for the service that implements various strategies to improve system performance and user experience, such as memory management, thermal control, and app launch optimization. |
| init.svc.surfaceflinger | running | This ID is for the service that composes graphical layers from multiple applications into a single buffer that can be displayed by a display controller. |
| init.svc.tecControl | running | This ID is for the service that controls thermal engine cooling on your device. |
| init.svc.thermal-engine | running | This ID is for the service that monitors and controls device temperature by adjusting CPU frequency, GPU frequency, fan speed, etc. |
| init.svc.time_daemon | running | This ID is for the service that synchronizes device time with network time servers or GPS satellites. |
| init.svc.tombstoned | running | This ID is for the service that collects and saves crash reports from native processes on your device. |
| init.svc.ueventd | running | This ID is for the service that listens to kernel uevents and creates device nodes in /dev directory accordingly. |
| init.svc.update_engine | running | This ID is for the service that downloads and applies system updates on your device. |
| init.svc.update_verifier_nonencrypted | stopped | This ID is for the service that verifies system updates on nonencrypted devices before booting into them. |
| init.svc.usbd | stopped | This ID is for the service that handles USB device mode configuration and switching on your device. |
| init.svc.vhds | running | This ID is for the service that provides virtual hard disk support on your device.  |
| init.svc.vndservicemanager | running | This ID is for the service that manages communication between vendor-specific services and applications.  |
| init.svc.vold | running | This ID is for the service that mounts and unmounts storage volumes on your device.  |
| init.svc.wait_for_keymaster | stopped | This ID is for the service that waits until keymaster HAL becomes available before continuing boot process. Keymaster HAL provides hardware-backed cryptographic operations on your device.  |
| init.svc.wfdhdcphalservice | running | This ID is for the service that provides HDCP protection for Wi-Fi Display (WFD) content on your device. HDCP stands for High-bandwidth Digital Content Protection.  |
| init.svc.wfdvndservice | running | This ID is for the service that provides vendor-specific functionality for Wi-Fi Display (WFD) on your device.  |
| init.svc.wificond | running | This ID is for the service that interacts with wpa_supplicant daemon to manage Wi-Fi connections on your device. |
| init.svc.wifidisplayhalservice | running | This ID indicates whether the Wi-Fi display HAL service is running or not. |
| init.svc.zygote | running | This ID indicates whether the zygote process, which is responsible for launching app processes, is running or not. |
| init.svc.zygote_secondary | running | This ID indicates whether the secondary zygote process, which is used for launching app processes with a different ABI, is running or not. |
| keyguard.no_require_sim | TRUE | This ID indicates whether the keyguard (lock screen) requires a SIM card to be unlocked or not. |
| log.tag.APM_AudioPolicyManager | V | This ID indicates the log level for the Audio Policy Manager, which handles audio routing and policy. |
| log.tag.AudioPolicyManagerCustom | D | This ID indicates the log level for the custom Audio Policy Manager, which may be implemented by device manufacturers. |
| log.tag.stats_log | I | This ID indicates the log level for the stats log, which collects and reports various statistics about the device and apps. |
| mcu_boot_version | 21.2.2.2108140.1 | This ID indicates the boot version of the microcontroller unit (MCU), which is a small computer that controls some hardware functions. |
| mcu_version | 21.2.2.2208260.2 | This ID indicates the firmware version of the microcontroller unit (MCU). |
| media.aac_51_output_enabled | TRUE | This ID indicates whether AAC 5.1 channel output is enabled or not for media playback. |
| media.settings.xml | /vendor/etc/media_profiles_vendor.xml | This ID indicates the path to the XML file that contains media settings, such as codec capabilities and profiles. |
| media.stagefright.enable-aac | TRUE | This ID indicates whether AAC codec is enabled or not for media playback and recording. |
| media.stagefright.enable-fma2dp | TRUE | This ID indicates whether FastMixer audio output is enabled or not for A2DP (Bluetooth audio) devices. |
| media.stagefright.enable-http | TRUE | This ID indicates whether HTTP streaming is enabled or not for media playback. |
| media.stagefright.enable-player | TRUE | This ID indicates whether Stagefright player is enabled or not for media playback. |
| media.stagefright.enable-qcp | TRUE | This ID indicates whether QCP codec is enabled or not for media playback and recording. |
| media.stagefright.enable-scan | TRUE | This ID indicates whether progressive download scan is enabled or not for media playback. |
| media.stagefright.thumbnail.prefer_hw_codecs | TRUE | This ID indicates whether hardware codecs are preferred or not for thumbnail extraction. |
| mmp.enable.3g2 | TRUE | This ID indicates whether 3G2 format is enabled or not for media playback and recording. |
| net.bt.name | Android | This ID indicates the Bluetooth name of the device. |
| net.lte.apn1.cid | 0 | This ID indicates the connection identifier (CID) of the first LTE access point name (APN). |
| net.lte.apn1.ifname | rmnet_data2 | This ID indicates the interface name of the first LTE access point name (APN). |
| net.lte.apn1.ip | 11.95.89.236 | This ID indicates the IP address of the first LTE access point name (APN). |
| net.lte.apn1.real_state | connect | This ID indicates the real state of the first LTE access point name (APN), such as connected or disconnected. |
| net.lte.apn1.state | connect | This ID indicates the state of the first LTE access point name (APN), such as enabled or disabled. |
| net.lte.apn3.cid |  | This ID indicates the connection identifier (CID) of the third LTE access point name (APN). |
| net.lte.apn3.ifname |  | This ID indicates the interface name of the third LTE access point name (APN). |
| net.lte.apn3.ip |  | This ID indicates the IP address of the third LTE access point name (APN). |
| net.lte.apn3.real_state | disconnected | This ID indicates the real state of the third LTE access point name (APN), such as connected or disconnected. |
| net.lte.apn3.state | disconnected | This ID indicates the state of the third LTE access point name (APN), such as enabled or disabled. |
| net.qtaguid_enabled | 1 | This ID indicates whether qtaguid module is enabled or not, which tracks network usage per app and user. |
| net.rmnet_data2.dns1 | 120.196.165.7 | This ID indicates the first DNS server address for rmnet_data2 interface, which is used for mobile data connection. |
| net.rmnet_data2.dns2 | 221.179.38.7 | This ID indicates the second DNS server address for rmnet_data2 interface, which is used for mobile data connection. |
| net.rmnet_data3.dns1 |  | This ID indicates the first DNS server address for rmnet_data3 interface, which is used for mobile data connection. |
| net.rmnet_data3.dns2 |  | This ID indicates the second DNS server address for rmnet_data3 interface, which is used for mobile data connection. |
| net.rmnet_data4.dns1 |  | This ID indicates the first DNS server address for rmnet_data4 interface, which is used for mobile data connection. |
| net.rmnet_data4.dns2 |  | This ID indicates the second DNS server address for rmnet_data4 interface, which is used for mobile data connection. |
| net.tcp.2g_init_rwnd | 10 | The initial receive window size for TCP connections over 2G networks. |
| net.tcp.default_init_rwnd | 60 | The default initial receive window size for TCP connections over any network. |
| persist.audio.fluence.speaker | TRUE | Whether to enable fluence noise cancellation for the speaker. |
| persist.audio.fluence.voicecall | TRUE | Whether to enable fluence noise cancellation for voice calls. |
| persist.audio.fluence.voicerec | FALSE | Whether to enable fluence noise cancellation for voice recording. |
| persist.backup.ntpServer | 0.pool.ntp.org | The NTP server to use for backup and restore operations. |
| persist.byd.telephony.networkType | LTE | The preferred network type for BYD devices. |
| persist.camera.privapp.list | org.codeaurora.snapcam | The list of privileged apps that can access the camera service. |
| persist.data.df.agg.dl_pkt | 10 | The number of packets to aggregate for download over cellular networks. |
| persist.data.df.agg.dl_size | 4096 | The maximum size of aggregated packets for download over cellular networks. |
| persist.data.df.dev_name | rmnet_usb0 | The device name to use for data flow debugging. |
| persist.data.df.dl_mode | 5 | The download mode to use for data flow debugging. |
| persist.data.df.iwlan_mux | 9 | Whether to enable multiplexing for IWLAN data connections. |
| persist.data.df.mux_count | 8 | The number of multiplexed channels to use for data connections. |
| persist.data.df.ul_mode | 5 | The upload mode to use for data flow debugging. |
| persist.data.wda.enable | TRUE | Whether to enable wireless data analysis. |
| persist.dbg.volte_avail_ovr | 1 | Whether to override the availability of VoLTE service. |
| persist.debug.coresight.config | stm-events | The coresight configuration to use for debugging. |
| persist.debug.wfd.enable | 1 | Whether to enable Wi-Fi display debugging. |
| persist.fuse_sdcard | TRUE | Whether to use FUSE for mounting the external storage as emulated internal storage. |
| persist.mm.enable.prefetch | TRUE | Whether to enable prefetching for multimedia playback. |
| persist.radio.cause |  | The cause code for radio reset events. |
| persist.radio.iccid | 8.99E+19 | The ICCID of the SIM card inserted in the device. |
| persist.radio.multisim.config | dsds | The multi-SIM configuration of the device. |
| persist.rild.nitz_long_ons_0 |  | The long operator name from NITZ for SIM slot 0. |
| persist.rild.nitz_long_ons_1 |  | The long operator name from NITZ for SIM slot 1. |
| persist.rild.nitz_long_ons_2 |  | The long operator name from NITZ for SIM slot 2. |
| persist.rild.nitz_long_ons_3 |  | The long operator name from NITZ for SIM slot 3. |
| persist.rild.nitz_plmn |  | The PLMN from NITZ for the current network. |
| persist.rild.nitz_short_ons_0 |  | The short operator name from NITZ for SIM slot 0. |
| persist.rild.nitz_short_ons_1 |  | The short operator name from NITZ for SIM slot 1. |
| persist.rild.nitz_short_ons_2 |  | The short operator name from NITZ for SIM slot 2. |
| persist.rild.nitz_short_ons_3 |  | The short operator name from NITZ for SIM slot 3. |
| persist.rmnet.data.enable | TRUE | Whether to enable rmnet data interface for cellular data connections. |
| persist.service.apklogfs.enable | 1 | Whether to enable APK log file system service. |
| persist.service.autoSave.enable | 0 | Whether to enable auto save service for log files and dumps. |
| persist.service.cachelog.enable | 1 | Whether to enable cache log service for log files and dumps. |
| persist.service.crashlog.enable | 1 | Whether to enable crash log service for log files and dumps. |
| persist.service.data_pt.enable | 0 | Whether to enable data partition service for log files and dumps. |
| persist.service.host.name | idilink.byd.com | The host name to use for log file and dump service connections. |
| persist.service.kernelpstore | 1 | Whether to enable kernel pstore service for log files and dumps. |
| persist.service.log.num | 21 | The number of log files and dumps to keep in each category. |
| persist.service.ota.enable | 1 | Whether to enable OTA update service. |
| persist.service.recovery.enable | 0 | This ID indicates whether the device can enter recovery mode automatically when it encounters a system error. |
| persist.service.upload.enable | 0 | This ID indicates whether the device can upload diagnostic data to the cloud server for analysis and troubleshooting. |
| persist.sys.316_req_status | 1 | This ID indicates the status of the request for the 316 certification, which is a safety standard for electric vehicles. |
| persist.sys.AutoType | 0 | This ID indicates the type of automatic transmission that the device supports, such as CVT or DCT. |
| persist.sys.adb.wiress.enable | TRUE | This ID indicates whether the device can enable wireless debugging via adb, which is a command-line tool for Android development. |
| persist.sys.alarmlog | 1 | This ID indicates whether the device can record and store alarm events, such as power on/off, reboot, or crash. |
| persist.sys.autovoice.pkgName | com.byd.autovoice | This ID indicates the package name of the app that provides voice control functionality for the device. |
| persist.sys.boot.reason |  | This ID indicates the reason for the last boot of the device, such as normal, recovery, or bootloader. |
| persist.sys.boot.reason.history | reboot,bydcloud,1683469669;recovery,1683445048;reboot,studyautonomouslypolicy,1683444616 | This ID indicates the history of boot reasons for the device, such as reboot,studyautonomouslypolicy,1683444616
| persist.sys.bt.status | TRUE | This ID indicates the status of Bluetooth on the device, such as on or off. |
| persist.sys.bt_addr | 98:BB:1E:56:2E:50 | This ID indicates the Bluetooth address of the device, which is used for pairing and communication with other Bluetooth devices. |
| persist.sys.byd.autoplay | FALSE | This ID indicates whether the device can automatically play media files when a USB or SD card is inserted. |
| persist.sys.byd.bluetooth_name | BYD | This ID indicates the name of the device that is displayed when it is scanned by other Bluetooth devices. |
| persist.sys.byd.bt_switch | 1 | This ID indicates whether the device can switch between Bluetooth modes, such as hands-free or music. |
| persist.sys.byd.default_name | BYD | This ID indicates the default name of the device that is used when it is not connected to any network or account. |
| persist.sys.byd.ditrainer_state | 1 | This ID indicates the state of the driver instructor mode on the device, which is a feature that allows drivers to receive feedback and guidance from a professional instructor via voice and video calls. |
| persist.sys.byd.hasSDInserted | TRUE | This ID indicates whether the device has an SD card inserted or not. |
| persist.sys.byd.hasUSBInserted | TRUE | This ID indicates whether the device has a USB device inserted or not. |
| persist.sys.byd.hotspot_switch | 0 | This ID indicates whether the device can enable or disable hotspot mode, which allows other devices to connect to its internet connection via Wi-Fi. |
| persist.sys.byd.isMediaExist | FALSE | This ID indicates whether the device has any media files stored on its internal memory or external storage devices. |
| persist.sys.byd.mediaMode | 1 | This ID indicates the mode of media playback on the device, such as local or online. |
| persist.sys.byd.mediaWidgetMode | 1 | This ID indicates the mode of media widget on the device, which is a small interface that allows users to control media playback without opening the app. |
| persist.sys.byd.otaupdate | FALSE | This ID indicates whether the device can receive over-the-air updates for its system software and apps. |
| persist.sys.byd.wifi_switch | 1 | This ID indicates whether the device can enable or disable Wi-Fi mode, which allows it to connect to wireless networks and access internet services. |
| persist.sys.camera_support_mark | 419 | This ID indicates whether the device supports camera watermarking, which is a feature that adds a logo or text to photos and videos taken by the camera app. |
| persist.sys.cloud.last_vin | LC0C76C42N1046530 | This ID indicates the last vehicle identification number (VIN) that was registered by the device on the cloud server, which is used for identifying and tracking vehicles. |
| persist.sys.cloud.token_flag | 1 | This ID indicates whether the device has a valid token for accessing cloud services, such as data backup and restore, remote control, and location sharing. |
| persist.sys.cloud.unlock_type | 0 | This ID indicates the type of unlock method that is used by the device to access cloud services, such as password, fingerprint, or face recognition. |
| persist.sys.cloud.user_id |  | This ID is used to identify the user account associated with the device in the cloud service. |
| persist.sys.cloud_412_data | 2023-05-07-15:30:49:-->412_data_163-> | This ID is used to store some data related to the cloud service on the device. |
| persist.sys.cloud_fid_uploaded | 1 | This ID indicates whether the Firebase installation ID (FID) has been uploaded to the cloud service. |
| persist.sys.cloud_last_branch | CANFD | This ID indicates the last branch of the cloud service that the device was connected to. |
| persist.sys.cloudlog | 2 | This ID enables or disables the logging of cloud service events on the device. |
| persist.sys.collect_config_uuid |  | This ID is used to collect configuration data from the device for analytics purposes. |
| persist.sys.csim.msisdn | 14803594044 | This ID is used to store the mobile subscriber integrated services digital network number (MSISDN) of the device's SIM card. |
| persist.sys.dalvik.vm.lib.2 | libart.so | This ID specifies the name of the library that provides the Java virtual machine (JVM) implementation for the device. |
| persist.sys.device_provisioned | 1 | This ID indicates whether the device has been provisioned or not. |
| persist.sys.disable_bg_dexopt | TRUE | This ID disables or enables the background optimization of Dalvik executable (DEX) files on the device. |
| persist.sys.displayinset.top | 0 | This ID specifies the size of the display inset at the top of the screen, which is usually reserved for a notch or a camera cutout. |
| persist.sys.dms.config.vin | LC0C76C42N1046530 | This ID is used to store the vehicle identification number (VIN) of the device's car mode configuration. |
| persist.sys.dyna_rework_uploaded | 0 | This ID indicates whether the dynamic rework data has been uploaded to the cloud service or not. |
| persist.sys.ecosport | eco | This ID enables or disables the eco-sport mode on the device, which affects the performance and battery consumption. |
| persist.sys.enable_rescue | TRUE | This ID enables or disables the rescue mode on the device, which allows users to recover their data in case of a system failure. |
| persist.sys.energytype | 0 | This ID indicates the type of energy source that powers the device, such as battery, solar, or wired. |
| persist.sys.factory.data2 | 040J516EFM92402783 | This ID stores some factory data on the device for testing purposes. |
| persist.sys.force_sw_gles | 1 | This ID forces the device to use software rendering for OpenGL ES graphics instead of hardware acceleration. |
| persist.sys.gps.lpp | 0 | This ID enables or disables the LTE positioning protocol (LPP) for GPS on the device, which improves location accuracy and reduces battery consumption. |
| persist.sys.gps_m_rst | 1 | This ID resets the GPS module on the device when it is set to 1 and then reverts back to 0. |
| persist.sys.gpsinfo | 139.7721217_35.70341793_1_2_0_-2.325592_.0_360.0_0 | This ID stores some GPS information on the device for debugging purposes. |
| persist.sys.imagerotation | 1 | This ID specifies the rotation angle of the image captured by the device's camera, in degrees clockwise from 0 to 270. |
| persist.sys.isMute | FALSE | This ID indicates whether the device is muted or not. |
| persist.sys.isolated_storage | FALSE | This ID enables or disables isolated storage on the device, which restricts apps from accessing each other's data and files. |
| persist.sys.magicwindow.enable | 1 | This ID enables or disables magic window mode on the device, which allows users to run multiple apps in resizable windows on a single screen. |
| persist.sys.mdlog.enable | 0 | This ID enables or disables mobile data logging on the device, which collects network traffic data for analysis and troubleshooting purposes. |
| persist.sys.ntp_server_ip | 203.107.6.88 | The IP address of the network time protocol server used by the device. |
| persist.sys.onlyTrace.enable | 0 | A flag that indicates whether only trace logging is enabled on the device. |
| persist.sys.ota.diagnostic | FALSE | A flag that indicates whether over-the-air diagnostic mode is enabled on the device. |
| persist.sys.privacy_switch | 294 | A flag that indicates whether privacy switch mode is enabled on the device. |
| persist.sys.protocol.record | CANFD | A flag that indicates whether protocol record mode is enabled on the device. |
| persist.sys.quickboot_ongoing |  | A flag that indicates whether quickboot mode is ongoing on the device. |
| persist.sys.rdevice_tcp | 12 | A flag that indicates whether remote device TCP mode is enabled on the device. |
| persist.sys.rebootreason | bydcloud | The reason for the last reboot of the device. |
| persist.sys.record_499_upload | 22 | A flag that indicates whether record 499 upload mode is enabled on the device. |
| persist.sys.record_610_upload | 0 | A flag that indicates whether record 610 upload mode is enabled on the device. |
| persist.sys.record_door_lf | 0 | A flag that indicates whether record door left front mode is enabled on the device. |
| persist.sys.record_lock_action | 2 | A flag that indicates whether record lock action mode is enabled on the device. |
| persist.sys.remotethemechange | 2 | A flag that indicates whether remote theme change mode is enabled on the device. |
| persist.sys.rescue_try_reboot | FALSE | A flag that indicates whether rescue try reboot mode is enabled on the device. |
| persist.sys.restore.status | TRUE | The status of the last restore operation on the device. |
| persist.sys.sapn_switch | 0 | A flag that indicates whether SAPN switch mode is enabled on the device. |
| persist.sys.sf.color_mode | 9 | The color mode of the surface flinger on the device. |
| persist.sys.sf.color_saturation | 1 | The color saturation of the surface flinger on the device. |
| persist.sys.sf.native_mode | 0 | The native mode of the surface flinger on the device. |
| persist.sys.system_info | 1 | The system information of the device, such as model, version, etc. |
| persist.sys.timeoff | 0 | The time offset of the device from UTC in milliseconds. |
| persist.sys.timesynced | TRUE | A flag that indicates whether the time of the device has been synced with a server. |
| persist.sys.timezone | Asia/Shanghai | The time zone of the device, such as GMT+8, etc. |
| persist.sys.usb.config | adb | The USB configuration of the device, such as MTP, PTP, etc. |
| persist.sys.usb.ffbm-02.func | mtp | The USB function of the device in FFBM-02 mode, such as diag, adb, etc. |
| persist.sys.user_authentication_status | 1 | The user authentication status of the device, such as locked, unlocked, etc. |
| persist.sys.v_type | 2 | The vehicle type of the device, such as sedan, SUV, etc. |
| persist.sys.vehicle_40d_code | 0 | The vehicle 40D code of the device, such as 1234ABCD, etc. |
| persist.sys.version | 21.1.2.2208230.1 | The version of the system software on the device, such as 10.0.0, etc. |
| persist.sys.vin_valid | 1 | A flag that indicates whether the vehicle identification number (VIN) of the device is valid or not. |
| persist.sys.watermarked | 0 | A flag that indicates whether watermarked mode is enabled on the device. |
| persist.sys.wfd.virtual | 0 | A flag that indicates whether wireless display virtual mode is enabled on the device. |
| persist.sys.wlan.status | TRUE | The status of WLAN on the device, such as connected, disconnected, etc. |
| persist.sys.wlan_ap.status | FALSE | The status of WLAN access point on the device, such as enabled, disabled, etc. |
| persist.timed.enable | TRUE | A flag that indicates whether timed service is enabled on the device. |
| persist.vendor.camera.cam_apa | 0 | A flag that indicates whether camera APA mode is enabled on the vendor partition of the device. |
| persist.vendor.dpm.tcm | 2 | The trusted computing module (TCM) configuration of DPM on the vendor partition of the device. |
| pm.dexopt.ab-ota | speed-profile | The dex optimization mode for AB-OTA updates on the package manager of the device.  |
| pm.dexopt.bg-dexopt | speed-profile | The dex optimization mode for background dexopt on package manager
| pm.dexopt.boot | verify | This ID indicates the optimization mode for booting apps. |
| pm.dexopt.first-boot | quicken | This ID indicates the optimization mode for first-boot apps. |
| pm.dexopt.inactive | verify | This ID indicates the optimization mode for inactive apps. |
| pm.dexopt.install | speed-profile | This ID indicates the optimization mode for newly installed apps. |
| pm.dexopt.shared | speed | This ID indicates the optimization mode for shared libraries. |
| qcom.hw.aac.encoder | TRUE | This ID indicates whether the device supports hardware AAC encoding. |
| qemu.hw.mainkeys | 0 | This ID indicates whether the device has hardware keys or a software navigation bar. |
| qualcomm.qti.logkit.lite | 1 | This ID indicates whether the device uses a lite version of Qualcomm logkit. |
| ril.apn3.control |  | This ID controls the third APN selection for data connection. |
| ril.call_state | 0 | This ID reports the current call state of the device. |
| ril.csim.iccid | 8.99E+19 | This ID contains the ICCID of the CSIM card inserted in the device. |
| ril.csim.msisdn |  | This ID contains the MSISDN of the CSIM card inserted in the device. |
| ril.data_service_state | 1 | This ID reports the current data service state of the device. |
| ril.ecclist | 112,120,119,08,118,999,*911,000,911,122,110,#911 | This ID contains the emergency call codes for the device. |
| ril.ecclist1 | 112,120,119,08,118,999,*911,000,911,122,110,#911 | This ID contains the emergency call codes for the second SIM slot of the device. |
| ril.imei | 8.68E+14 | This ID contains the IMEI number of the device. |
| ril.imsi | 4.60E+14 | This ID contains the IMSI number of the SIM card inserted in the device. |
| ril.subscription.types | NV,RUIM | This ID reports the subscription types of the SIM cards inserted in the device. |
| rild.libpath | /vendor/lib64/libril-qc-hal-qmi.so | This ID specifies the path to the radio interface layer library for the device. |
| ro.actionable_compatible_property.enabled | TRUE | This ID indicates whether the device supports actionable compatible property feature. |
| ro.adb.secure | 1 | This ID indicates whether ADB connections are secure or not. |
| ro.af.client_heap_size_kbyte | 7168 | This ID specifies the heap size for audio effects in kilobytes. |
| ro.allow.mock.location | 0 | This ID indicates whether mock location is allowed or not on the device. |
| ro.baseband | msm | This ID reports the baseband version of the device. |
| ro.bluetooth.library_name | libbluetooth_qti.so | This ID specifies the name of the Bluetooth library for the device. |
| ro.board.platform | lito | This ID reports the platform name of the device. |
| ro.boot.baseband | msm | The baseband version of the device, which is related to the radio firmware. |
| ro.boot.boot_devices | soc/1d84000.ufshc | The list of devices that are used for booting the system. |
| ro.boot.bootdevice | 1d84000.ufshc | The name of the device that contains the boot partition. |
| ro.boot.bootreason | reboot,bydcloud | The reason for the last boot, such as reboot, recovery, or power key. |
| ro.boot.console | ttyMSM0 | The name of the console device that is used for logging kernel messages. |
| ro.boot.cpuserialno | 0xFAE3F1BE | The serial number of the CPU chip. |
| ro.boot.dir | 0x00 | The directory where the boot image is located. |
| ro.boot.display_status | 0x06FE | The status of the display during boot, such as on or off. |
| ro.boot.dtb_idx | 0 | The index of the device tree blob that is used for booting. |
| ro.boot.dtbo_idx | 8 | The index of the device tree overlay that is applied during booting. |
| ro.boot.dynamic_partitions | TRUE | A flag that indicates whether the device supports dynamic partitions, which allow resizing partitions without repartitioning the storage device. |
| ro.boot.efuse | 0x02 | The value of the efuse register, which is used for storing device-specific information such as encryption keys. |
| ro.boot.flash.locked | 0 | A flag that indicates whether the bootloader is locked or unlocked. |
| ro.boot.hardware | qcom | The name of the hardware platform that the device is based on. |
| ro.boot.hw_id | 0x00 | The hardware ID of the device, which is a unique identifier for each device model. |
| ro.boot.keymaster | 1 | The version of the keymaster HAL, which provides hardware-backed security services such as key generation and attestation. |
| ro.boot.memcg | 1 | A flag that indicates whether memory cgroups are enabled, which allow controlling memory usage of processes in a hierarchical way. |
| ro.boot.panel_id | 23 | The ID of the display panel that is attached to the device. |
| ro.boot.pwrsrc | 0x01 | The power source that is used for booting, such as battery or AC adapter. |
| ro.boot.recoverymode | 0 | A flag that indicates whether the device is in recovery mode, which allows performing system maintenance operations such as factory reset or system update. |
| ro.boot.selinux | permissive | The mode of SELinux enforcement, which is a security mechanism that enforces mandatory access control policies on processes and files. |
| ro.boot.serialno | 6d1bd7bc | The serial number of the device, which is a unique identifier for each device instance. |
| ro.boot.slot_suffix | _b | The suffix of the boot slot that is used for booting, such as _a or _b, which is related to the A/B system update feature that allows updating one slot while running from another slot. |
| ro.boot.spi_sel | 0x01 | The selection of the SPI flash chip that is used for booting. |
| ro.boot.ufs_size | 128GB | The size of the UFS storage device that is used for booting. |
| ro.boot.usbcontroller | a600000.dwc3 | The name of the USB controller that is used for booting. |
| ro.boot.vbmeta.avb_version | 1 | The version of Android Verified Boot (AVB), which is a security feature that verifies the integrity and authenticity of the boot image and other partitions before loading them. |
| ro.boot.vbmeta.device_state | unlocked | The device state with respect to AVB, such as locked or unlocked. |
| ro.boot.vbmeta.digest | 37887ef49584f841fd3b5217be5c4b87de2a8054f18cb5c182e26d7716e8f2ce | The digest (hash) of the vbmeta image, which contains metadata and signatures for verifying other partitions. |
| ro.boot.vbmeta.hash_alg | sha256 | The hash algorithm that is used for computing and verifying the digest of the vbmeta image. |
| ro.boot.vbmeta.invalidate_on_error | yes | A flag that indicates whether to invalidate (erase) vbmeta if verification fails, which prevents further boot attempts until a valid vbmeta image is flashed. |
| ro.boot.vbmeta.size | 5952 | The size of the vbmeta image in bytes. |
| ro.boot.verifiedbootstate | orange | The state of verified boot, which can be green (verification succeeded), yellow (verification failed but boot allowed), orange (verification disabled), or red (verification failed and boot not allowed).  |
| ro.boot.veritymode | enforcing | The mode of dm-verity, which is a security feature that verifies the integrity and authenticity of system and vendor partitions at runtime. It can be enforcing (verification enabled and enforced), logging (verification enabled but not enforced), or disabled (verification disabled).  |
| ro.boot.wificountrycode | CN | The country code that is used for Wi-Fi regulatory compliance.  |
| ro.bootimage.build.date | Tue Aug 23 1:20:54 CST 2022 | The build date of the boot image in human-readable format.  |
| ro.bootimage.build.date.utc | 1661188854 | The build date of the boot image in Unix time format (seconds since epoch).  |
| ro.bootimage.build.fingerprint | qti/lito/lito:10/QKQ1.210218.001/build08230120:user/release-keys | The build fingerprint of the boot image, which uniquely identifies its version and variant.  |
| ro.bootloader | unknown | The version of the bootloader, which is a program that loads and executes the kernel during booting.  |
| ro.bootmode | unknown | The current boot mode, such as normal, recovery, or bootloader (fastboot).  |
| ro.build.ab_update | TRUE | A flag that indicates whether the device supports A/B system update feature or not.  |
| ro.build.characteristics | nosdcard | A comma-separated list of characteristics or features of this build or product.  |
| ro.build.date | Tue Aug 23 1:20:54 CST 2022 | The build date in human-readable format.  |
| ro.build.date.utc | 1661188854 | The build date in Unix time format.  |
| ro.build.description | DiLink4.0-user 10 QKQ1.210218.001 eng.build.20220823.012054 release-keys  | A description string composed from other build properties.  |
| ro.build.display.id | QKQ1.210218.001 release-keys | A string meant to be displayed to users indicating this build's identity.  |
| ro.build.factory.user | FALSE | A string indicating who built this product. |
| ro.build.fingerprint | BYD-AUTO/DiLink4.0/DiLink4.0:10/QKQ1.210218.001/eng.build.20220823.012054:user/release-keys | A string that uniquely identifies this build. |
| ro.build.flavor | qssi-user | A string describing what flavor was built from this product's configuration. |
| ro.build.host | dpc | A string indicating what host was used to produce this build. |
| ro.build.id | QKQ1.210218.001 | Either a changelist number or a label like "M4-rc20". |
| ro.build.keys | release-keys | A string indicating what keys were used to sign this build. |
| ro.build.product | DiLink4.0 | A string identifying this product's name. |
| ro.build.system.fission_single_os | 0 | A flag indicating whether this product supports fission single OS feature or not [10]. |
| ro.build.system_root_image | FALSE | A flag indicating whether this product has system_root_image feature enabled or not [11]. |
| ro.build.tags | release-keys | Comma-separated tags describing this build's properties. |
| ro.build.type | user | A string identifying what type this build's variant is. |
| ro.build.type.1for2 | TRUE | The type of build, such as user or userdebug. |
| ro.build.user | build | The user name associated with the build. |
| ro.build.version.all_codenames | REL | The current development codenames, or REL if this is a release build. |
| ro.build.version.base_os |  | The base OS build the product is based on. |
| ro.build.version.codename | REL | The current development codename, or REL if this is a release build. |
| ro.build.version.incremental | eng.build.20220823.012054 | The internal value used by the underlying source control to represent this build. |
| ro.build.version.min_supported_target_sdk | 23 | The minimum supported SDK version for apps on this device. |
| ro.build.version.preview_sdk | 0 | The developer preview SDK version of this build. |
| ro.build.version.preview_sdk_fingerprint | REL | The fingerprint of the developer preview SDK version of this build. |
| ro.build.version.release | 10 | The version number of this build. |
| ro.build.version.sdk | 29 | The SDK version of this build. |
| ro.build.version.security_patch | 2020/8/5 | The date of the most recent security patch update applied to this build. |
| ro.byd.telephony.cap.5G | TRUE | Whether the device supports 5G network capability or not. |
| ro.carrier | unknown | The name of the wireless carrier that the device is connected to. |
| ro.clu.size | 123 | The number of CPU cores available on the device. |
| ro.com.android.dataroaming | TRUE | Whether data roaming is enabled or not. |
| ro.config.alarm_alert | Alarm_Classic.ogg | The default alarm sound file name. |
| ro.config.notification_sound | pixiedust.ogg | The default notification sound file name. |
| ro.config.ringtone | Ring_Synth_04.ogg | The default ringtone file name. |
| ro.control_privapp_permissions | enforce | Whether to enforce privileged permissions for preinstalled apps or not. |
| ro.crypto.allow_encrypt_override | TRUE | Whether to allow encryption to be overridden by user input or not. |
| ro.crypto.state | unencrypted | The state of encryption on the device, such as encrypted or unencrypted. |
| ro.crypto.volume.filenames_mode | aes-256-cts | The mode of encryption for filenames on the device, such as aes-256-heh or aes-256-cts. |
| ro.dalvik.vm.native.bridge | 0 | The native bridge library to load for apps that run on a different instruction set than the device's primary instruction set. |
| ro.debuggable | 0 | Whether the device can be debugged over USB or not. |
| ro.device_owner | FALSE | Whether the device has a device owner app installed or not. |
| ro.feature.symbol | amap:other | Whether the device supports symbol input method or not. |
| ro.fission.mode | cell | Whether the device runs in fission mode or not, which means splitting system processes into multiple isolated processes for security reasons. |
| ro.frp.pst | /dev/block/bootdevice/by-name/frp | The partition GUID where factory reset protection is implemented. |
| ro.hardware | qcom | The name of the hardware platform that the device is based on. |
| ro.hardware.egl | adreno | The name of the EGL (Embedded Graphics Library) implementation that the device uses for rendering graphics. |
| ro.hardware.info | V31.E32.00.23 | A string that describes the hardware features of the device, such as CPU model and frequency, RAM size, screen resolution, etc. |
| ro.hardware.keystore_desede | TRUE | Whether the device supports triple DES encryption for keystore operations or not. |
| ro.hardware.vulkan | adreno | Whether the device supports Vulkan graphics API or not. |
| ro.hwui.drop_shadow_cache_size | 6 | The size in megabytes of the cache for drop shadows rendered by the hardware UI engine. |
| ro.hwui.gradient_cache_size | 1 | The size in megabytes of the cache for gradients rendered by the hardware UI engine. |
| ro.hwui.layer_cache_size | 48 | The size in megabytes of the cache for layers rendered by the hardware UI engine. |
| ro.hwui.path_cache_size | 32 | The size in megabytes of the cache for paths rendered by the hardware UI engine. |
| ro.hwui.r_buffer_cache_size | 8 | The size in megabytes of the cache for render buffers used by the hardware UI engine. |
| ro.hwui.text_large_cache_height | 1024 | The height in pixels of the cache for large text rendered by the hardware UI engine.  |
| ro.hwui.text_large_cache_width | 2048 | The width of the large text cache in pixels. |
| ro.hwui.text_small_cache_height | 1024 | The height of the small text cache in pixels. |
| ro.hwui.text_small_cache_width | 1024 | The width of the small text cache in pixels. |
| ro.hwui.texture_cache_flushrate | 0.4 | The fraction of the texture cache that is flushed each frame. |
| ro.hwui.texture_cache_size | 72 | The size of the texture cache in bytes. |
| ro.hwui.use_vulkan |  | Whether to use Vulkan graphics API or not. |
| ro.iorapd.enable | FALSE | Whether to enable iorapd, a daemon that optimizes app startup time. |
| ro.kernel.qemu.gles | 0 | The OpenGL ES emulation mode for the emulator. |
| ro.logd.size.stats | 64K | The maximum size of the log buffer for stats events in bytes. |
| ro.minui.pixel_format | RGBX_8888 | The pixel format used by minui, a minimal graphics library. |
| ro.netflix.bsp_rev | Q7250-19133-1 | The Netflix BSP revision number. |
| ro.nfc.port | I2C | The port number for NFC communication. |
| ro.odm.build.date | Tue Aug 23 1:20:54 CST 2022 | The build date of the original device manufacturer (ODM) software. |
| ro.odm.build.date.utc | 1661188854 | The build date of the ODM software in UTC time. |
| ro.odm.build.fingerprint | qti/lito/lito:10/QKQ1.210218.001/build08230120:user/release-keys | A string that uniquely identifies the ODM software build. |
| ro.oem_unlock_supported | 1 | Whether the device supports OEM unlocking or not. |
| ro.opengles.version | 196610 | The highest supported version of OpenGL ES on the device. |
| ro.osd.hw_ver | V00.04 | The hardware version of the on-screen display (OSD) chip. |
| ro.osd.sw_ver | 25.1.1.2203230.1-25.1.1.2207130.2 | The software version of the OSD chip. |
| ro.panel.size | 101 | The size of the display panel in inches. |
| ro.postinstall.fstab.prefix | /system | The prefix for the fstab file used during post-installation. |
| ro.product.board | SM6350 | The name of the device board platform. |
| ro.product.brand | BYD-AUTO | The brand name of the device. |
| ro.product.build.date | Tue Aug 23 1:20:54 CST 2022 | The build date of the product software. |
| ro.product.build.date.utc | 1661188854 | The build date of the product software in UTC time. |
| ro.product.build.fingerprint | qti/qssi/qssi:10/QKQ1.210218.001/build08230120:user/release-keys | A string that uniquely identifies the product software build. |
| ro.product.build.id | QKQ1.210218.001 | A string that identifies the product software build. |
| ro.product.build.tags | release-keys | A comma-separated list of tags describing the product software build. |
| ro.product.build.type | user | The type of product software build, such as user or userdebug. |
| ro.product.build.version.incremental | eng.build.20220823.012054 | The incremental version number of the product software build. |
| ro.product.build.version.release | 10 | The release version number of the product software build. |
| ro.product.build.version.sdk | 29 | The SDK version number of the product software build. |
| ro.product.cpu.abi | arm64-v8a | The primary application binary interface (ABI) supported by the device CPU. |
| ro.product.cpu.abilist | arm64-v8a,armeabi-v7a,armeabi | A comma-separated list of ABIs supported by the device CPU. |
| ro.product.cpu.abilist32 | armeabi-v7a,armeabi | A comma-separated list of 32-bit ABIs supported by the device CPU. |
| ro.product.cpu.abilist64 | arm64-v8a | A comma-separated list of 64-bit ABIs supported by the device CPU. |
| ro.product.device | DiLink4.0 | The name of the device model or product code name.  |
| ro.product.first_api_level | 29 | The API level corresponding to the first release for which this device was shipped with this system image installed.  |
| ro.product.locale | zh-CN | The default locale for the device.  |
| ro.product.manufacturer | BYD AUTO | The name of the manufacturer of the device.  |
| ro.product.model | DiLink4.0 For BYD AUTO | The end-user-visible name for the end product.  |
| ro.product.name | DiLink4.0 | The name of the overall product.  |
| ro.product.odm.brand | BYD-AUTO | The brand name associated with this ODM partition image.  |
| ro.product.odm.device | DiLink4.0 | A value used to differentiate between devices based on ODM partition images.  |
| ro.product.odm.manufacturer | BYD AUTO | A value used to differentiate between manufacturers based on ODM partition images.  |
| ro.product.odm.model | DiLink4.0 For BYD AUTO | A value used to differentiate between models based on ODM partition images.  |
| ro.product.odm.name | DiLink4.0 | A value used to differentiate between products based on ODM partition images.  |
| ro.product.product.brand | BYD-AUTO | A value used to differentiate between brands based on product partition images.  |
| ro.product.product.device | DiLink4.0 | A value used to differentiate between devices based on product partition images.  |
| ro.product.product.manufacturer | BYD AUTO | The name of the manufacturer of the product. |
| ro.product.product.model | DiLink4.0 For BYD AUTO | The name of the model of the product. |
| ro.product.product.name | DiLink4.0 | The name of the product. |
| ro.product.property_source_order | odm,vendor,product,product_services,system | The order in which system properties are read from different sources. |
| ro.product.system.brand | BYD-AUTO | The brand name of the system image. |
| ro.product.system.device | DiLink4.0 | The name of the device on which the system image runs. |
| ro.product.system.manufacturer | BYD AUTO | The name of the manufacturer of the system image. |
| ro.product.system.model | DiLink4.0 For BYD AUTO | The name of the model of the system image. |
| ro.product.system.name | DiLink4.0 | The name of the system image. |
| ro.product.vendor.brand | BYD-AUTO | The brand name of the vendor image. |
| ro.product.vendor.device | DiLink4.0 | The name of the device on which the vendor image runs. |
| ro.product.vendor.manufacturer | BYD AUTO | The name of the manufacturer of the vendor image. |
| ro.product.vendor.model | DiLink4.0 For BYD AUTO | The name of the model of the vendor image. |
| ro.product.vendor.name | DiLink4.0 | The name of the vendor image. |
| ro.property_service.version | 2 | The version number of the property service. |
| ro.qc.sdk.audio.fluencetype | none | The type of audio fluence technology used by the device. |
| ro.qc.sdk.audio.ssr | FALSE | The status of surround sound recording feature on the device. |
| ro.revision | 0 | The revision number of the hardware on which the system runs. |
| ro.secure | 1 | A flag indicating whether the device is running in secure mode or not. |
| ro.serialno | 6d1bd7bc | The serial number of the device. |
| ro.sf.lcd_density | 160 | The logical density of the display in dots per inch (dpi). |
| ro.surface_flinger.has_HDR_display | TRUE | A flag indicating whether the device has a high dynamic range (HDR) display or not. |
| ro.surface_flinger.has_wide_color_display | TRUE | A flag indicating whether the device has a wide color gamut (WCG) display or not. |
| ro.surface_flinger.protected_contents | TRUE | A list of protected content types that can be displayed by the surface flinger service. |
| ro.surface_flinger.use_color_management | TRUE | A flag indicating whether the surface flinger service uses color management or not. |
| ro.surface_flinger.wcg_composition_dataspace | 143261696 | The default data space used by the surface flinger service for WCG composition. |
| ro.system.build.date | Tue Aug 23 1:20:54 CST 2022 | The date when the system image was built. |
| ro.system.build.date.utc | 1661188854 | The date when the system image was built in UTC time format. |
| ro.system.build.fingerprint | qti/qssi/qssi:10/QKQ1.210218.001/build08230120:user/release-keys | A string that uniquely identifies the build of the system image. |
| ro.system.build.id | QKQ1.210218.001 | The identifier for the build of the system image. |
| ro.system.build.tags | release-keys | A list of tags describing the build of the system image. |
| ro.system.build.type | user | The type of build of the system image, such as user, userdebug, or eng. |
| ro.system.build.version.incremental | eng.build.20220823.012054 | The incremental version number of the build of the system image. |
| ro.system.build.version.release | 10 | The release version number of the build of the system image, such as 10 or 11. |
| ro.system.build.version.sdk | 29 | The SDK version number of the build of the system image, such as 29 or 30. |
| ro.telephony.call_ring.multiple | FALSE | This ID indicates whether the device supports multiple call ringing tones. The value can be 0 (disabled) or 1 (enabled). |
| ro.telephony.default_network | 32,32 | This ID specifies the default network mode for the device. The value can be one of the constants defined in TelephonyManager.java, such as 0 (unknown), 1 (GSM only), 2 (WCDMA only), etc. |
| ro.treble.enabled | TRUE | This ID indicates whether the device supports Project Treble, which is a modularization of the Android OS framework. The value can be true or false. |
| ro.vehicle.type | Di4.0_3.5UI | This ID indicates whether the device is a vehicle device. The value can be true or false. |
| ro.vehicle.type.value | 17 | This ID specifies the type of vehicle device, such as car, truck, bus, etc. |
| ro.vendor.build.date | Tue Aug 23 1:20:54 CST 2022 | This ID shows the build date of the vendor image on the device. The value is a string in the format YYYY-MM-DD. |
| ro.vendor.build.date.utc | 1661188854 | This ID shows the build date of the vendor image on the device in UTC time. The value is a long integer representing milliseconds since epoch. |
| ro.vendor.build.fingerprint | qti/lito/lito:10/QKQ1.210218.001/build08230120:user/release-keys | This ID shows the fingerprint of the vendor image on the device. The value is a string that uniquely identifies the build, such as "google/coral/coral
| ro.vendor.build.security_patch | 2020/8/5 | This ID shows the security patch level of the vendor image on the device. The value is a string in the format YYYY-MM-DD, such as "2020-10-05". |
| ro.vendor.qti.va_aosp.support | 1 | This ID indicates whether the device supports voice assistant features from Qualcomm Technologies, Inc. The value can be true or false. |
| ro.vendor.qti.va_odm.support | 1 | This ID indicates whether the device supports voice assistant features from an original design manufacturer (ODM). The value can be true or false. |
| ro.vndk.version | 29 | This ID shows the version of the vendor native development kit (VNDK) on the device. The value can be a string such as "29" or "current". |
| ro.wifi.channels |  | This ID specifies the Wi-Fi channels that are allowed on the device. The value can be a comma-separated list of integers, such as "1,6,11". |
| ro.xdja.disp.mode |  | This ID indicates whether the device supports display modes from Xdja Corporation. The value can be true or false. |
| ro.zygote | zygote64_32 | This ID specifies which zygote process to use for app launching. The zygote is a system process that forks to create new processes for apps. The value can be one of "zygote32", "zygote64", or "zygote32_64". |
| security.perf_harden | 1 | This ID indicates whether performance hardening is enabled for security-sensitive operations. Performance hardening reduces the risk of side-channel attacks by introducing random delays or noise. The value can be 0 (disabled) or 1 (enabled). |
| selinux.restorecon_recursive | /data/misc_ce/0 | This ID specifies which directories to restore SELinux file contexts recursively on boot. SELinux is a security enhancement for Linux that enforces access control policies. The value can be a colon-separated list of paths, such as "/data/misc_ce /data/misc_de". |
| service.adb.tcp.port | 5555 | This ID specifies which TCP port to use for adb (Android Debug Bridge) connections over Wi-Fi. Adb is a command-line tool that lets developers communicate with and control an Android device. The value can be an integer between 1024 and 65535, or -1 to disable adb over Wi-Fi. |
| service.bootanim.exit | 1 | This ID indicates whether to exit the boot animation when it finishes playing. The boot animation is a graphical sequence that shows when the device boots up. The value can be 0 (do not exit) or 1 (exit). |
| service.sf.present_timestamp | 1 | This ID indicates whether to enable SurfaceFlinger present time stamps for debugging purposes. SurfaceFlinger is a system service that handles compositing and displaying graphical layers from apps and the system UI. The value can be true or false. |
| sys.acc_status | ON | This ID shows the status of accessory detection on the device. Accessory detection is a feature that lets the device recognize and communicate with external accessories, such as headphones, speakers, docks, etc. The value can be one of "0" (no accessory), "1" (analog accessory), "2" (digital accessory), or "3" (unsupported accessory). |
| sys.accanim.status | 0 | This ID shows the status of accessory animation on the device. Accessory animation is a feature that plays a graphical sequence when an accessory is connected or disconnected. The value can be one of "0" (no animation), "1" (animation start), or "2" (animation end). |
| sys.apn3.control |  | This ID controls whether to enable APN3 mode on the device. APN3 mode is a feature that allows multiple APNs (Access Point Names) to be active simultaneously for different network services, such as internet, MMS, IMS, etc. The value can be true or false. |
| sys.autohal.loglevel | 2 | This ID specifies which log level to use for autohal (Automotive Hardware Abstraction Layer). Autohal is a framework that provides standard interfaces for automotive hardware components, such as sensors, lights, HVAC, etc. The value can be one of "none", "error", "warning", "info", "debug", or "verbose". |
| sys.boot.reason | reboot,bydcloud | This ID shows the reason for the last boot of the device. The value can be one of "normal", "recovery", "reboot", "shutdown", "charger", etc. |
| sys.boot.reason.last | reboot,bydcloud | This ID indicates the last boot reason of the device, such as normal, recovery, or bootloader. |
| sys.boot_completed | 1 | This ID indicates whether the boot process has completed successfully or not. |
| sys.bootanim.rotation | 0 | This ID indicates the rotation angle of the boot animation on the device screen. |
| sys.byd.KaraokeBoot | TRUE | This ID indicates whether the device has booted into karaoke mode or not. |
| sys.byd.apprequest_orientation | other | This ID indicates the requested orientation of the app on the device screen. |
| sys.byd.boot_business | activated | This ID indicates the business type of the boot process, such as normal, factory, or upgrade. |
| sys.byd.boot_business_sub | null | This ID indicates the sub-type of the boot business type, such as normal, recovery, or fastboot. |
| sys.byd.isMediaForeground | FALSE | This ID indicates whether the media app is in the foreground or not. |
| sys.byd.isSDExist | TRUE | This ID indicates whether the SD card is inserted or not. |
| sys.byd.isVideoFullScreen | FALSE | This ID indicates whether the video app is in full screen mode or not. |
| sys.byd.mSdcardUuid | 103A-6EEA | This ID indicates the UUID of the SD card on the device. |
| sys.byd.orientation | 0 | This ID indicates the current orientation of the device screen, such as portrait or landscape. |
| sys.byd.pano_start | 0 | This ID indicates whether the panorama camera mode is started or not. |
| sys.byd.power_on_upgrade_app |  | This ID indicates whether the device has powered on to upgrade an app or not. |
| sys.byd.sdexist | 1 | This ID indicates whether the SD card exists or not. |
| sys.bydlogtool.life | 1 | This ID indicates the life cycle of the log tool app on the device. |
| sys.car.protocol | CANFD | This ID indicates the protocol type of the car mode on the device, such as CANBUS or I2C. |
| sys.cloud.201_send_status | 1 | This ID indicates the status of sending data to the cloud server, such as success or failure. |
| sys.cloud.unlock_index | 13 | This ID indicates the index of unlocking data from the cloud server. |
| sys.cloud_532_reply | 2023/5/8 08:58:12:-->532_cmd:5-> reply reult:fail !  | This ID indicates whether the cloud server has replied to a request or not. |
| sys.connect.adb.wiress | 1 | This ID indicates whether the device is connected to a wireless ADB (Android Debug Bridge) or not. |
| sys.dms.config.vin | LC0C76C42N1046530 | This ID indicates the vehicle identification number (VIN) of the device in car mode. |
| sys.dns.vehicleCode | ff | This ID indicates the vehicle code of the device in car mode. |
| sys.ext.amp.type | 0 | The type of audio amplifier used by the device. |
| sys.fm.hasfmchip | 1 | Whether the device has a FM radio chip or not. |
| sys.gb.connect_type | 0 | The type of connection used by the device to communicate with Google services. |
| sys.hal.activemic.config | 1 | The configuration of the active microphone used by the device. |
| sys.hal.iflytek.config | 1 | The configuration of the iFlytek speech recognition engine used by the device. |
| sys.hicar.callstate | 0 | The state of the phone call when the device is connected to a HiCar system. |
| sys.hicar.connected | 0 | Whether the device is connected to a HiCar system or not. |
| sys.hicar.enabled | TRUE | Whether the device supports HiCar mode or not. |
| sys.isInEcall | 0 | Whether the device is in an emergency call or not. |
| sys.isolated_storage_snapshot | FALSE | Whether the device is using isolated storage snapshot or not. |
| sys.load_hid_vir_game | 0 | Whether the device loads a virtual game controller when connected to a HID device or not. |
| sys.log.dumpsys | meminfo_system | Whether the device dumps system information for debugging purposes or not. |
| sys.log.ps.top | top_done | The top processes running on the device according to their CPU usage. |
| sys.logbootcomplete | 1 | Whether the device has completed booting or not. |
| sys.modify.type | 0 | The type of modification applied to the device, such as root or custom ROM. |
| sys.module.config | 0 | The configuration of the modules loaded by the device, such as camera or fingerprint. |
| sys.motion_switch | 0 | Whether the device supports motion detection or not. |
| sys.mtp.device_type | 2 | The type of MTP device that the device emulates when connected to a computer via USB. |
| sys.oem_unlock_allowed | 0 | Whether the device allows OEM unlocking or not. |
| sys.qca1530 | detect | Whether the device has a Qualcomm Atheros 1530 chipset or not. |
| sys.quickboot.enable | 0 | Whether the device supports quick boot mode or not. |
| sys.rescue_boot_count | 1 | The number of times that the device has booted into rescue mode due to system errors. |
| sys.restart_modem | 0 | Whether the device restarts its modem or not. |
| sys.retaildemo.enabled | 0 | Whether the device is in retail demo mode or not. |
| sys.sapn_action |  | The action performed by the device when it receives a SAPN message from a carrier. |
| sys.screen.on | 1 | Whether the screen of the device is on or off. |
| sys.shutdown.requested |  | Whether the device has received a shutdown request or not. |
| sys.signalstrength | 36 | The signal strength of the cellular network that the device is connected to. |
| sys.sysctl.extra_free_kbytes | 10800 | The amount of extra free memory in kilobytes that the system reserves for emergency situations. |
| sys.sysctl.tcp_def_init_rwnd | 60 | The default initial receive window size for TCP connections in segments. |
| sys.system_server.start_count | 1 | The number of times that the system server has started on the device. |
| sys.system_server.start_elapsed | 9717 | The elapsed time since the system server started on the device in milliseconds. |
| sys.system_server.start_uptime | 9717 | The uptime of the system server on the device in milliseconds. |
| sys.tcp_client_ver | di4_ivi_cluster_mp1228.202208050_canfd | The version of the TCP client used by the device. |
| sys.tcp_connect_status | 1 | The status of the TCP connection established by the device, such as success or failure. |
| sys.tcp_reg_errcode | 0 | The error code returned by the TCP registration process on the device, such as 0 for success or -1 for failure. |
| sys.tcp_step | 6 | The step of the TCP registration process on the device, such as 1 for start or 4 for end. |
| sys.timesynced | TRUE | Whether the time on the device is synchronized with a network time server or not. |
| sys.usb.config | adb | The current USB configuration of the device, such as mtp,adb or none.  |
| sys.usb.configfs | 1 | This ID indicates the configuration of the USB port on your device, such as whether it is used for charging, data transfer, or audio output. |
| sys.usb.controller | a600000.dwc3 | This ID specifies the name of the USB controller driver that is loaded on your device. |
| sys.usb.ffs.ready | 1 | This ID shows whether the FunctionFS (FFS) file system is ready for use by the USB gadget driver on your device. |
| sys.usb.state | adb | This ID reflects the current state of the USB connection on your device, such as connected, disconnected, or configured. |
| sys.use_memfd | FALSE | This ID determines whether your device uses memfd_create() system call to create anonymous shared memory regions. |
| sys.user.0.ce_available | TRUE | This ID indicates whether the credential encrypted (CE) storage is available for user 0 on your device. |
| sys.vendor.shutdown.waittime | 500 | This ID sets the maximum time in milliseconds that your device waits for vendor services to shut down gracefully before forcing a reboot or shutdown. |
| sys.vin | LC0C76C42N1046530 | This ID represents the vehicle identification number (VIN) of your device if it is a car head unit. |
| sys.vin_valid_record_time | 12 | This ID stores the timestamp of the last valid VIN record on your device if it is a car head unit. |
| sys.wifitracing.started | 1 | This ID shows whether Wi-Fi tracing is started on your device for debugging purposes. |
| sys.wlan.addr | 98:bb:1e:56:2e:51 | This ID displays the MAC address of the Wi-Fi interface on your device. |
| sys.wlan.driver_load | reset | This ID indicates whether the Wi-Fi driver is loaded on your device. |
| sys.wlan_mac_address.enable | 0 | This ID enables or disables the use of a random MAC address for Wi-Fi connections on your device. |
| telephony.lteOnCdmaDevice | 0 | This ID specifies whether your device supports LTE on CDMA networks. |
| tunnel.audio.encode | TRUE | This ID enables or disables audio tunneling to a digital signal processor (DSP) on your device for power efficiency. |
| use.voice.path.for.pcm.voip | TRUE | This ID controls whether the voice path or the multimedia path is used for PCM VoIP audio on your device. |
| vendor.gralloc.disable_ubwc | 0 | This ID disables the use of Universal Bandwidth Compression (UBWC) for graphics buffer allocation on your device. |
| vendor.opengles.version | 196610 | This ID reports the version of OpenGL ES that is supported by your device. |
| vold.decrypt |  | This ID indicates the status of decryption of data partition on your device, such as trigger_restart_min_framework, trigger_restart_framework, or default_password. |
| vold.has_adoptable | 1 | This ID shows whether your device supports adoptable storage, which allows you to format and use a microSD card as internal storage. |
| vold.has_quota | 0 | This ID determines whether your device supports disk quota for apps in shared storage. |
| vold.has_reserved | 0 | This ID reveals whether your device has reserved space in data partition for system updates and factory reset protection (FRP). |
| vold.post_fs_data_done | 1 | This ID signals whether post-fs-data actions have been completed by vold (volume daemon) on your device after file system mounting. |
| wifi.interface | wlan0 | This ID specifies the name of the Wi-Fi interface on your device, such as wlan0 or p2p0. |
| xdja.license.state | success | This ID represents the license state of Xdja security software on your device, such as valid or invalid. |
| xdja.sys.usb.state | adb | This ID reflects the USB state of Xdja security software on your device, such as enable or disable. |
| xdja.sys.usb.state_changed | 1 | This ID notifies whether the USB state of Xdja security software on your device has changed. |