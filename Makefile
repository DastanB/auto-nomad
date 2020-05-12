PROJECT_NAME=django
CONFIG_FILE=local.yml
TEST_CONFIG_FILE=test.yml
PROD_CONFIG_FILE=prod.yml

# colors
GREEN = $(shell tput -Txterm setaf 2)
YELLOW = $(shell tput -Txterm setaf 3)
WHITE = $(shell tput -Txterm setaf 7)
RESET = $(shell tput -Txterm sgr0)
GRAY = $(shell tput -Txterm setaf 6)
TARGET_MAX_CHAR_NUM = 20

# Common

all: run

## Runs application. Builds, creates, starts, and attaches to containers for a service. | Common
run:
	@docker-compose -f $(CONFIG_FILE) up --build -d && docker-compose -f $(CONFIG_FILE) logs -f $(PROJECT_NAME)

## Shows logs of django container | Logs
logs:
	@docker-compose -f $(CONFIG_FILE) logs -f $(PROJECT_NAME)

## Shows logs of celeryworker container
logs-celery:
	@docker-compose -f $(CONFIG_FILE) logs -f celeryworker

## Rebuild application container | rest
build:
	@docker-compose -f $(CONFIG_FILE) build

## Stops application. Stops running container without removing them.
stop:
	@docker-compose -f $(CONFIG_FILE) stop

## Removes stopped service containers.
down:
	@docker-compose -f $(CONFIG_FILE) down

down-all:
	@docker-compose -f $(CONFIG_FILE) down -v

## Runs command `sh` commands in docker container.
bash:
	@docker-compose -f $(CONFIG_FILE) run --rm $(PROJECT_NAME) bash

# Help

## Shows help.
help:
	@echo ''
	@echo 'Usage:'
	@echo ''
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
		    if (index(lastLine, "|") != 0) { \
				stage = substr(lastLine, index(lastLine, "|") + 1); \
				printf "\n ${GRAY}%s: \n\n", stage;  \
			} \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			if (index(lastLine, "|") != 0) { \
				helpMessage = substr(helpMessage, 0, index(helpMessage, "|")-1); \
			} \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''

# Docs

## Runs command `shell_plus` commands in RUNNING docker container.
shell:
	@docker-compose -f $(CONFIG_FILE) exec $(PROJECT_NAME) /entrypoint python manage.py shell_plus

# Database
## Makes migration in RUNNING container.
makemigrations:
	@docker-compose -f $(CONFIG_FILE) exec $(PROJECT_NAME) /entrypoint python manage.py makemigrations

## Upgrades database in RUNNING container.
migrate:
	@docker-compose -f $(CONFIG_FILE) exec $(PROJECT_NAME) /entrypoint python manage.py migrate

## Runs command `shell_plus` commands in docker container.
run-shell:
	@docker-compose -f $(CONFIG_FILE) run --rm $(PROJECT_NAME) python manage.py shell_plus

## Makes migration in container.
run-makemigrations:
	@docker-compose -f $(CONFIG_FILE) run --rm $(PROJECT_NAME) python manage.py makemigrations

## Upgrades database in container.
run-migrate:
	@docker-compose -f $(CONFIG_FILE) run --rm $(PROJECT_NAME) python manage.py migrate

## Runs application with test config.
run-test:
	@docker-compose -f $(TEST_CONFIG_FILE) up --build

## Runs application with prod config.
run-prod:
	@docker-compose -f $(PROD_CONFIG_FILE) up --build
