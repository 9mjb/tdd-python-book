
# ######################################################
# https://tech.davis-hansson.com/p/make/
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

# Don't use TABs, use '>'
ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

# targets that don't produce files should be marked as .PHONY
# .PHONY: test  # Make will not look for a file named `test` on the file system
# ######################################################

.PHONY: test
test: .functional_test

.unittest:
> 	./manage.py test && touch .unittest
.functional_test: .unittest
>	./functional_tests.py && touch .functional_test


.PHONY: run
run:
>	manage.py runserver



