.PHONY: all


TOPDF=pdflatex
OPT=-output-directory
TARGET=target
SRC=src
FILE=td3.tex



all:
	mkdir -p $(TARGET)
	cd $(SRC) && $(TOPDF) $(OPT) ../$(TARGET) $(FILE)
