#!/bin/bash

# Trova automaticamente la cartella principale del repository
REPO_DIR=$(pwd)
while [ "$REPO_DIR" != "/" ] && [ "$REPO_DIR" != "." ]; do
	if [ -f "$REPO_DIR/script/lib.sh" ]; then
		# Includi lo script
		source "$REPO_DIR/script/lib.sh"
		break
	else
		# Sali di un livello
		REPO_DIR=$(dirname "$REPO_DIR")
	fi
done

if [ "$REPO_DIR" == "/" ] || [ "$REPO_DIR" == "." ]; then
	# Non ha trovato la cartella giusta
	echo "/!\ Non ho trovato la cartella principale del repository" 1>&2
	exit 1	
fi

###################
#  Inizio script  #
###################

echo "Conversione dei file PDF presenti repository in formato TXT"
for file in $REPO_DIR/documenti/*/*.pdf
do
	filename=$(basename "$file" .pdf)
	echo $file
	pdftotext -f 7 "$file" "$REPO_DIR/tmp/$filename.gulpease"
done

