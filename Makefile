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

PYTHON = python

VALD_DIR    = vald-origin
VALD_SHA    = VALD_SHA
VALD_CLIENT_PYTHON_VERSION = VALD_CLIENT_PYTHON_VERSION

PWD    := $(eval PWD := $(shell pwd))$(PWD)
GOPATH := $(eval GOPATH := $(shell go env GOPATH))$(GOPATH)

PROTO_ROOT  = $(VALD_DIR)/apis/proto
PB2DIR_ROOT = src

SHADOW_ROOT = vald

PROTOS = \
	gateway/vald/vald.proto \
	agent/core/agent.proto \
	payload/payload.proto \
	v1/agent/core/agent.proto \
	v1/gateway/vald/vald.proto \
	v1/vald/filter.proto \
	v1/vald/insert.proto \
	v1/vald/object.proto \
	v1/vald/remove.proto \
	v1/vald/search.proto \
	v1/vald/update.proto \
	v1/vald/upsert.proto \
	v1/payload/payload.proto
PROTOS := $(PROTOS:%=$(PROTO_ROOT)/%)
SHADOWS = $(PROTOS:$(PROTO_ROOT)/%.proto=$(SHADOW_ROOT)/%.proto)
PB2PYS  = $(PROTOS:$(PROTO_ROOT)/%.proto=$(PB2DIR_ROOT)/$(SHADOW_ROOT)/%_pb2.py)
PB2PY_VALIDATE = $(PB2DIR_ROOT)/validate/validate_pb2.py

PROTO_PATHS = \
	$(PWD) \
	$(PWD)/$(VALD_DIR) \
	$(PWD)/$(PROTO_ROOT) \
	$(GOPATH)/src \
	$(GOPATH)/src/github.com/googleapis/googleapis \
	$(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate

MAKELISTS = Makefile

red    = /bin/echo -e "\x1b[31m\#\# $1\x1b[0m"
green  = /bin/echo -e "\x1b[32m\#\# $1\x1b[0m"
yellow = /bin/echo -e "\x1b[33m\#\# $1\x1b[0m"
blue   = /bin/echo -e "\x1b[34m\#\# $1\x1b[0m"
pink   = /bin/echo -e "\x1b[35m\#\# $1\x1b[0m"
cyan   = /bin/echo -e "\x1b[36m\#\# $1\x1b[0m"

define go-get
	GO111MODULE=on go get -u $1
endef

define go-get-no-mod
	GO111MODULE=off go get -u $1
endef

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
	rm -rf $(PB2DIR_ROOT)
	rm -rf $(SHADOW_ROOT)
	rm -rf $(VALD_DIR)

.PHONY: proto
## build proto
proto: \
	$(PB2PYS) \
	$(PB2PY_VALIDATE)

$(PROTOS): $(VALD_DIR)
$(SHADOWS): $(PROTOS)
$(SHADOW_ROOT)/%.proto: $(PROTO_ROOT)/%.proto
	mkdir -p $(dir $@)
	cp $< $@
	sed -i -e 's:^import "apis/proto/:import "$(SHADOW_ROOT)/:' $@
	sed -i -e 's:^import "github.com/envoyproxy/protoc-gen-validate/:import ":' $@

$(PB2DIR_ROOT):
	mkdir -p $@

$(PB2PYS): proto/deps $(PB2DIR_ROOT) $(SHADOWS)
$(PB2DIR_ROOT)/$(SHADOW_ROOT)/%_pb2.py: $(SHADOW_ROOT)/%.proto
	@$(call green, "generating pb2.py files...")
	$(PYTHON) \
		-m grpc_tools.protoc \
		$(PROTO_PATHS:%=-I %) \
		--python_out=$(PWD)/$(PB2DIR_ROOT) \
		--grpc_python_out=$(PWD)/$(PB2DIR_ROOT) \
		$<

$(PB2PY_VALIDATE): $(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate
	@$(call green, "generating pb2.py files...")
	(cd $(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate; \
		$(PYTHON) \
			-m grpc_tools.protoc \
			$(PROTO_PATHS:%=-I %) \
			-I $(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate \
			--python_out=$(PWD)/$(PB2DIR_ROOT) \
			--grpc_python_out=$(PWD)/$(PB2DIR_ROOT) \
			validate/validate.proto)

$(VALD_DIR):
	git clone --depth 1 https://$(VALDREPO) $(VALD_DIR)

.PHONY: vald/sha/print
## print VALD_SHA value
vald/sha/print:
	@cat $(VALD_SHA)

.PHONY: vald/sha/update
## update VALD_SHA value
vald/sha/update: vald
	(cd vald; git rev-parse HEAD | tr -d '\n' > ../$(VALD_SHA))

.PHONY: vald/client/python/version/print
## print VALD_CLIENT_PYTHON_VERSION value
vald/client/python/version/print:
	@cat $(VALD_CLIENT_PYTHON_VERSION)

.PHONY: vald/client/python/version/update
## update VALD_CLIENT_PYTHON_VERSION value
vald/client/python/version/update: vald
	(vald_version=`cat $(VALD_DIR)/versions/VALD_VERSION | sed -e 's/^v//'`; \
	    client_version=`cat $(VALD_CLIENT_PYTHON_VERSION)`; \
	    major=$${client_version%%.*}; client_version="$${client_version#*.}"; \
	    minor=$${client_version%%.*}; client_version="$${client_version#*.}"; \
	    patch=$${client_version%%.*}; client_version="$${client_version#*.}"; \
	    if [ "$${vald_version}" = "$${major}.$${minor}.$${patch}" ]; then \
	        if [ "$${patch}" = "$${client_version}" ]; then \
	            new_version="$${major}.$${minor}.$${patch}.post1"; \
	        else \
	            rev="$${client_version#post}"; \
	            rev=$$((rev+1)); \
	            new_version="$${major}.$${minor}.$${patch}.post$${rev}"; \
	        fi; \
	    else \
	        new_version="$${vald_version}"; \
	    fi; \
	    echo "VALD_VERSION: $${vald_version}, NEW_CLIENT_VERSION: $${new_version}"; \
	    echo "$${new_version}" > VALD_CLIENT_PYTHON_VERSION)
	sed -i -e "s/^version = .*\$$/version = `cat VALD_CLIENT_PYTHON_VERSION`/" setup.cfg

.PHONY: proto/deps
## install proto deps
proto/deps: \
	$(GOPATH)/src/github.com/googleapis/googleapis \
	$(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate

$(GOPATH)/src/github.com/googleapis/googleapis:
	git clone \
		--depth 1 \
		https://github.com/googleapis/googleapis \
		$(GOPATH)/src/github.com/googleapis/googleapis

$(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate:
	git clone \
		--depth 1 \
		https://github.com/envoyproxy/protoc-gen-validate \
		$(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate
