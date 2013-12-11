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

# Ottiene il nome della cartella
main_tex=$(basename "$(pwd)")".tex"

# Riceve il nome del file da compilare come parametro
#main_tex="$1"

pretty_file=$( pretty_path "$main_tex")

# Il parametro -n non fa andare a capo
log "info" "Compilo $pretty_file ..."

# Compila il pdf 3 volte (serve per poter fare l'indice)
for iter in $(seq 3); do
	pdflatex -interaction=nonstopmode -halt-on-error "$main_tex" > /dev/null
	
	# Se c'è stato un errore
	if [[ $? != 0 ]]; then
		log "error" "ERRORE"
		log "error" "C'è stato un errore nella compilazione."
		log "error" "Controllare in un editor il file $pretty_file e riprovare."
		exit 1
	fi
done

# Se non ci sono stati errori
log "success" "OK"

