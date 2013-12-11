
# Il nome della cartella corrente
CURR_DIR_NAME = $(notdir $(shell pwd))

# I file LaTeX che sono inclusi praticamente in ogni documento
MODEL_FILES := $(REPO_DIR)/modello/layout.tex $(REPO_DIR)/modello/global.tex $(REPO_DIR)/modello/steakman.png

# I file che vengono utilizzati per fare il controllo ortografico
DICTIONARIES := $(REPO_DIR)/script/aspell-personal.txt $(REPO_DIR)/script/aspell-replacements.txt

