In this blog post, I will introduce the basic concept of Nand flash instruction scan, which is a technique to analyze the internal operations of Nand flash memory devices. Nand flash is a type of non-volatile memory that stores data by changing the electrical charge of cells arranged in a grid. Each cell can store one or more bits of data, depending on the technology.

## 1 What's the structure of Nand flash?
Nand flash consists of several components, such as the memory array, the controller, the interface, and the power supply. The memory array is where the data is stored in cells. The controller is responsible for managing the read, write, and erase operations on the memory array. The interface is the communication channel between the controller and the host device, such as a computer or a smartphone. The power supply provides the necessary voltage and current for the memory operations.

### 1.1 Does it have a controller to send out instructions?
Yes, Nand flash has a controller that sends out instructions to the memory array. The controller is usually embedded in the same package as the memory array, or integrated on a separate chip. The controller has a set of registers that store the commands, addresses, and data for each operation. The controller also has a state machine that controls the timing and sequence of the operations.

#### 1.1.1 How does the controller interface with the host?
The controller interfaces with the host through a standard protocol, such as Serial Peripheral Interface (SPI), Serial ATA (SATA), or Universal Flash Storage (UFS). The protocol defines the format and meaning of the signals that are exchanged between the host and the controller. The host can send commands to the controller to perform various operations on the memory array, such as read, write, erase, or query status. The controller can send data or status information back to the host in response to the commands.

#### 1.1.1.1 What's the difference and relation between host's instruction and controller's instruction?
The host's instruction and the controller's instruction are different in terms of abstraction level and granularity. The host's instruction is a high-level command that specifies what operation to perform on a logical block or page of data in the memory array. For example, a host's instruction could be "write data to page 0x1234". 

The controller's instruction is a low-level command that specifies how to perform an operation on a physical cell or group of cells in the memory array. For example, a controller's instruction could be "apply voltage Vpp to wordline WL0 and bitline BL0 for t microseconds". 

The relation between them is that one host's instruction may correspond to multiple controller's instructions, depending on the complexity and implementation of the operation.

