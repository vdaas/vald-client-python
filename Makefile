#
# Copyright (C) 2019-2020 Vdaas.org Vald team ( kpango, rinx, kmrmt )
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

REPO       ?= vdaas
NAME        = vald
VALDREPO    = github.com/$(REPO)/$(NAME)
LANGUAGE    = python
PKGNAME     = $(NAME)-client-$(LANGUAGE)
PKGREPO     = github.com/$(REPO)/$(PKGNAME)

VALD_DIR    = vald-origin
VALD_SHA    = VALD_SHA
VALD_CLIENT_PYTHON_VERSION = VALD_CLIENT_PYTHON_VERSION
VALD_CHECKOUT_REF ?= main

BINDIR ?= /usr/local/bin

PROTO_ROOT  = $(VALD_DIR)/apis/proto
PB2DIR_ROOT = src

BUF_VERSION_URL := https://raw.githubusercontent.com/vdaas/vald/main/versions/BUF_VERSION
BUF_CONFIGS = \
	$(PROTO_ROOT)/buf.yaml \
	$(PROTO_ROOT)/buf.lock

SHADOW_ROOT       = vald
SHADOW_PROTO_ROOT = $(SHADOW_ROOT)/$(SHADOW_ROOT)

PROTOS = \
	v1/agent/core/agent.proto \
	v1/filter/egress/egress_filter.proto \
	v1/filter/ingress/ingress_filter.proto \
	v1/vald/filter.proto \
	v1/vald/insert.proto \
	v1/vald/object.proto \
	v1/vald/remove.proto \
	v1/vald/search.proto \
	v1/vald/update.proto \
	v1/vald/upsert.proto \
	v1/payload/payload.proto
PROTOS := $(PROTOS:%=$(PROTO_ROOT)/%)
SHADOWS = $(PROTOS:$(PROTO_ROOT)/%.proto=$(SHADOW_PROTO_ROOT)/%.proto)
PB2PYS  = $(PROTOS:$(PROTO_ROOT)/%.proto=$(PB2DIR_ROOT)/$(SHADOW_ROOT)/%_pb2.py)

MAKELISTS = Makefile

PYTHON_VERSION := $(eval PYTHON_VERSION := $(shell cat PYTHON_VERSION))$(PYTHON_VERSION)
TEST_DATASET_PATH = wordvecs1000.json

red    = /bin/echo -e "\x1b[31m\#\# $1\x1b[0m"
green  = /bin/echo -e "\x1b[32m\#\# $1\x1b[0m"
yellow = /bin/echo -e "\x1b[33m\#\# $1\x1b[0m"
blue   = /bin/echo -e "\x1b[34m\#\# $1\x1b[0m"
pink   = /bin/echo -e "\x1b[35m\#\# $1\x1b[0m"
cyan   = /bin/echo -e "\x1b[36m\#\# $1\x1b[0m"

.PHONY: all
## execute clean and proto
all: clean proto

.PHONY: help
## print all available commands
help:
	@awk '/^[a-zA-Z_0-9%:\\\/-]+:/ { \
	  helpMessage = match(lastLine, /^## (.*)/); \
	  if (helpMessage) { \
	    helpCommand = $$1; \
	    helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
      gsub("\\\\", "", helpCommand); \
      gsub(":+$$", "", helpCommand); \
	    printf "  \x1b[32;01m%-35s\x1b[0m %s\n", helpCommand, helpMessage; \
	  } \
	} \
	{ lastLine = $$0 }' $(MAKELISTS) | sort -u
	@printf "\n"

.PHONY: clean
## clean
clean:
	rm -rf $(PB2DIR_ROOT)/google $(PB2DIR_ROOT)/vald $(PB2DIR_ROOT)/buf
	rm -rf $(SHADOW_ROOT)
	rm -rf $(VALD_DIR)

.PHONY: proto
## build proto
proto: $(PB2PYS)
	@$(call green, "generating pb2.py files...")
	cp -f $(BUF_CONFIGS) $(SHADOW_ROOT)
	buf generate --include-imports

$(PROTOS): $(VALD_DIR)
$(SHADOWS): $(PROTOS)
$(SHADOW_PROTO_ROOT)/%.proto: $(PROTO_ROOT)/%.proto
	mkdir -p $(dir $@)
	cp $< $@
	sed -i -e 's:^import "v1:import "$(SHADOW_ROOT)/v1:' $@

$(PB2DIR_ROOT):
	mkdir -p $@

$(PB2PYS): proto/deps $(PB2DIR_ROOT) $(SHADOWS)

$(VALD_DIR):
	git clone https://$(VALDREPO) $(VALD_DIR)

.PHONY: vald/clone
## clone vald repository
vald/clone: $(VALD_DIR)

.PHONY: vald/checkout
## checkout vald repository
vald/checkout: $(VALD_DIR)
	cd $(VALD_DIR) && git checkout $(VALD_CHECKOUT_REF)

.PHONY: vald/origin/sha/print
## print origin VALD_SHA value
vald/origin/sha/print: $(VALD_DIR)
	@cd $(VALD_DIR) && git rev-parse HEAD | tr -d '\n'

.PHONY: vald/sha/print
## print VALD_SHA value
vald/sha/print:
	@cat $(VALD_SHA)

.PHONY: vald/sha/update
## update VALD_SHA value
vald/sha/update: $(VALD_DIR)
	(cd $(VALD_DIR); git rev-parse HEAD | tr -d '\n' > ../$(VALD_SHA))

.PHONY: vald/client/version/print
## print VALD_CLIENT_PYTHON_VERSION value
vald/client/version/print:
	@cat $(VALD_CLIENT_PYTHON_VERSION)

.PHONY: vald/client/version/update
## update VALD_CLIENT_PYTHON_VERSION value
vald/client/version/update: $(VALD_DIR)
	(vald_version=`cat $(VALD_DIR)/versions/VALD_VERSION | sed -e 's/^v//'`; \
	    echo "VALD_VERSION: $${vald_version}"; \
	    echo "$${vald_version}" > VALD_CLIENT_PYTHON_VERSION)
	sed -i -e "s/^version = .*\$$/version = `cat VALD_CLIENT_PYTHON_VERSION`/" setup.cfg

.PHONY: proto/deps
## install proto deps
proto/deps: buf/install

.PHONY: buf/install
## install buf command.
buf/install: $(BINDIR)/buf

$(BINDIR)/buf:
	@version=$$(curl -sSL $(BUF_VERSION_URL)); \
	curl -sSL \
	"https://github.com/bufbuild/buf/releases/download/$$version/buf-$(shell uname -s)-$(shell uname -m)" \
	-o "${BINDIR}/buf" && \
	chmod +x "${BINDIR}/buf"

.PHONY: ci/deps/install
## install deps for CI environment
ci/deps/install:
	sudo apt-get update -y && sudo apt-get install -y \
		python3-setuptools \
		libprotobuf-dev \
		libprotoc-dev \
		protobuf-compiler
	pip3 install grpcio-tools

.PHONY: ci/test
## Execute test for CI environment
ci/test: $(TEST_DATASET_PATH)
	python src/test.py

$(TEST_DATASET_PATH):
	curl -L https://raw.githubusercontent.com/rinx/word2vecjson/master/data/wordvecs1000.json -o $(TEST_DATASET_PATH)

.PHONY: ci/package/prepare
## prepare package to publish
ci/package/prepare:
	python3 setup.py sdist
	python3 setup.py bdist_wheel

.PHONY: version/python
## Print Python version
version/python:
	@echo $(PYTHON_VERSION)
