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

	mipi_dcphy0: phy@feda0000 {
		compatible = "rockchip,rk3588-mipi-dcphy";
		reg = <0x0 0xfeda0000 0x0 0x10000>;
		rockchip,grf = <&mipidcphy0_grf>;
		clocks = <&cru PCLK_MIPI_DCPHY0>,
			 <&cru CLK_USBDPPHY_MIPIDCPPHY_REF>;
		clock-names = "pclk", "ref";
		resets = <&cru SRST_M_MIPI_DCPHY0>,
			 <&cru SRST_P_MIPI_DCPHY0>,
			 <&cru SRST_P_MIPI_DCPHY0_GRF>,
			 <&cru SRST_S_MIPI_DCPHY0>;
		reset-names = "m_phy", "apb", "grf", "s_phy";
		#phy-cells = <0>;
		status = "disabled";
	};

	mipi_dcphy1: phy@fedb0000 {
		compatible = "rockchip,rk3588-mipi-dcphy";
		reg = <0x0 0xfedb0000 0x0 0x10000>;
		rockchip,grf = <&mipidcphy1_grf>;
		clocks = <&cru PCLK_MIPI_DCPHY1>,
			 <&cru CLK_USBDPPHY_MIPIDCPPHY_REF>;
		clock-names = "pclk", "ref";
		resets = <&cru SRST_M_MIPI_DCPHY1>,
			 <&cru SRST_P_MIPI_DCPHY1>,
			 <&cru SRST_P_MIPI_DCPHY1_GRF>,
			 <&cru SRST_S_MIPI_DCPHY1>;
		reset-names = "m_phy", "apb", "grf", "s_phy";
		#phy-cells = <0>;
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

- `rockchip_dts\rockchip\rp-camera-dphy1-ov13855.dtsi`: This file describes the configuration of a camera module that uses the OV13855 sensor and the DW9763 VCM driver on the CSI2 DPHY1 interface. It defines some properties for the I2C bus, power domain, pinctrl, GRF, GPIOs, clocks, resets, lens focus, ports, and endpoints. There are three other ov13855's dts files: `rp-camera-dcphy0-ov13855.dtsi`, `rp-camera-dphy0-ov13855.dtsi` and `rp-camera-dphy1-ov13855.dtsi`.
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
## Short summary
- `csi2_dphyN` and `csi2_dcphyN` are the device tree nodes that represent the MIPI CSI2 DPHY and DCPHY interfaces, respectively. They are compatible with the `rockchip,rk3568-csi2-dphy` and `rockchip,rk3588-csi2-dcphy` drivers, respectively. They have a property called `rockchip,hw` that points to the corresponding hardware node (`csi2_dphyN_hw` or `mipi_dcphyN`). They also have a `ports` sub-node that defines the input and output endpoints for the DPHY or DCPHY interface. For `csi2_dphyN`, there are **six** different indices: 0, 1, 2, 3, 4, and 5. For `csi2_dcphyN`, there are **two** different indices: 0 and 1.
- `mipiN_csi` is the device tree node that represents the MIPI CSI2 host controller. It is compatible with the `rockchip,rk3588-mipi-csi2` driver. It has a property called `reg` that specifies the base address and size of the CSI2 host controller registers. It also has a `ports` sub-node that defines the input and output endpoints for the CSI2 host controller. For `mipiN_csi`, there are **six** different indices: 0, 1, 2, 3, 4, and 5.
- `csi2_dphyN_hw` and `mipi_dcphyN` are the device tree nodes that represent the hardware configuration of the MIPI CSI2 DPHY and DCPHY interfaces, respectively. They are compatible with the `rockchip,rk3588-csi2-dphy-hw` and `rockchip,rk3588-mipi-dcphy` drivers, respectively. They have properties such as `reg`, `clocks`, `resets`, and `rockchip,grf` that specify the register address, clock sources, reset signals, and GRF registers for the DPHY or DCPHY interface. For `csi2_dphyN_hw`, there are **two** different indices: 0 and 1. For `mipi_dcphyN`, there are **two** different indices: 0 and 1.

To summarize, the relationship between these nodes is that each DPHY or DCPHY interface has a corresponding hardware node and a host controller node, and they are connected by endpoints in their ports sub-nodes. For example, in this page, there is a camera module that uses the OV13855 sensor on the CSI2 DPHY1 interface. The device tree nodes for this configuration are:

- `csi2_dphy1_hw`: The hardware node for CSI2 DPHY1.
- `csi2_dphy3`: The device node for CSI2 DPHY1 in full mode.
- `mipi4_csi2`: The device node for MIPI CSI2 host controller 4.
- `ov13855_3`: The device node for OV13855 sensor.
- The endpoints that connect these nodes are:
    - `<&ov13855_out3>`: The output endpoint of OV13855 sensor.
    - `<&mipi_in_ucam3>`: The input endpoint of CSI2 DPHY1.
    - `<&csidphy1_out>`: The output endpoint of CSI2 DPHY1.
    - `<&mipi4_csi2_input>`: The input endpoint of MIPI CSI2 host controller 4.
    - `<&mipi4_csi2_output>`: The output endpoint of MIPI CSI2 host controller 4.

## Questions
### 1 Are 6 `csi2_dphyN` corresponding to 6 `mipiN_csi`?
No, the 6 `csi2_dphyN` are not corresponding to the 6 `mipiN_csi`. The `csi2_dphyN` are the device nodes for the MIPI CSI2 DPHY interfaces, which are compatible with the `rockchip,rk3568-csi2-dphy` driver. The `mipiN_csi` are the device nodes for the MIPI CSI2 host controller, which are compatible with the `rockchip,rk3588-mipi-csi2` driver. The DPHY interfaces and the host controller are different components of the MIPI CSI2 protocol stack, and they have different functions and properties. The DPHY interfaces are responsible for converting the parallel data from the sensor into serial data for transmission, while the host controller is responsible for receiving, decoding, and processing the serial data from the DPHY interfaces. The DPHY interfaces and the host controller are connected by endpoints in their ports sub-nodes, but they do not have a one-to-one correspondence. For example, in this page, there is a camera module that uses the OV13855 sensor on the CSI2 DPHY1 interface. The device tree nodes for this configuration are:

    - `csi2_dphy1_hw`: The hardware node for CSI2 DPHY1.
    - `csi2_dphy3`: The device node for CSI2 DPHY1 in full mode.
    - `mipi4_csi2`: The device node for MIPI CSI2 host controller 4.
    - `ov13855_3`: The device node for OV13855 sensor.
    - The endpoints that connect these nodes are:
        - `<&ov13855_out3>`: The output endpoint of OV13855 sensor[1].
        - `<&mipi_in_ucam3>`: The input endpoint of CSI2 DPHY1.
        - `<&csidphy1_out>`: The output endpoint of CSI2 DPHY1.
        - `<&mipi4_csi2_input>`: The input endpoint of MIPI CSI2 host controller 4[2].
        - `<&mipi4_csi2_output>`: The output endpoint of MIPI CSI2 host controller 4[3].

    As you can see, the CSI2 DPHY1 interface is represented by two different device nodes (`csi2_dphy1_hw` and `csi2_dphy3`), and it is connected to a different host controller node (`mipi4_csi2`) than its index number.

#### 1.1 What are `mipiN_csi`'s relationship with `csi2_dphyN_hw` and `mipi_dcphyN`?
The `mipiN_csi`'s relationship with `csi2_dphyN_hw` and `mipi_dcphyN` are as follows:

    - The `mipiN_csi` have a property called `reg` that specifies the base address and size of the CSI2 host controller registers. They also have a property called `rockchip,hw` that points to the corresponding hardware node (`csi2_dphyN_hw` or `mipi_dcphyN`). The hardware node contains some properties such as `reg`, `clocks`, `resets`, and `rockchip,grf` that specify the register address, clock sources, reset signals, and GRF registers for the DPHY or DCPHY interface.
    - The `mipiN_csi` have a `ports` sub-node that defines the input and output endpoints for the CSI2 host controller. The input endpoint is connected to the output endpoint of either a DPHY or a DCPHY interface, depending on whether the sensor uses MIPI CSI-2 or MIPI C-PHY protocol. The output endpoint is connected to the input endpoint of another device node, such as a RKISP1 or a RKVDEC.
    - For example, in this page, there is a device node for MIPI CSI2 host controller 0 (`mipi0_csi2`). It has the following properties and ports:

        - `reg = <0x0 0xfdd10000 0x0 0x10000>`: This means that the base address of the CSI2 host controller 0 registers is 0xfdd10000 and the size is 0x10000 bytes.
        - `rockchip,hw = <&csi2_dcphy0>`: This means that the hardware node for this host controller is `csi2_dcphy0`, which represents a MIPI C-PHY interface compatible with the `rockchip,rk3588-csi2-dcphy` driver[4][5].
        - `<&mipi0_csi2_input>`: This is the input endpoint of MIPI CSI2 host controller 0. It is connected to the output endpoint of `csi2_dcphy0`, which is `<&csidcphy0_out>`.
        - `<&mipi0_csi2_output>`: This is the output endpoint of MIPI CSI2 host controller 0[6]. It is connected to the input endpoint of `rkcif_mipi_lvds0`, which is `<&cif_mipi_in0>`.

#### 1.2 Consider the text below, what is this refering to in `dts`?
 ```
 MIPI CSI 输入支持 6 路 MIPI CSI 摄像头输入
 支持2路MIPI CSI 4L，分辨率最大支持1080P@60，每路MIPI CSI 4L均可配置为支持2路最大支持1080P@30及720P@60分辨率。向下兼容RK3588硬件支持的所有分辨率。 
 支持4路MIPI CSI 2L，分辨率最大支持1080P@30及720P@60分辨率。 
 ```
The text you provided is in Chinese, and it describes the MIPI CSI input support for the RK3588 SoC. It says that the RK3588 supports 6 MIPI CSI camera inputs:

    - It supports 2 MIPI CSI 4L, which can support up to 1080P@60 resolution. Each MIPI CSI 4L can be configured to support 2 channels with up to 1080P@30 or 720P@60 resolution. It is backward compatible with all resolutions supported by the RK3588 hardware.
    - It supports 4 MIPI CSI 2L, which can support up to 1080P@30 or 720P@60 resolution.

In the dts file, this is referring to the following device nodes and properties:

- `csi2_dphyN` and `csi2_dcphyN`: These are the device nodes for the MIPI CSI2 DPHY and DCPHY interfaces, respectively. They have a property called `data-lanes` that specifies the number of data lanes used by the sensor. For example, `data-lanes = <1 2 3 4>` means that the sensor uses 4 data lanes[^7^][7]. The DPHY interfaces support MIPI CSI-2 protocol, while the DCPHY interfaces support MIPI C-PHY protocol.
- `mipiN_csi`: These are the device nodes for the MIPI CSI2 host controller. They have a property called `reg` that specifies the base address and size of the host controller registers. For example, `reg = <0x0 0xfdd10000 0x0 0x10000>` means that the base address of the host controller registers is 0xfdd10000 and the size is 0x10000 bytes.
- The endpoints that connect these nodes are defined in their ports sub-nodes. For example, `<&mipi_in_ucam3>` is the input endpoint of CSI2 DPHY1, and `<&mipi4_csi2_input>` is the input endpoint of MIPI CSI2 host controller 4.

#### 1.3 What are `mipiN_csi`'s relationship with `csi2_dphyN` and `csi2_dcphyN`?
In the dts file, this is referring to the following device nodes and properties:

    - `csi2_dphyN` and `csi2_dcphyN`: These are the device nodes for the MIPI CSI2 DPHY and DCPHY interfaces, respectively. They have a property called `data-lanes` that specifies the number of data lanes used by the sensor. For example, `data-lanes = <1 2 3 4>` means that the sensor uses 4 data lanes[7]. The DPHY interfaces support MIPI CSI-2 protocol, while the DCPHY interfaces support MIPI C-PHY protocol.
    - `mipiN_csi`: These are the device nodes for the MIPI CSI2 host controller. They have a property called `reg` that specifies the base address and size of the host controller registers. For example, `reg = <0x0 0xfdd10000 0x0 0x10000>` means that the base address of the host controller registers is 0xfdd10000 and the size is 0x10000 bytes.
    - The endpoints that connect these nodes are defined in their ports sub-nodes. For example, `<&mipi_in_ucam3>` is the input endpoint of CSI2 DPHY1, and `<&mipi4_csi2_input>` is the input endpoint of MIPI CSI2 host controller 4.

The `mipiN_csi` nodes represent the MIPI CSI2 host controllers, while the `csi2_dphyN` and `csi2_dcphyN` nodes represent the MIPI CSI2 DPHY and DCPHY interfaces, respectively. The DPHY and DCPHY interfaces are responsible for converting the parallel data from the sensor into serial data for transmission, while the host controller is responsible for receiving, decoding, and processing the serial data from the DPHY or DCPHY interfaces.

The `mipiN_csi` nodes are connected to either a `csi2_dphyN` or a `csi2_dcphyN` node through their respective input and output endpoints defined in their `ports` sub-nodes. For example, if a camera sensor uses the MIPI CSI-2 protocol, its output endpoint would be connected to the input endpoint of a `csi2_dphyN` node. The output endpoint of that `csi2_dphyN` node would then be connected to the input endpoint of a `mipiN_csi` node. On the other hand, if a camera sensor uses the MIPI C-PHY protocol, its output endpoint would be connected to the input endpoint of a `csi2_dcphyN` node, which would then be connected to a `mipiN_csi` node in a similar manner.