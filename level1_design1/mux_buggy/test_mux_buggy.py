# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_buggy(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    sel=1
    #for i in range(4):
    dut.sel.value = 6
    await Timer(2, units='ns')
    