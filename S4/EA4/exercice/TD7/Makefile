.PHONY: all


TOPDF=pdflatex
OPT= -shell-escape -output-directory
TARGET=target
SRC=src
FILE=td7.tex



all:
	mkdir -p $(TARGET)
	cd $(SRC) && $(TOPDF) $(OPT) ../$(TARGET) $(FILE)
