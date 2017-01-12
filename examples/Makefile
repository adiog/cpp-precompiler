CC=gcc-wrap.sh
CFLAGS=-std=c++14 -Wall -pedantic
LDFLAGS=-lpthread

SRC_DIR=.
SRC_FILES=$(wildcard $(SRC_DIR)/*.cc)
ELF_FILES=$(SRC_FILES:.cc=)

%: %.cc
		$(CC) $(CFLAGS) $(LDFLAGS) $< -o $@

all:	$(ELF_FILES)

