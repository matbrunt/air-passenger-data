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

build:
	docker build -f docker/prophet.dockerfile -t honir/prophet:latest ./docker

explore:
	docker-compose up -d explore

prophet:
	docker-compose up -d prophet

shell:
	docker-compose run --rm -w /home/jovyan/work/app explore /bin/bash
