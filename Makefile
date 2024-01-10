.PHONY: setup start add save clean

ORG=r0b4dams
NAME=brightauth
VERSION := $(shell cat _version.txt)

setup: _requirements.txt clean
	@python3 -m venv .venv
	@.venv/bin/pip install -r _requirements.txt

dev: setup .venv/bin/python3
	@.venv/bin/python3 src/main.py

add: .venv
	@.venv/bin/pip install $(pkg)
	@$(MAKE) save

save: .venv
	@.venv/bin/pip freeze > _requirements.txt

clean:
	@rm -rf .venv
	@find . -type f -name "*.pyc" -delete

build: docker-build docker-push

docker-build: setup
	@echo "$(ORG)/$(NAME):$(VERSION)"
	@docker build -t $(ORG)/$(NAME):$(VERSION) .

docker-push: 
	@docker push $(ORG)/$(NAME):$(VERSION)

docker-run: docker-build
	@docker compose up --build 

docker-stop:
	@docker compose down