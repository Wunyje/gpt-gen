# Investigation on ISP
## 1 What is ISP?
ISP stands for Image Signal Processor, which is a unit used to process the output signal of the front-end image sensor . ISP can perform various functions such as noise reduction, HDR correction, face recognition and automatic scene recognition .

### 1.1 What's the difference between ISP 2.X and ISP 3.X?
ISP 2.X and ISP 3.X are two generations of ISP products from Arm, a leading semiconductor company. ISP 2.X includes Mali-C52 and Mali-C32, while ISP 3.X includes Mali-C55. The main difference between them is that ISP 3.X offers improved image quality features, works under a wide range of different lighting and weather conditions, and is designed to enable maximum performance and capability in area and power constrained applications. ISP 3.X also supports multi-camera capability for up to 8 separate inputs, image resolutions up to 8K and a maximum image size up to 48 megapixels (MP).

### 1.2 What's the relationship of ISP and gstreamer?
Gstreamer is a framework for creating streaming media applications. It provides a set of plugins that can be used to capture, process, encode and display video and audio data. ISP and gstreamer can work together to implement various vision systems for IoT and embedded markets. For example, gstreamer can use the v4l2src plugin to capture raw data from an image sensor, then use the v4l2_isp plugin to send the data to an ISP for processing, and finally use the v4l2sink plugin to display the processed data on a screen.




## 2 What is MIPI D-PHY?
MIPI D/CPHY RX is a physical layer interface that enables high-performance, low-power communication between cameras, displays, and application processors in mobile, automotive, and IoT applications. It supports two modes of operation: MIPI D-PHY and MIPI C-PHY.

MIPI D-PHY is a clock-forwarded synchronous link that provides high noise immunity and high jitter tolerance. It operates at up to 6.5 Gb/s per lane and can support up to 4 lanes in parallel. MIPI D-PHY is compliant with the MIPI D-PHY specification, v2.1.

## 2.1 What is MIPI C-PHY?

MIPI C-PHY is a three-phase encoding scheme that uses three wires per trio to transmit data symbols. It operates at up to 6.5 Gs/s per trio and can support up to 3 trios in parallel. MIPI C-PHY is compliant with the MIPI C-PHY specification, v2.0.

## 2.2 What is the difference between MIPI C-PHY and MIPI D-PHY?

MIPI C-PHY and MIPI D-PHY have different encoding schemes, signaling levels, and bandwidth capabilities. MIPI C-PHY uses three-level signaling (0, 1, or Z) and can transmit 2.28 bits per symbol, while MIPI D-PHY uses two-level signaling (0 or 1) and can transmit 1 bit per symbol. MIPI C-PHY can achieve higher bandwidth efficiency than MIPI D-PHY with the same number of wires, but it also requires more complex encoding and decoding logic.

## 2.3 What is the relationship of 2Lanex4 and MIPI DPHY?

2Lanex4 is a configuration of MIPI DPHY that uses two lanes with four sub-lanes each. Each sub-lane operates at one-fourth of the lane frequency, resulting in a lower power consumption and a higher robustness against skew and crosstalk. 2Lanex4 can achieve the same bandwidth as 4Lanex2 with half the number of wires.

### 2.3.1 What is the difference between 2Lanex4 and 4Lanex2?

2Lanex4 and 4Lanex2 are two configurations of MIPI DPHY that have the same aggregate throughput but different number of wires and sub-lane frequencies. 2Lanex4 uses two lanes with four sub-lanes each, while 4Lanex2 uses four lanes with two sub-lanes each. The sub-lane frequency of 2Lanex4 is one-fourth of that of 4Lanex2, which reduces power consumption and improves robustness. However, 2Lanex4 also requires more complex lane aggregation and de-aggregation logic than 4Lanex2.