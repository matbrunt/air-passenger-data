#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = air-passenger-data

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Clean downloaded data files
clean-all:
	rm -f src/data/**/*

clean:
	rm -f src/data/interim/* src/data/processed/*

explore:
	docker-compose up -d explore

shell:
	docker-compose run --rm -w /home/jovyan/work/app explore /bin/bash
