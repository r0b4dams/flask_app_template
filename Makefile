.PHONY: setup dev add save clean

ORG=r0b4dams
NAME=flask_app_template
VERSION := $(shell cat version.txt || echo '0.0.1')

install: clean
	test -f requirements.txt || touch requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

dev: .venv
	@.venv/bin/python3 src

preview: .venv
	@export MODE=production && .venv/bin/python3 src

add: .venv
	@.venv/bin/pip install $(pkg)
	@$(MAKE) save

save: .venv
	@.venv/bin/pip freeze > requirements.txt

clean:
	@rm -rf .venv
	@find . -type f -name "*.pyc" -delete


image: docker-build docker-push

docker-build: install
	@docker build -t $(ORG)/$(NAME):$(VERSION) .

docker-push: 
	@docker push $(ORG)/$(NAME):$(VERSION)