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

aspell_personal="$REPO_DIR/script/aspell-personal.txt"
aspell_repl="$REPO_DIR/script/aspell-replacements.txt"
aspell_parameters="--lang it --mode tex --encoding utf-8 --personal \"$aspell_personal\" --repl \"$aspell_repl\"";

# Per ogni file tex contenuto nella cartella (non le sottocartelle)
for tex_file in *.tex; do
	pretty_file=$( pretty_path "$tex_file")
	
	log "info" "Controllo l'ortografia del file $pretty_file ..."
	
	# Fai un controllo
	set_red_text
	mispelled=$(cat "$tex_file" | eval "aspell list \"$tex_file\" $aspell_parameters")
	return_code="$?"
	reset_text_color
	
	if [ $return_code != 0 ]; then
		log "error" "ERROR"
		exit 1
	fi
	
	# Se ci sono parole errate
	if [ -n "$mispelled" ]; then
		eval "aspell check \"$tex_file\" $aspell_parameters"
		
		# Riordina il dizionario aspell-personal per facilitare i merge automatici
		head_personal="personal_ws-1.1 it 600"
		body_personal=$(tail -n +2 "$aspell_personal" | sort -s)
		echo "$head_personal" > "$aspell_personal"
		echo -n "$body_personal" >> "$aspell_personal"
		
		# Riordina il dizionario aspell-replacements per facilitare i merge automatici
		head_repl="personal_repl-1.1 it 100"
		body_repl=$(tail -n +2 "$aspell_repl" | sort -s)
		echo "$head_repl" > "$aspell_repl"
		echo -n "$body_repl" >> "$aspell_repl"
		
		mispelled=$(cat "$tex_file" | eval "aspell list \"$tex_file\" $aspell_parameters")
		
		# Se la variabile non è vuota
		if [ -n "$mispelled" ]; then
			log "error" "Il file $pretty_file ha degli errori ortografici non corretti."
			log "error" "Rieseguire il check e utilizzare l'interfaccia interattiva."
			exit 1
		fi
	fi
done
