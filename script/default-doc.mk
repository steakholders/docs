
all:
	@make test-spelling
	@make documents

documents: $(CURR_DIR_NAME).pdf

# Compila il file LaTeX principale
$(CURR_DIR_NAME).pdf: *.tex $(MODEL_FILES)
	@$(REPO_DIR)/script/compile-latex.sh

# Con questo trucchetto viene creato un file vuoto, la cui data di modifica
# viene usata dal makefile per decidere se è necessario rieseguire i comandi.
test-spelling: test-spelling.cache
test-spelling.cache: *.tex $(DICTIONARIES)
	@$(REPO_DIR)/script/test-encoding.sh
	@$(REPO_DIR)/script/test-spelling.sh
	@touch $@

clean:
	@rm -f *.cache
	@rm -f *.log *.tex.backup
	@rm -f *~
	@rm -f *.aux *.out *.toc
	@rm -f *.pdf
	@rm -f *.tex.bak
	@rm -f *.lof *.lot
