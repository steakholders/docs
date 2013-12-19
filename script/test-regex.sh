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

function grep_test() {
	regexp="$1"
	error_message="$2"
	files="${@:3}"
	
	#result=$(grep -l "$regexp" $files)
	result=$(grep --color=always "$regexp" $files)
	status="$?"
	
	if [ "$status" -gt 1 ]; then
		log "error" "Errore di grep, exit status $status"
		exit 2
	fi
	
	if [ "$status" == "0" ]; then
		log "warning" "Attenzione, sono state trovate occorrenze dell'espressione regolare '$regexp'."
		log "warning" "$error_message"
		echo "$result"
	fi
}

# Comandi deprecati
grep_test "\\\groupName" "Sostituire con \GroupName{}." $(find . -name '*.tex')
grep_test "\\\projectName" "Sostituire con \ProjectName{}." $(find . -name '*.tex')
grep_test "\\\proponente" "Sostituire con \Proponente{}." $(find . -name '*.tex')
grep_test "\\\committente" "Sostituire con \Committente{}." $(find . -name '*.tex')

# Tipico utilizzo errato che 'mangia' lo spazio successivo al comando
grep_test "\\\LaTeX[^{}]" "Sostituire con \LaTeX{}." $(find . -name '*.tex')
grep_test "\\\GroupName[^{}]" "Sostituire con \GroupName{}." $(find . -name '*.tex')
grep_test "\\\ProjectName[^{}]" "Sostituire con \ProjectName{}." $(find . -name '*.tex')
grep_test "\\\Proponente[^{}]" "Sostituire con \Proponente{}." $(find . -name '*.tex')
grep_test "\\\Committente[^{}]" "Sostituire con \Committente{}." $(find . -name '*.tex')

# Errori tipici con LaTeX
grep_test " [[:alpha:]]*_" "Utilizzare il comando LaTeX \_ (l'underscore ha un'altra funzione)" $(find . -name '*.tex')

# Errori ortografici
grep_test "E'" "Sostituire con È." $(find . -name '*.tex')
grep_test "[[:alpha:]]\`[aeiou]" "Riscrivere usando l'accento giusto: uno tra àèìòù" $(find . -name '*.tex')

# Codici speciali
grep_test "TODO" "C'è un TODO non risolto." $(find . -name '*.tex')
grep_test "FIXME" "C'è un FIXME non risolto." $(find . -name '*.tex')
grep_test "^>>>>>" "C'è un merge non risolto." $(find . -name '*.tex')
grep_test "^=====" "C'è un merge non risolto." $(find . -name '*.tex')
grep_test "^<<<<<" "C'è un merge non risolto." $(find . -name '*.tex')

# Controlla che ci sia prima il nome e poi il cognome
grep_test "Poli Federico" "Riscrivere mettendo prima il nome e poi il cognome." $(find . -name '*.tex')
grep_test "Rotundo Enrico" "Riscrivere mettendo prima il nome e poi il cognome." $(find . -name '*.tex')
grep_test "Girardi Serena" "Riscrivere mettendo prima il nome e poi il cognome." $(find . -name '*.tex')
grep_test "Tresoldi Nicolò" "Riscrivere mettendo prima il nome e poi il cognome." $(find . -name '*.tex')
grep_test "Donato Gianluca" "Riscrivere mettendo prima il nome e poi il cognome." $(find . -name '*.tex')
grep_test "De Francheschi luca" "Riscrivere mettendo prima il nome e poi il cognome." $(find . -name '*.tex')
grep_test "Fornari Giacomo" "Riscrivere mettendo prima il nome e poi il cognome." $(find . -name '*.tex')
