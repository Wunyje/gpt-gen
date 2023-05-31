## 1 Is this function of Rockchip product developed on Linux?
Yes, this function of Rockchip product is developed on Linux. According to the datasheet of RK3328, it supports Linux 4.4 operating system with various drivers and libraries for audio and video codec.

## 2 What is the main developing key point of this?
The main developing key point of this function is to achieve high performance and low power consumption for audio and video processing. Rockchip product uses a dual-core Cortex-A72 and quad-core Cortex-A53 CPU architecture with separate NEON coprocessor to handle complex multimedia tasks. It also supports multi-format video decoders and encoders, such as H.264/H.265/VP9 up to 4Kx2K@60fps, and high-quality JPEG codec.

## 3 How to implement audio and video codec function on Rockchip's product?
To implement audio and video codec function on Rockchip's product, one needs to use the provided drivers and libraries that are compatible with the Linux operating system. For example, one can use the VPU (video processing unit) driver to access the hardware video codec engine, and use the Gstreamer framework to build multimedia pipelines. Similarly, one can use the ALSA (advanced Linux sound architecture) driver to access the hardware audio codec engine, and use the PulseAudio framework to manage audio streams.