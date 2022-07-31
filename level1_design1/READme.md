### Level1 Design1 - Basic Multiplexer

A multiplexer or mux is a combinational circuits that selects several analog or digital input signals and forwards the selected input into a single output line. A multiplexer of 2n inputs has n selected lines, are used to select which input line to send to the output

![mux](https://user-images.githubusercontent.com/88897605/182018710-08601ec6-a5e3-4c1f-9189-d94139f15e61.png)

# Verification Environment

The values are assigned to the input port using
```
5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;
```   
The following error is seen:
```
assert dut.out.value == INP30, "Mux result is incorrect: {INP30} != {OUT}, expected value={EXP}".format(
                     AssertionError: Mux result is incorrect: 3 != 0, expected value=3
```
#### Test Scenario
* Test Inputs: Binary Numbers
* Expected Output: 3
* Observed Output in the DUT  dut.out.value == 0

Output mismatches for the above inputs proving that there is a design bug in the Functional Verilog Code 

### Design Bug
Based on the above test input and analysing the design, we see the following
```
 5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      default: out = 0;                                 ====> BUG
    endcase
  end

endmodule 

For the Multiplexer Design , the logic should be 31 bits of input instead of 30bits of input as in the design code.
```
#### Mux Bug 

![mux_test_failed](https://user-images.githubusercontent.com/88897605/182019902-ba67d5be-4006-4195-9551-5dd136a6ca71.png)


### Design Fix
Based on the above Bug test input and analysing the design, we can Debug the following code by adding input values
```
 5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      5'b11110: out = inp30;                                 ====> BUG RESOLVED 
      default: out = 0;
    endcase
  end

endmodule 
```
#### Mux Bug Fix

Updating the design and re-running the test makes the test pass

![mux_bug_fix](https://user-images.githubusercontent.com/88897605/182020098-676eef55-04c9-41d0-a36e-f88422489056.png)
The updated design is checked in as mux_fix.v
