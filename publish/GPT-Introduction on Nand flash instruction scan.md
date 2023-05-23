#! https://zhuanlan.zhihu.com/p/630765841
# GPT-Introduction on Nand flash instruction scan
```
CONTENT:
Introduction on Nand flash instruction scan
1 What's the structure of Nand flash?
1.1 Does it have a controller to send out instructions?
1.1.1 How does the controller interface with the host?
1.1.1.1 What's the difference and relation between host's instruction and controller's instruction?
1.1.2 What's the difference between Nand flash instrution and ISA, like x86, RISCV, ARM?
1.1.3 Is nand flash's instruction more confidencial than common ISA?
1.2 Can a Nand flash be programed to run specific program?
1.2.1 If so, how to make the  specific program run in the Nand flash?
2 What is instruction scan?
2.1 What's the main purpose of instruction scan?
2.1.1 Does the purpose of instruction scan varies, depending on the target is nand flash or ISA?
2.1.2 If so, what is the purpose correspondingly?
2.2 How do exsiting works implement instruction scan on nand flash?
2.2.1 What is the difference between nand flash and ISA instruction scan?
2.2.2 If the main purpose is to reverse nand flash instruction, how to do that?
2.2.3 If the main purpose is to determine nand flash instruction, it's the same as 2.1?
2.2.4 If a scan program was used to scan nand flash instruction, would it  be processed within or without Nand flash?
```

Nand flash is a type of non-volatile memory that stores data by changing the state of electrically erasable programmable read-only memory (EEPROM) cells. Nand flash has a simple structure consisting of an array of memory cells, each composed of one or more floating-gate transistors, and a controller that manages the read, write, and erase operations on the cells.

## 1 What's the structure of Nand flash?

Nand flash has two main components: the memory array and the controller. The memory array is organized into blocks, each containing a fixed number of pages. A page is the smallest unit of data that can be read or written, and typically ranges from 512 bytes to 16 KB. A block is the smallest unit of data that can be erased, and typically ranges from 16 KB to 4 MB .

### 1.1 Does it have a controller to send out instructions?

Yes, Nand flash has a controller that sends out instructions to the memory array. The controller is responsible for interfacing with the host system, managing the wear-leveling and error correction algorithms, and executing the commands issued by the host. The controller communicates with the memory array through an 8-bit or 16-bit bidirectional data bus, and uses a set of control signals to indicate the type and timing of each operation .

### 1.1.1 How does the controller interface with the host?
The controller interfaces with the host through a standard protocol, such as Serial Peripheral Interface (SPI), Serial ATA (SATA), or Universal Flash Storage (UFS). The protocol defines the format and meaning of the signals that are exchanged between the host and the controller. The host can send commands to the controller to perform various operations on the memory array, such as read, write, erase, or query status. The controller can send data or status information back to the host in response to the commands.

#### 1.1.1.1 What's the difference and relation between host's instruction and controller's instruction?
The host's instruction and the controller's instruction are different in terms of abstraction level and granularity. The host's instruction is a high-level command that specifies what operation to perform on a logical block or page of data in the memory array. For example, a host's instruction could be "write data to page 0x1234". 

The controller's instruction is a low-level command that specifies how to perform an operation on a physical cell or group of cells in the memory array. For example, a controller's instruction could be "apply voltage Vpp to wordline WL0 and bitline BL0 for t microseconds". 

The relation between them is that one host's instruction may correspond to multiple controller's instructions, depending on the complexity and implementation of the operation.

### 1.1.2 What's the difference between Nand flash instruction and ISA, like x86, RISCV, ARM?

Nand flash instruction is a set of commands that specify how to access and manipulate the data stored in the memory array. Nand flash instruction is not a general-purpose instruction set architecture (ISA) like x86, RISCV, or ARM, which define how to perform various computations and control flows on a processor. Nand flash instruction is specific to the Nand flash device and its controller, and does not support arithmetic or logical operations, branching or looping instructions, or registers or memory addressing modes.

### 1.1.3 Is nand flash's instruction more confidencial than common ISA?

Nand flash's instruction is not more confidencial than common ISA, but it may vary depending on the manufacturer and model of the Nand flash device. Different Nand flash devices may have different command sets, timing parameters, and features, such as multi-plane operations, cache programming, or copy-back commands. Therefore, it is important to consult the datasheet of the specific Nand flash device to understand its instruction set and characteristics.

## 1.2 Can a Nand flash be programed to run specific program?

No, Nand flash cannot be programed to run specific program. Nand flash is a passive storage device that only responds to the commands issued by the host system or the controller. It does not have a processor or an execution unit that can run program code. Nand flash can only store data that can be read or written by the host system or the controller.

### 1.2.1 If so, how to make the specific program run in the Nand flash?

Not applicable.

## 2 What is instruction scan?

Instruction scan is a technique to analyze and reverse engineer the instruction set and behavior of a Nand flash device. Instruction scan involves sending various commands to the Nand flash device and observing its responses, such as status codes, data output, or power consumption. By systematically scanning all possible commands and parameters, instruction scan can reveal information such as the supported command set, the page and block size, the erase count limit, or the error correction scheme of the Nand flash device.

### 2.1 What's the main purpose of instruction scan?

The main purpose of instruction scan is to understand how a Nand flash device works and how to interact with it effectively. Instruction scan can help researchers and developers to:

- Identify unknown or undocumented Nand flash devices
- Discover hidden or proprietary features or commands
- Test the reliability and security of Nand flash devices
- Optimize the performance and compatibility of Nand flash devices
- Recover data from damaged or corrupted Nand flash devices

### 2.1.1 Does the purpose of instruction scan vary depending on whether the target is nand flash or ISA?

Yes, the purpose of instruction scan varies depending on whether the target is nand flash or ISA. 

For nand flash, instruction scan can be used to reveal the hidden features or commands of the device, to bypass security mechanisms or encryption schemes, or to modify or clone the data stored in the device. It also may reveal information about physical characteristics such as cell layout or wear-leveling algorithm

For ISA, instruction scan can be used to discover undocumented or unused instructions, to test the correctness or robustness of the processor, or to exploit potential weaknesses or backdoors in the processor. It also may reveal information about logical characteristics such as instruction encoding or register usage.


### 2.2 How do existing works implement instruction scan on nand flash?

Existing works implement instruction scan on nand flash by using various tools and methods such as:

- Logic analyzers or oscilloscopes to capture and analyze signals between host system/controller and nand flash device
- Custom hardware platforms or software libraries to send commands and receive responses from nand flash device
- Fuzzing techniques to generate random or semi-random commands and parameters
- Machine learning techniques to classify or cluster commands based on their responses
- Differential analysis techniques to compare responses across different devices or conditions

### 2.2.1 What is the difference between nand flash and ISA instruction scan?

The difference between nand flash and ISA instruction scan is that nand flash instruction scan requires direct access to the nand flash device and its interface signals, while ISA instruction scan can be performed on any system that runs code on a processor with an ISA. Nand flash instruction scan also involves more physical parameters such as voltage levels or timing constraints than ISA instruction scan.

### 2.2.2 If the main purpose is to reverse nand flash instruction set how to do that?

To reverse nand flash instruction set one possible approach is:

- Identify basic commands such as read id (90h), read status (70h), reset (ffh), etc.
- Identify page size by sending read commands with different column addresses
- Identify block size by sending erase commands with different row addresses
- Identify supported features by sending extended commands such as multi-plane (11h), cache (15h), copy-back (00h/35h), etc.
- Identify error correction scheme by sending write commands with corrupted data and reading back status codes
- Identify command encoding by sending invalid commands and observing status codes

### 2.2.3 If the main purpose is to determine nand flash instruction set isn't it same as 2.1?

No, determining nand flash instruction set means finding out what commands are supported by a given nand flash device without necessarily understanding their meaning or behavior while reversing nand flash instruction set means finding out both what commands are supported and how they work.

### 2.2.4 If a scan program was used to scan nand flash instruction would it be processed within or without Nand Flash?

A scan program would be processed without Nand Flash because Nand Flash cannot run program code by itself it can only store data that can be read or written by another system.