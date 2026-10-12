PROJECT:=CS100_Recitation2

TEMPLATE:=../template
CLSS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.cls)
STYS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.sty)
STYS_MINIMUS:=$(wildcard ${TEMPLATE}/minimus/*.sty)
CLSS_STANDALONE_SILICON:=$(wildcard ${TEMPLATE}/standalone-silicon/*.cls)

include ${TEMPLATE}/makefile-latex/latex-std-dependence.mk

DEPS_MAIN_TEX:=${CLSS_VSP_BEAMER} ${STYS_VSP_BEAMER} ${STYS_MINIMUS}
DEPS_FIGS_TEX:=${STYS_MINIMUS} ${CLSS_STANDALONE_SILICON}

include ${TEMPLATE}/makefile-latex/makefile-latex.mk

# 图像编译产物位于build/，确保目录先于图像编译创建
${FIGS_TEX_PDF}: | ${BUILD_DIR}
