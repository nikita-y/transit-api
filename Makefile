SHELL := /bin/bash

IMAGE_BASE  := nikitany/transit-api
BRANCH_NAME := $(shell git rev-parse --abbrev-ref HEAD | sed 's/[^a-zA-Z0-9\-\.]/-/g')
COMMIT_HASH := $(shell git log -1 --format=format:"%H" | cut -c 1-8)
IMAGE_TAG   := $(IMAGE_BASE):$(BRANCH_NAME)-$(COMMIT_HASH)
LATEST_TAG  := $(IMAGE_BASE):latest

.PHONY: build
build:
	docker build -t $(IMAGE_TAG) -t $(LATEST_TAG) .

.PHONY: run
run: build
	docker run --rm -d -p 8000:5000 $(LATEST_TAG)

.PHONY: deploy
deploy: build
	kubectl apply -f deployment.yaml
