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

file_richieste="/tmp/file_a.tmp"
file_definite="/tmp/file_b.tmp"

# grep "\\\\glossario{[^}]*}" -R "$REPO_DIR" -osh --include="*.tex"
# "\\\\glossario{[^}]*}": trova tutte le stringhe della forma \glossario{qualcosa che non sia una chiusa graffa}
# -R "$REPO_DIR": cerca ricorsivamente in tutti i file della cartella $REPO_DIR
# -o: visualizza solo i match
# -s: non visualizzare errori se non riesce a leggere qualche file
# -h: non visualizzare in output il nome del file che contiene il match
# --include="*.txt": controlla solo i file .tex
#
# sed 's/.glossario{\([^}]*\)}/\1/g'
# prende in input "\glossario{qualcosa}" e restituisce solo "qualcosa"
#
# sort: ordina
#
# uniq: toglie i duplicati
#
grep "\\\\glossario{[^}]*}" -R "$REPO_DIR" -osh --include="*.tex" | sed 's/.glossario{\([^}]*\)}/\1/g' | sort | uniq > "$file_richieste"
grep "\\\\definizione{[^}]*}" -R "$REPO_DIR" -osh --include="*.tex" | sed 's/.definizione{\([^}]*\)}/\1/g' | sort | uniq > "$file_definite"

# Trova le differenze tra le due liste
non_ancora_definite=$(grep -Fxv -i -f "$file_definite"  "$file_richieste")
definite_non_richieste=$(grep -Fxv -i -f "$file_richieste"  "$file_definite")

# Cancella i file temporanei
rm "$file_richieste" "$file_definite"

# Segnala le differenze
if [ ! -z "$non_ancora_definite" ]; then
	log "error" "Ci sono dei termini non ancora definiti nel dizionario"
	log "error" "$non_ancora_definite"
	exit 1
fi

