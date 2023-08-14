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
