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

# Cartella in cui LaTeX deve cercare gli *.sty
#export TEXINPUTS="$REPO_DIR/modello:"

# Compila tante volte (serve per poter fare l'indice)

# 1: Draft mode
errors=$(pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -draftmode "$main_tex" | grep -E ".*:[0-9]+:.*")

# Se c'è stato un errore
if [[ $errors != "" ]]; then
	log "error" "ERRORE"
	log "error" "Ci sono stati errori nella compilazione draftmode di $pretty_file"
	set_red_text; echo "$errors"; reset_text_color;
	rm "${main_tex%.tex}.pdf"
	exit 1
fi

# 1: Completo
errors=$(pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$main_tex" | grep -E ".*:[0-9]+:.*")

# Se c'è stato un errore
if [[ $errors != "" ]]; then
	log "error" "ERRORE"
	log "error" "Ci sono stati errori nella compilazione completa di $pretty_file"
	set_red_text; echo "$errors"; reset_text_color;
	rm "${main_tex%.tex}.pdf"
	exit 1
fi

# Se non ci sono stati errori
log "success" "OK"

