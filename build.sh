#!/bin/bash

NGRF_DIR=/mnt/c/Users/bigyi/OneDrive/Documents/OpenTTD/newgrf/
USAGE="usage: ./build.sh (default | install | bundle)"
BAD_ARGS=85

sprites() {
	python3 generateSpritesets.py | sed '/^\/\/!SPRITES!\/\//{
		r /dev/stdin
		d
		}' cass2_template.nml > out/cass2.nml
}

default() {
	mkdir -p out
	sprites
	nmlc --custom-tags=./lang/custom_tags.txt --palette=DOS --nfo=out/cass2.nfo --grf=out/cass2.grf out/cass2.nml
}

install() {
	default
	if [[ -e "./out/cass2.grf" ]]; then
		cp ./out/cass2.grf $NGRF_DIR
	fi
}

clean() {
	rm "$NGRF_DIR/cass2.grf"
}

bundle() {
	rm cass2.tar
	rm -r dist
	mkdir -p dist
	default
	cp out/cass2.grf dist
	cp README.md dist/readme.txt
	cp LICENSE dist/license.txt
	cp changelog.md dist/changelog.txt
	tar cvf cass2.tar dist
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
elif [[ "$1" = "clean" ]]; then
	clean
else
	echo $USAGE
	exit $BAD_ARGS
fi