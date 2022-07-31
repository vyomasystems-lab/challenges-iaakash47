# Level3 Design  - Axi Lite Slave

The AxiMaster and AxiLiteMaster classes implement AXI masters and are capable of generating read and write operations against AXI slaves. Requested operations will be split and aligned according to the AXI specification. The AxiMaster module is capable of generating narrow bursts, handling multiple in-flight operations, and handling reordering and interleaving in responses across different transaction IDs. AxiMaster and AxiLiteMaster and related objects all extend Region, so they can be attached to AddressSpace objects to handle memory operations in the specified region.

AxiLiteSlave classes implement AXI slaves and are capable of completing read and write operations from upstream AXI masters. The AxiSlave module is capable of handling narrow bursts. These modules can either be used to perform memory reads and writes on a MemoryInterface on behalf of the DUT, or they can be extended to implement customized functionality.

The AxiSlave is a wrapper around AxiSlaveWrite and AxiSlaveRead. Similarly, AxiLiteSlave is a wrapper around AxiLiteSlaveWrite and AxiLiteSlaveRead. If a read-only or write-only interface is required instead of a full interface, use the corresponding read-only or write-only variant, the usage and API are exactly the same.
Once the module is instantiated, read and write operations can be initiated in a couple of different ways.

First, operations can be carried out with async blocking ```read(), write()``` , and their associated word-access wrappers. Multiple concurrent operations started from different coroutines are handled correctly, with results returned in the order that the operations complete



### Introduction to AXI4-Lite (Advanced Extensible Interface)

Advanced eXtensible Interface 4 (AXI4) is a family of buses defined as part of the fourth generation of the ARM Advanced Microcontroler Bus Architectrue (AMBA) standard. AXI was first introduced with the third generation of AMBA, as AXI3

The AMBA specification defines 3 AXI4 protocols:

* AXI4: A high performance memory mapped data and address interface. Capable of Burst access to memory mapped devices.
* AXI4-Lite: A subset of AXI, lacking burst access capability. Has a simpler interface than the full AXI4 interface.
* AXI4-Stream: A fast unidirectional protocol for transfering data from master to slave.


# Verification Environment

The values are assigned to the input port

#### Test Scenario
* Test Inputs: AXI Signals
* Expected Output: 17,18,19,1a,1b,1c 1d
* Observed Output in the DUT  dut.out.value == 0

Output mismatches for the above inputs proving that there is a design bug in the Functional Verilog Code



![IMG_20220731_211247](https://user-images.githubusercontent.com/88897605/182035121-f5a026b8-bdf4-4f8a-b66a-c32273f3ebf6.png)
![IMG_20220731_211409](https://user-images.githubusercontent.com/88897605/182035119-5654bc3f-84d1-4b95-a34c-900196373a99.png)


### Level3 Design Bug

```
parameter VALID_ADDR_WIDTH = ADDR_WIDTH + $clog2(STRB_WIDTH);                                                         ====> BUG in the code
parameter WORD_WIDTH = STRB_WIDTH;
parameter WORD_SIZE = DATA_WIDTH/WORD_WIDTH;

reg mem_wr_en;
reg mem_rd_en;

reg s_axil_awready_reg = 1'b0, s_axil_awready_next;
reg s_axil_wready_reg = 1'b0, s_axil_wready_next;
reg s_axil_bvalid_reg = 1'b0, s_axil_bvalid_next;
reg s_axil_arready_reg = 1'b0, s_axil_arready_next;
reg [DATA_WIDTH-1:0] s_axil_rdata_reg = {DATA_WIDTH{1'b0}}, s_axil_rdata_next;
reg s_axil_rvalid_reg = 1'b0, s_axil_rvalid_next;
reg [DATA_WIDTH-1:0] s_axil_rdata_pipe_reg = {DATA_WIDTH{1'b0}};
reg s_axil_rvalid_pipe_reg = 1'b0;

// (* RAM_STYLE="BLOCK" *)
reg [DATA_WIDTH-1:0] mem[(2**VALID_ADDR_WIDTH)-1:0];

wire [VALID_ADDR_WIDTH-1:0] s_axil_awaddr_valid = s_axil_awaddr >> (ADDR_WIDTH + VALID_ADDR_WIDTH);                   ====> BUG in the code
wire [VALID_ADDR_WIDTH-1:0] s_axil_araddr_valid = s_axil_araddr >> (ADDR_WIDTH + VALID_ADDR_WIDTH);                   ====> BUG in the code

```

### Design Fix
Based on the above Bug test input and analysing the design, we can Debug the following code by adding input values

Updating the design and re-running the test makes the test pass
```
parameter VALID_ADDR_WIDTH = ADDR_WIDTH - $clog2(STRB_WIDTH);         ====> BUG Resolved 
parameter WORD_WIDTH = STRB_WIDTH;
parameter WORD_SIZE = DATA_WIDTH/WORD_WIDTH;

reg mem_wr_en;
reg mem_rd_en;

reg s_axil_awready_reg = 1'b0, s_axil_awready_next;
reg s_axil_wready_reg = 1'b0, s_axil_wready_next;
reg s_axil_bvalid_reg = 1'b0, s_axil_bvalid_next;
reg s_axil_arready_reg = 1'b0, s_axil_arready_next;
reg [DATA_WIDTH-1:0] s_axil_rdata_reg = {DATA_WIDTH{1'b0}}, s_axil_rdata_next;
reg s_axil_rvalid_reg = 1'b0, s_axil_rvalid_next;
reg [DATA_WIDTH-1:0] s_axil_rdata_pipe_reg = {DATA_WIDTH{1'b0}};
reg s_axil_rvalid_pipe_reg = 1'b0;

// (* RAM_STYLE="BLOCK" *)
reg [DATA_WIDTH-1:0] mem[(2**VALID_ADDR_WIDTH)-1:0];

wire [VALID_ADDR_WIDTH-1:0] s_axil_awaddr_valid = s_axil_awaddr >> (ADDR_WIDTH - VALID_ADDR_WIDTH);     ====> BUG Resolved 
wire [VALID_ADDR_WIDTH-1:0] s_axil_araddr_valid = s_axil_araddr >> (ADDR_WIDTH - VALID_ADDR_WIDTH);     ====> BUG Resolved 
```
The updated design is checked in as axi_lite_slave_buggy.v

#### Level3 Design Bug Fix

![IMG_20220731_211324](https://user-images.githubusercontent.com/88897605/182035401-0b94c71a-196f-4315-8ff0-5c6147b532c4.png)

# AXI Lite Slave  Reference Waveform
![c1fe3809e14e48fafe99944ac3b6c04c](https://user-images.githubusercontent.com/88897605/182039247-bd763630-0f91-457f-968e-ec5f851e6956.png)


# AXI Lite Slave Waveform
![IMG_20220731_232459](https://user-images.githubusercontent.com/88897605/182039192-abf5d4a3-b3c9-44bc-b4f1-f28ee5f72d8a.jpg)
