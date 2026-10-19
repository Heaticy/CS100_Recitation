PROJECT:=CS100_Recitation4

TEMPLATE:=../template
CLSS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.cls)
STYS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.sty)
STYS_MINIMUS:=$(wildcard ${TEMPLATE}/minimus/*.sty)

include ${TEMPLATE}/makefile-latex/latex-std-dependence.mk

DEPS_MAIN_TEX:=${CLSS_VSP_BEAMER} ${STYS_VSP_BEAMER} ${STYS_MINIMUS} $(shell find code -type f) $(wildcard image/*.png image/*.jpg image/*.pdf)

include ${TEMPLATE}/makefile-latex/makefile-latex.mk

.PHONY: demos check-demos check-behavior check-all package
demos:
	bash code/build-demos.sh

check-demos: demos
	python3 code/check-demos.py

check-behavior:
	python3 code/check-behavior.py

check-all: check-demos check-behavior

package: default
	python3 code/package-release.py
