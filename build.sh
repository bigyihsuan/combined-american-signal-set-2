#!/bin/bash

set -e

NGRF_DIRS=(/mnt/c/Users/bigyi/Documents/OpenTTD/newgrf /mnt/c/Users/bigyi/OneDrive/Documents/OpenTTD/newgrf)
USAGE="usage: ./build.sh (default | install | bundle | sprites | compile | clean)"
BAD_ARGS=85
GRF_FILENAME=cass2.grf
GRF_PATH=./dist/$GRF_FILENAME

LINE() {
	echo "--------"
}

default() {
	clean
	compile
	bundle
	install
}

sprites() {
	echo "Generating sprites..."
	python3 src/generateSpritesets.py | sed '/^\/\/!SPRITES!\/\//{
		r /dev/stdin
		d
		}' src/cass2_template.nml > out/cass2.nml
	echo "Sprites generated."
}

compile() {
	echo "Compiling GRF..."
	mkdir -v -p out
	sprites
	./nml/nmlc --custom-tags=lang/custom_tags.txt --palette=DOS --nfo=out/cass2.nfo --grf=out/$GRF_FILENAME out/cass2.nml
	echo "Compiling GRF complete."
	LINE
}

bundle() {
	echo "Bundling GRF..."
	rm -v cass2.tar
	rm -v -r dist
	mkdir -v -p dist
	cp -v out/$GRF_FILENAME dist
	cp -v README.md dist/readme.txt
	cp -v LICENSE dist/license.txt
	cp -v changelog.md dist/changelog.txt
	tar cvf cass2.tar dist
	echo "GRF bundled."
	LINE
}

install() {
    echo "Installing GRF..."
    if [[ -e $GRF_PATH ]]; then
		for dir in "${NGRF_DIRS[@]}"; do
			cp -v $GRF_PATH $dir
		done
		echo "Successfully installed."
	else
		echo "GRF path '$GRF_PATH' does not exist."
	fi
	LINE
}

clean() {
    echo "Cleaning installation dir..."
	for dir in "${NGRF_DIRS[@]}"; do
		[ -e "$dir/$GRF_FILENAME" ] && rm -v "$dir/$GRF_FILENAME"
	done
	echo "Cleaning complete."
	LINE
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
elif [[ "$1" = "compile" ]]; then
	compile
elif [[ "$1" = "clean" ]]; then
	clean
else
	echo $USAGE
	exit $BAD_ARGS
fi