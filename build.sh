#!/bin/bash

NMLC=nmlc
NGRF_DIR=/mnt/c/Users/bigyihsuan/Documents/OpenTTD/newgrf/

default() {
	$(NMLC) cass2.nml --nfo=cass2.nfo --grf=cass2.grf
}

install() {
	cp cass2.grf $(NGRF_DIR)
}

bundle() {
	default
	mkdir -p cass2
	cp cass2.grf cass2
	cp README.md cass2/readme.txt
	cp LICENSE cass2/license.txt
	cp changelog.md cass2/changelog.txt
	tar cvf cass2.tar cass2
}