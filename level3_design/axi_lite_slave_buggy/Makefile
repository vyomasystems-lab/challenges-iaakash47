# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/axi_lite_slave_buggy.v

TOPLEVEL :=  axi_lite_slave_buggy          # design
MODULE   :=  test_axi_lite_slave_buggy       # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build _pycache_