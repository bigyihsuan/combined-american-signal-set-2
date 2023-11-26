#!/bin/bash

NGRF_DIR=/mnt/c/Users/bigyi/OneDrive/Documents/OpenTTD/newgrf/
USAGE="usage: ./build.sh (default | install | bundle)"
BAD_ARGS=85

sprites() {
	python3 generateSpritesets.py | sed '/^#SPRITES#/{
		r /dev/stdin
		d
		}' cass2_template.nml > cass2.nml
}

default() {
	sprites
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

if [[ "$#" -eq 0 ]]; then
	default
	exit 0
fi

if [[ "$1" = "sprites" ]]; then
	sprites
elif [[ "$1" = "default" ]]; then
	default
elif [[ "$1" = "install" ]]; then
	install
elif [[ "$1" = "bundle" ]]; then
	bundle
else
	echo $USAGE
	exit $BAD_ARGS
fi