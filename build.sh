#!/bin/bash

NGRF_DIR=/mnt/c/Users/bigyi/OneDrive/Documents/OpenTTD/newgrf/
USAGE="usage: ./build.sh (default | install | bundle)"
BAD_ARGS=85

default() {
	mkdir -p out
	nmlc --nfo=out/cass2.nfo --grf=out/cass2.grf --palette=DOS cass2.nml
	# nmlc --grf=cass2.grf cass2.nml
}

install() {
	default
	if [[ -e "./out/cass2.grf" ]]; then
		cp ./out/cass2.grf $NGRF_DIR
	fi
}

bundle() {
	default
	cp README.md out/readme.txt
	cp LICENSE out/license.txt
	cp changelog.md out/changelog.txt
	tar cvf cass2.tar out
}

if [[ ! -n "$1" ]]; then
	echo $USAGE
	exit $BAD_ARGS
fi

if [[ "$1" = "default" ]]; then
	default
elif [[ "$1" = "install" ]]; then
	install
elif [[ "$1" = "bundle" ]]; then
	bundle
else
	echo $USAGE
	exit $BAD_ARGS
fi