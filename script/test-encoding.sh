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

for tex_file in *.tex; do
	pretty_file=$( pretty_path "$tex_file")
	
	encoding=$(file -bi "$tex_file")
	if [[ $encoding != *"us-ascii"* ]] &&
	   [[ $encoding != *"utf-8"* ]] &&
	   [[ $encoding != *"binary"* ]]
	then
		log "error" "Il file $pretty_file non è salvato nel formato utf-8"
		log "error" "Output: $encoding"
		exit 1
	fi
done
