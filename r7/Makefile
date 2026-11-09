PROJECT:=CS100_Recitation7
TEMPLATE:=../template
CLSS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.cls)
STYS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.sty)
STYS_MINIMUS:=$(wildcard ${TEMPLATE}/minimus/*.sty)
include ${TEMPLATE}/makefile-latex/latex-std-dependence.mk
DEPS_MAIN_TEX:=${CLSS_VSP_BEAMER} ${STYS_VSP_BEAMER} ${STYS_MINIMUS} $(wildcard code/*) $(wildcard image/*)
include ${TEMPLATE}/makefile-latex/makefile-latex.mk
.PHONY: check-demos
check-demos:
	python3 code/check-demos.py
