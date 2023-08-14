## RK3588 `DTS` code of `csi2` snippets
A `dts` file is a device tree source file that describes the hardware configuration of a system. A `dtsi` file is a device tree include file that contains common definitions that can be reused by multiple `dts` files. The device tree compiler (`dtc`) can process these files and generate a binary device tree blob (`dtb`) that can be used by the kernel or bootloader.

On this page, there are six `dts` or `dtsi` files related to the Rockchip RK3588 system-on-chip (SoC). The RK3588 is a high-performance 8-core SoC that supports 8K video decoding, 4K video encoding, and multiple display interfaces. Here is a brief summary of each file:

- `rockchip_dts\rockchip\rk3588-evb4-lp4-v10.dts`: This file describes the specific model and compatibility of the RK3588 evaluation board version 10 with LPDDR4 memory. It includes two other files: `rk3588-evb4-lp4.dtsi` and `rk3588-android.dtsi`.
```dts
/dts-v1/;

#include "rk3588-evb4-lp4.dtsi"
#include "rk3588-android.dtsi"

/ {
	model = "Rockchip RK3588 EVB4 LP4 V10 Board";
	compatible = "rockchip,rk3588-evb4-lp4-v10", "rockchip,rk3588";
};
```

- `rockchip_dts\rockchip\rk3588-evb4-lp4.dtsi`: This file describes the common configuration of the RK3588 evaluation board with LPDDR4 memory. It includes three other files: `rk3588.dtsi`, `rk3588-evb.dtsi`, and `rk3588-rk806-single.dtsi`.
```dts
#include "dt-bindings/usb/pd.h"
#include "rk3588.dtsi"
#include "rk3588-evb.dtsi"
#include "rk3588-rk806-single.dtsi"
```

- `rockchip_dts\rockchip\rk3588.dtsi`: This file describes the core configuration of the RK3588 SoC, such as the interrupt controller, the address and size cells, the aliases, and the CSI2 DPHYs. It includes two other files: `rk3588s.dtsi` and `rk3588-vccio3-pinctrl.dtsi`.
```dts
#include <dt-bindings/phy/phy-snps-pcie3.h>
#include "rk3588s.dtsi"
#include "rk3588-vccio3-pinctrl.dtsi"

/ {
	aliases {
		csi2dphy3 = &csi2_dphy3;
		csi2dphy4 = &csi2_dphy4;
		csi2dphy5 = &csi2_dphy5;
		dp0 = &dp0;
		dp1 = &dp1;
		edp0 = &edp0;
		edp1 = &edp1;
		ethernet0 = &gmac0;
		hdptx0 = &hdptxphy0;
		hdptx1 = &hdptxphy1;
		hdptxhdmi0 = &hdptxphy_hdmi0;
		hdptxhdmi1 = &hdptxphy_hdmi1;
		hdmi0 = &hdmi0;
		hdmi1 = &hdmi1;
		rkcif_mipi_lvds4= &rkcif_mipi_lvds4;
		rkcif_mipi_lvds5= &rkcif_mipi_lvds5;
		usbdp0 = &usbdp_phy0;
		usbdp1 = &usbdp_phy1;
	};

	/* dphy1 full mode */
	csi2_dphy3: csi2-dphy3 {
		compatible = "rockchip,rk3568-csi2-dphy";
		rockchip,hw = <&csi2_dphy1_hw>;
		status = "disabled";
	};

	/* dphy1 split mode 01 */
	csi2_dphy4: csi2-dphy4 {
		compatible = "rockchip,rk3568-csi2-dphy";
		rockchip,hw = <&csi2_dphy1_hw>;
		status = "disabled";
	};

	/* dphy1 split mode 23 */
	csi2_dphy5: csi2-dphy5 {
		compatible = "rockchip,rk3568-csi2-dphy";
		rockchip,hw = <&csi2_dphy1_hw>;
		status = "disabled";
	};
}
	mipi4_csi2: mipi4-csi2@fdd50000 {
		compatible = "rockchip,rk3588-mipi-csi2";
		reg = <0x0 0xfdd50000 0x0 0x10000>;
		reg-names = "csihost_regs";
		interrupts = <GIC_SPI 151 IRQ_TYPE_LEVEL_HIGH>,
			     <GIC_SPI 152 IRQ_TYPE_LEVEL_HIGH>;
		interrupt-names = "csi-intr1", "csi-intr2";
		clocks = <&cru PCLK_CSI_HOST_4>;
		clock-names = "pclk_csi2host";
		resets = <&cru SRST_P_CSI_HOST_4>, <&cru SRST_CSIHOST4_VICAP>;
		reset-names = "srst_csihost_p", "srst_csihost_vicap";
		status = "disabled";
	};

	mipi5_csi2: mipi5-csi2@fdd60000 {
		compatible = "rockchip,rk3588-mipi-csi2";
		reg = <0x0 0xfdd60000 0x0 0x10000>;
		reg-names = "csihost_regs";
		interrupts = <GIC_SPI 153 IRQ_TYPE_LEVEL_HIGH>,
			     <GIC_SPI 154 IRQ_TYPE_LEVEL_HIGH>;
		interrupt-names = "csi-intr1", "csi-intr2";
		clocks = <&cru PCLK_CSI_HOST_5>;
		clock-names = "pclk_csi2host";
		resets = <&cru SRST_P_CSI_HOST_5>, <&cru SRST_CSIHOST5_VICAP>;
		reset-names = "srst_csihost_p", "srst_csihost_vicap";
		status = "disabled";
	};
	csi2_dphy1_hw: csi2-dphy1-hw@fedc8000 {
		compatible = "rockchip,rk3588-csi2-dphy-hw";
		reg = <0x0 0xfedc8000 0x0 0x8000>;
		clocks = <&cru PCLK_CSIPHY1>;
		clock-names = "pclk";
		resets = <&cru SRST_CSIPHY1>, <&cru SRST_P_CSIPHY1>;
		reset-names = "srst_csiphy1", "srst_p_csiphy1";
		rockchip,grf = <&mipidphy1_grf>;
		rockchip,sys_grf = <&sys_grf>;
		status = "disabled";
	};
```
- `rockchip_dts\rockchip\rk3588s.dtsi`: This file describes the sub-nodes of the RK3588 SoC, such as the CSI2 DCPHYs, the MIPI CSI2s, and the RKISP1s. It also defines some properties for the power domains, clocks, resets, and GRFs.
```dts
#include <dt-bindings/clock/rk3588-cru.h>
#include <dt-bindings/interrupt-controller/arm-gic.h>
#include <dt-bindings/interrupt-controller/irq.h>
#include <dt-bindings/phy/phy.h>
#include <dt-bindings/power/rk3588-power.h>
#include <dt-bindings/soc/rockchip,boot-mode.h>
#include <dt-bindings/soc/rockchip-system-status.h>
#include <dt-bindings/suspend/rockchip-rk3588.h>
#include <dt-bindings/thermal/thermal.h>

/ {
	compatible = "rockchip,rk3588";

	interrupt-parent = <&gic>;
	#address-cells = <2>;
	#size-cells = <2>;

	aliases {
        csi2dcphy0 = &csi2_dcphy0;
        csi2dcphy1 = &csi2_dcphy1;
        csi2dphy0 = &csi2_dphy0;
        csi2dphy1 = &csi2_dphy1;
        csi2dphy2 = &csi2_dphy2;
        }
    csi2_dcphy0: csi2-dcphy0 {
		compatible = "rockchip,rk3588-csi2-dcphy";
		phys = <&mipi_dcphy0>;
		phy-names = "dcphy";
		status = "disabled";
	};

	csi2_dcphy1: csi2-dcphy1 {
		compatible = "rockchip,rk3588-csi2-dcphy";
		phys = <&mipi_dcphy1>;
		phy-names = "dcphy";
		status = "disabled";
	};

	/* dphy0 full mode */
	csi2_dphy0: csi2-dphy0 {
		compatible = "rockchip,rk3568-csi2-dphy";
		rockchip,hw = <&csi2_dphy0_hw>;
		status = "disabled";
	};

	/* dphy0 split mode 01 */
	csi2_dphy1: csi2-dphy1 {
		compatible = "rockchip,rk3568-csi2-dphy";
		rockchip,hw = <&csi2_dphy0_hw>;
		status = "disabled";
	};

	/* dphy0 split mode 23 */
	csi2_dphy2: csi2-dphy2 {
		compatible = "rockchip,rk3568-csi2-dphy";
		rockchip,hw = <&csi2_dphy0_hw>;
		status = "disabled";
	};

	mipi0_csi2: mipi0-csi2@fdd10000 {
		compatible = "rockchip,rk3588-mipi-csi2";
		reg = <0x0 0xfdd10000 0x0 0x10000>;
		reg-names = "csihost_regs";
		interrupts = <GIC_SPI 143 IRQ_TYPE_LEVEL_HIGH>,
			     <GIC_SPI 144 IRQ_TYPE_LEVEL_HIGH>;
		interrupt-names = "csi-intr1", "csi-intr2";
		clocks = <&cru PCLK_CSI_HOST_0>, <&cru ICLK_CSIHOST0>;
		clock-names = "pclk_csi2host", "iclk_csi2host";
		resets = <&cru SRST_P_CSI_HOST_0>, <&cru SRST_CSIHOST0_VICAP>;
		reset-names = "srst_csihost_p", "srst_csihost_vicap";
		status = "disabled";
	};

	mipi1_csi2: mipi1-csi2@fdd20000 {
		compatible = "rockchip,rk3588-mipi-csi2";
		reg = <0x0 0xfdd20000 0x0 0x10000>;
		reg-names = "csihost_regs";
		interrupts = <GIC_SPI 145 IRQ_TYPE_LEVEL_HIGH>,
			     <GIC_SPI 146 IRQ_TYPE_LEVEL_HIGH>;
		interrupt-names = "csi-intr1", "csi-intr2";
		clocks = <&cru PCLK_CSI_HOST_1>, <&cru ICLK_CSIHOST1>;
		clock-names = "pclk_csi2host", "iclk_csi2host";
		resets = <&cru SRST_P_CSI_HOST_1>, <&cru SRST_CSIHOST1_VICAP>;
		reset-names = "srst_csihost_p", "srst_csihost_vicap";
		status = "disabled";
	};

	mipi2_csi2: mipi2-csi2@fdd30000 {
		compatible = "rockchip,rk3588-mipi-csi2";
		reg = <0x0 0xfdd30000 0x0 0x10000>;
		reg-names = "csihost_regs";
		interrupts = <GIC_SPI 147 IRQ_TYPE_LEVEL_HIGH>,
			     <GIC_SPI 148 IRQ_TYPE_LEVEL_HIGH>;
		interrupt-names = "csi-intr1", "csi-intr2";
		clocks = <&cru PCLK_CSI_HOST_2>;
		clock-names = "pclk_csi2host";
		resets = <&cru SRST_P_CSI_HOST_2>, <&cru SRST_CSIHOST2_VICAP>;
		reset-names = "srst_csihost_p", "srst_csihost_vicap";
		status = "disabled";
	};

	mipi3_csi2: mipi3-csi2@fdd40000 {
		compatible = "rockchip,rk3588-mipi-csi2";
		reg = <0x0 0xfdd40000 0x0 0x10000>;
		reg-names = "csihost_regs";
		interrupts = <GIC_SPI 149 IRQ_TYPE_LEVEL_HIGH>,
			     <GIC_SPI 150 IRQ_TYPE_LEVEL_HIGH>;
		interrupt-names = "csi-intr1", "csi-intr2";
		clocks = <&cru PCLK_CSI_HOST_3>;
		clock-names = "pclk_csi2host";
		resets = <&cru SRST_P_CSI_HOST_3>, <&cru SRST_CSIHOST3_VICAP>;
		reset-names = "srst_csihost_p", "srst_csihost_vicap";
		status = "disabled";
	};

	csi2_dphy0_hw: csi2-dphy0-hw@fedc0000 {
		compatible = "rockchip,rk3588-csi2-dphy-hw";
		reg = <0x0 0xfedc0000 0x0 0x8000>;
		clocks = <&cru PCLK_CSIPHY0>;
		clock-names = "pclk";
		resets = <&cru SRST_CSIPHY0>, <&cru SRST_P_CSIPHY0>;
		reset-names = "srst_csiphy0", "srst_p_csiphy0";
		rockchip,grf = <&mipidphy0_grf>;
		rockchip,sys_grf = <&sys_grf>;
		status = "disabled";
	};
```

- `rockchip_dts\rockchip\rk3588-evb.dtsi`: This file describes some common definitions for the RK3588 evaluation board, such as the GPIOs, PWMs, pinctrls, input devices, display interfaces, and sensors.
```dts
#include <dt-bindings/gpio/gpio.h>
#include <dt-bindings/pwm/pwm.h>
#include <dt-bindings/pinctrl/rockchip.h>
#include <dt-bindings/input/rk-input.h>
#include <dt-bindings/display/drm_mipi_dsi.h>
#include <dt-bindings/display/rockchip_vop.h>
#include <dt-bindings/sensor-dev.h>
```

- `rockchip_dts\rockchip\rk3588-rk806-single.dtsi`: This file describes some common definitions for the RK806 power management IC (PMIC) that is used on the RK3588 evaluation board.
```dts
#include <dt-bindings/gpio/gpio.h>
#include <dt-bindings/pinctrl/rockchip.h>
```

- `rockchip_dts\rockchip\rp-camera-dphy1-ov13855.dtsi`: This file describes the configuration of a camera module that uses the OV13855 sensor and the DW9763 VCM driver on the CSI2 DPHY1 interface. It defines some properties for the I2C bus, power domain, pinctrl, GRF, GPIOs, clocks, resets, lens focus, ports, and endpoints.
```dts
&i2c3 {
	status = "okay";
	pinctrl-names = "default";
	pinctrl-0 = <&i2c3m0_xfer>;

	dw9763_3: dw9763_3@c {
                compatible = "dongwoon,dw9763";
                status = "okay";
                reg = <0x0c>;
                rockchip,vcm-max-current = <120>;   
                rockchip,vcm-start-current = <20>;   
                rockchip,vcm-rated-current = <90>;  
                rockchip,vcm-step-mode = <3>;     
                rockchip,vcm-t-src = <0x20>;
                rockchip,vcm-t-div = <1>;
                rockchip,camera-module-index = <0>;    
                rockchip,camera-module-facing = "front";  
        };
  
	ov13855_3: ov13855_3@36 {
		compatible = "ovti,ov13855";
		status = "okay";
		reg = <0x36>;
		clocks = <&cru CLK_MIPI_CAMARAOUT_M4>;
		clock-names = "xvclk";
		power-domains = <&power RK3588_PD_VI>;
		pinctrl-names = "default";
		pinctrl-0 = <&mipim0_camera4_clk>;
		rockchip,grf = <&sys_grf>;
		pwdn-gpios = <&gpio1 RK_PB2 GPIO_ACTIVE_HIGH>;
		rockchip,camera-module-index = <0>;
		rockchip,camera-module-facing = "front";
		rockchip,camera-module-name = "CMK-OT2016-FV1";
		rockchip,camera-module-lens-name = "default";
		lens-focus = <&dw9763_3>;
		port {
			ov13855_out3: endpoint {
				remote-endpoint = <&mipi_in_ucam3>;
				data-lanes = <1 2 3 4>;
			};
		};
	};
};

&csi2_dphy1_hw {
	status = "okay";
};

&csi2_dphy3 {
	status = "okay";
	ports {
		#address-cells = <1>;
		#size-cells = <0>;
		port@0 {
			reg = <0>;
			#address-cells = <1>;
			#size-cells = <0>;
			mipi_in_ucam3: endpoint@1 {
				reg = <1>;
				remote-endpoint = <&ov13855_out3>;
				data-lanes = <1 2 3 4>;
			};
		};
		port@1 {
			reg = <1>;
			#address-cells = <1>;
			#size-cells = <0>;
			csidphy1_out: endpoint@0 {
				reg = <0>;
				remote-endpoint = <&mipi4_csi2_input>;
			};
		};
	};
};

&mipi4_csi2 {
	status = "okay";
	ports {
		#address-cells = <1>;
		#size-cells = <0>;
		port@0 {
			reg = <0>;
			#address-cells = <1>;
			#size-cells = <0>;
			mipi4_csi2_input: endpoint@1 {
				reg = <1>;
				remote-endpoint = <&csidphy1_out>;
			};
		};
		port@1 {
			reg = <1>;
			#address-cells = <1>;
			#size-cells = <0>;
			mipi4_csi2_output: endpoint@0 {
				reg = <0>;
				remote-endpoint = <&cif_mipi_in4>;
			};
		};
	};
};


&rkcif_mipi_lvds4 {
	status = "okay";
	port {
		cif_mipi_in4: endpoint {
			remote-endpoint = <&mipi4_csi2_output>;
		};
	};
};

&rkcif_mipi_lvds4_sditf {
	status = "okay";
	port {
		mipi4_lvds_sditf: endpoint {
			remote-endpoint = <&isp1_vir0>;
		};
	};
};

&rkisp1 {
	status = "okay";
};

&isp1_mmu {
	status = "okay";
};

&rkisp1_vir0 {
	status = "okay";
	port {
		#address-cells = <1>;
		#size-cells = <0>;

		isp1_vir0: endpoint@0 {
			reg = <0>;
			remote-endpoint = <&mipi4_lvds_sditf>;
		};
	};
};
```

## New Bing's Answer on "relate the part of `csi2` within them and give the introduction about different `csi2` related componets and their relations"

CSI2 stands for Camera Serial Interface 2, which is a standard interface for connecting cameras to processors or display devices. It uses a high-speed serial bus called MIPI D-PHY to transmit image data and control signals. The RK3588 SoC supports up to six CSI2 interfaces, each with four data lanes and one clock lane. The CSI2 interfaces can be configured to work in different modes, such as full mode, split mode, or dual mode, depending on the number of data lanes and the resolution of the camera sensor.

The files on this page contain some definitions and configurations for the CSI2 interfaces and their related components on the RK3588 evaluation board. Here are some of the main components and their relations:

- `csi2_dphy0_hw` and `csi2_dphy1_hw`: These are the hardware nodes that describe the physical layer (PHY) of the CSI2 interfaces. They define some properties such as the register address, clock, reset, GRF, and sys_grf. They also include other files that contain some pinctrl settings for the VCCIO3 domain.
- `csi2_dphy0`, `csi2_dphy1`, `csi2_dphy2`, `csi2_dphy3`, `csi2_dphy4`, and `csi2_dphy5`: These are the logical nodes that describe the device layer (DL) of the CSI2 interfaces. They specify which hardware node they are using (`rockchip,hw`) and their status (`status`). They also have ports that connect to other endpoints, such as the CSI2 host or the camera sensor.
- `csi2dcphy0` and `csi2_dcphy1`: They are from `rockchip_dts\rockchip\rk3588s.dtsi`
- `mipi0_csi2`, `mipi1_csi2`, `mipi2_csi2`, `mipi3_csi2`, `mipi4_csi2`, and `mipi5_csi2`: These are the nodes that describe the CSI2 host controller, which is responsible for receiving and processing the image data from the camera sensor. They define some properties such as the register address, interrupt, clock, reset, and status. They also have ports that connect to other endpoints, such as the CSI2 DPHY or the CIF MIPI. 
- `rkcif_mipi_lvds0`, `rkcif_mipi_lvds1`, `rkcif_mipi_lvds2`, `rkcif_mipi_lvds3`, `rkcif_mipi_lvds4`, and `rkcif_mipi_lvds5`: These are the nodes that describe the CIF MIPI module, which is a video capture device that can convert MIPI signals to parallel or LVDS signals. They define some properties such as the power domain and status. They also have ports that connect to other endpoints, such as the CSI2 host or the ISP.
- `rkisp1_vir0`, `rkisp1_vir1`, `rkisp1_vir2`, and `rkisp1_vir3`: These are the nodes that describe the ISP virtual devices, which are used to provide a common interface for applications to access different ISP sub-devices. They define some properties such as the status. They also have ports that connect to other endpoints, such as the CIF MIPI or the SDITF.
- `i2c3`: This is the node that describes the I2C bus that connects to some camera sensors and VCM drivers on the evaluation board. It defines some properties such as the pinctrl and status. It also has sub-nodes that describe each device on the bus, such as their compatible name, register address, clock, power domain, pinctrl, GPIOs, lens focus, port, and endpoint.

One example of how these components are related is shown in this file: [rp-camera-dphy1-ov13855.dtsi]. This file describes a camera module that uses an OV13855 sensor and a DW9763 VCM driver on the CSI2 DPHY1 interface. The file includes some definitions for:

- The I2C devices (`dw9763_3` and `ov13855_3`) that communicate with the sensor and the VCM driver.
- The CSI2 DPHY hardware node (`csi2_dphy1_hw`) that provides the physical layer for the interface.
- The CSI2 DPHY logical node (`csi2_dphy3`) that provides the device layer for the interface in full mode.
- The CSI2 host node (`mipi4_csi2`) that receives and processes the image data from the sensor.
- The CIF MIPI node (`rkcif_mipi_lvds4`) that converts MIPI signals to parallel signals.
- The ISP virtual device node (`rkisp1_vir0`) that provides a common interface for applications to access ISP sub-devices.
- The ports and endpoints that connect these nodes together.