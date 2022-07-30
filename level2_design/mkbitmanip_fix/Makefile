# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)  # reference model

VERILOG_SOURCES = $(PWD)/mkbitmanip_fix.v

TOPLEVEL := mkbitmanip_fix        # design
MODULE   := test_mkbitmanip_fix   # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
