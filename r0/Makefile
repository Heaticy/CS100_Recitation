PROJECT:=CS100_Recitation0

TEMPLATE:=../template
CLSS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.cls)
STYS_VSP_BEAMER:=$(wildcard ${TEMPLATE}/vsp-beamer/*.sty)
STYS_MINIMUS:=$(wildcard ${TEMPLATE}/minimus/*.sty)

include ${TEMPLATE}/makefile-latex/latex-std-dependence.mk

DEPS_MAIN_TEX:=${CLSS_VSP_BEAMER} ${STYS_VSP_BEAMER} ${STYS_MINIMUS}

# 讲稿：同名加_Script后缀，独立于课件编译，不计入课件的TEXS依赖
SCRIPT:=${PROJECT}_Script
TEXS:=$(filter-out ${SCRIPT}.tex,$(wildcard *.tex))

include ${TEMPLATE}/makefile-latex/makefile-latex.mk

# 讲稿PDF随default目标一并编译
default: ${BUILD_DIR}/${SCRIPT}.pdf

${BUILD_DIR}/${SCRIPT}.pdf: ${SCRIPT}.tex | ${BUILD_DIR}
	${LATEX} ${LATEX_MAIN_FLAGS} ${SCRIPT}.tex
	touch $@
	${NOTIFY_DONE}
