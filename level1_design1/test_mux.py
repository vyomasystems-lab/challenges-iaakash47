# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
    
async def mux_basic_test(dut):
    """Test for INP30"""

    INP30 = 3    
    SEL = 30

    # input driving
    dut.inp30.value = INP30    
    dut.sel.value = SEL

    await Timer(2, units='ns')
    
    assert dut.out.value == INP30, "Mux result is incorrect: {INP30} != {OUT}, expected value={EXP}".format(
            INP30=int(dut.inp30.value), SEL=int(dut.sel.value), OUT=int(dut.out.value), EXP=INP30)
