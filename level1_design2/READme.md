# Level1 Design2 - Sequence Detector 1011

A sequence detector is a sequential state machine that takes an input string of bits and generates an output 1 whenever the target sequence has been detected

![seq_detect](https://user-images.githubusercontent.com/88897605/182020410-bbc07c8a-400a-4d49-893d-57797dcafc02.png)

# Verification Environment

The values are assigned to the input port using
```
begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;
      end
      SEQ_1011:
      begin
        next_state = IDLE;
      end
    endcase
  end
endmodule

```

The following error is seen:

```
 assert dut.seq_seen.value == 1, f'Sequence must be detected but is not detected. Given sequence = 01011. Model Output: {dut.seq_seen.value} Expected Ouput: 1'

```
#### Test Scenario
* Test Inputs:  01011 
* Expected Output: 1
* Observed Output in the DUT  dut.out.value == 0

Output mismatches for the above inputs proving that there is a design bug in the Functional Verilog Code 

### Seq Dectect Bug
Based on the above test input and analysing the design, we see the following
```
![seq_detect_1011_fail](https://user-images.githubusercontent.com/88897605/182020967-df2db513-fe32-4994-9449-1eb526a2d948.png)
```

#### Seq Dectect Bug Fix

Updating the design and re-running the test makes the test pass
![seq_detect_1011_pass_fix](https://user-images.githubusercontent.com/88897605/182021166-66ef53e9-2d7c-4593-844a-35068242c42a.png)

The updated design is checked in as seq_detect_1011_fix.v


## Level2 Design  - Bit Manipulation Co Processor 

Bit manipulation instructions sets (BMI sets) - The purpose of these instruction sets is to improve the speed of bit manipulation. All the instructions in these sets are non-SIMD and operate only on general-purpose registers.

![bit_manip](https://user-images.githubusercontent.com/88897605/182021873-17ac8bfe-6082-4a4a-b259-4cfba3ff7704.png)

# Verification Environment

The values are assigned to the input port

The following error is seen:

```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x8 does not match MODEL = 0x0
```
#### Test Scenario
* Test Inputs:  1ul
* Expected Output: 0x0
* Observed Output in the DUT  dut.out.value == 0x8

Output mismatches for the above inputs proving that there is a design bug in the Functional Verilog Code 

#### Bit Manipulation Bug

![bitmanip_stimulation_fail py](https://user-images.githubusercontent.com/88897605/182022379-3c2ae43b-53ae-4bfb-bb7b-e93fc587b97a.png)
