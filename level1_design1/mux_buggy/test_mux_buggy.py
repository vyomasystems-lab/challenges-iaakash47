# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    inp00=1
    inp01=0
    inp1=0
    inp2=1
    inp3=0
    inp4=0
    inp5=1
    inp6=0
    inp7=0
    inp8=1
    inp9=0
    inp10=0
    inp11=1
    inp12=0
    inp13=0
    inp14=1
    inp15=0
    inp16=0
    inp17=1
    inp18=0
    inp19=0
    inp20=1
    inp21=0
    inp23=0
    inp24=0
    inp25=1
    inp26=0
    inp27=0
    inp28=1
    inp29=0
    inp30=1

    
    sel=[inp00,inp01,inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11,inp12,inp13,inp14,inp15,inp16,inp17,inp18,inp19,inp20,inp21,inp22,inp23,inp24,inp25,inp26,inp27,inp28,inp29,inp30]
    for i in range(32):
        dut.sel.value=sel[i]
        assert dut.out.value==sel[i]
