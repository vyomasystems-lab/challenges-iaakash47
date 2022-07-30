# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)  # reference model

VERILOG_SOURCES = $(PWD)/mkbitmanip_buggy.v

TOPLEVEL := mkbitmanip_buggy        # design
MODULE   := test_mkbitmanip_buggy   # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
