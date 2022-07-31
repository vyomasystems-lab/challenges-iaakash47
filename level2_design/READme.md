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

#### Bit Manipulation Bug Fix

Updating the design and re-running the test makes the test pass

![bitmanip_stimulation_pass_fix py](https://user-images.githubusercontent.com/88897605/182022444-0ba05b30-fd41-462a-ba2c-049ce62df993.png)

The updated design is checked in as mkbitmanip_fix.v
