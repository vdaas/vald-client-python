#
# Copyright (C) 2019 kpango (Yusuke Kato)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
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

VALD_SHA    = VALD_SHA
VALD_CLIENT_PYTHON_VERSION = VALD_CLIENT_PYTHON_VERSION

PROTO_ROOT  = vald/apis/proto
PB2DIR_ROOT = src
SHADOW_ROOT = proto
SHADOW_ROOT_VALD = $(SHADOW_ROOT)/vald
SHADOW_ROOT_VALIDATE = $(SHADOW_ROOT)/validate

PROTOS.vald.proto = vald/vald.proto
PROTOS.agent.proto = agent/agent.proto
PROTOS.payload.proto = payload/payload.proto
PROTOS      = $(PROTOS.vald.proto) $(PROTOS.agent.proto) $(PROTOS.payload.proto)
PROTOS     := $(PROTOS:%=$(PROTO_ROOT)/%)
SHADOWS     = $(notdir $(PROTOS))
SHADOWS    := $(SHADOWS:%=$(SHADOW_ROOT_VALD)/%)
PB2PYS      = $(SHADOWS:$(SHADOW_ROOT_VALD)/%.proto=$(PB2DIR_ROOT)/%_pb2.py)
SHADOW_VALIDATE := $(SHADOW_ROOT_VALIDATE)/validate.proto
PB2PY_VALIDATE = $(PB2DIR_ROOT)/validate/validate_pb2.py

PROTODIRS   = $(shell find $(PROTO_ROOT) -type d | sed -e "s%$(PROTO_ROOT)/%%g" | grep -v "$(PROTO_ROOT)")

PROTO_PATHS = \
	$(SHADOW_ROOT) \
	$(SHADOW_ROOT_VALD) \
	$(SHADOW_ROOT_VALIDATE) \
	$(GOPATH)/src/github.com/protocolbuffers/protobuf/src \
	$(GOPATH)/src/github.com/gogo/protobuf/protobuf \
	$(GOPATH)/src/github.com/googleapis/googleapis

MAKELISTS   = Makefile

red    = /bin/echo -e "\x1b[31m\#\# $1\x1b[0m"
green  = /bin/echo -e "\x1b[32m\#\# $1\x1b[0m"
yellow = /bin/echo -e "\x1b[33m\#\# $1\x1b[0m"
blue   = /bin/echo -e "\x1b[34m\#\# $1\x1b[0m"
pink   = /bin/echo -e "\x1b[35m\#\# $1\x1b[0m"
cyan   = /bin/echo -e "\x1b[36m\#\# $1\x1b[0m"

define go-get
	GO111MODULE=off go get -u $1
endef

define mkdir
	mkdir -p $1
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

.PHONY: proto
## build proto
proto: $(PB2PYS) $(PB2PY_VALIDATE)

$(PB2DIR_ROOT):
	$(call mkdir, $@)
	$(call rm, -rf, $@/*)

$(SHADOW_ROOT_VALD):
	$(call mkdir, $@)
	$(call rm, -rf, $@/*)

$(SHADOW_ROOT_VALIDATE):
	$(call mkdir, $@)
	$(call rm, -rf, $@/*)

$(SHADOWS): vald $(SHADOW_ROOT_VALD)
	cp $(PROTO_ROOT)/$(PROTOS.$(notdir $@)) $@
	sed -i -e '/^.*gql\.proto.*$$\|^.*gql\..*_type.*$$/d' $@
	sed -i -e 's:^import "payload.proto";$$:import "vald/payload.proto";:' $@

$(SHADOW_VALIDATE): proto/deps $(SHADOW_ROOT_VALIDATE)
	cp $(GOPATH)/src/github.com/envoyproxy/protoc-gen-validate/validate/validate.proto $(SHADOW_VALIDATE)

$(PB2PYS): proto/deps $(PB2DIR_ROOT) $(SHADOWS) $(SHADOW_VALIDATE)
	@$(call green, "generating pb2.py files...")
	python \
		-m grpc_tools.protoc \
		$(PROTO_PATHS:%=-I %) \
		--python_out=$(PB2DIR_ROOT) \
		--grpc_python_out=$(PB2DIR_ROOT) \
		$(SHADOW_ROOT_VALD)/*.proto

$(PB2PY_VALIDATE): $(SHADOW_VALIDATE)
	@$(call green, "generating pb2.py files...")
	python \
		-m grpc_tools.protoc \
		$(PROTO_PATHS:%=-I %) \
		--python_out=$(PB2DIR_ROOT) \
		--grpc_python_out=$(PB2DIR_ROOT) \
		$(SHADOW_VALIDATE)

vald:
	git clone --depth 1 https://$(VALDREPO) vald

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
	echo "$(shell cat vald/versions/VALD_VERSION).$(shell cat $(VALD_SHA))" | sed -e 's/^v//' | tr -d '\n' > $(VALD_CLIENT_PYTHON_VERSION)

.PHONY: proto/deps
## install proto deps
proto/deps: \
	$(GOPATH)/bin/protoc-gen-doc \
	$(GOPATH)/bin/protoc-gen-go \
	$(GOPATH)/bin/protoc-gen-gogo \
	$(GOPATH)/bin/protoc-gen-gofast \
	$(GOPATH)/bin/protoc-gen-gogofast \
	$(GOPATH)/bin/protoc-gen-gogofaster \
	$(GOPATH)/bin/protoc-gen-gogoslick \
	$(GOPATH)/bin/protoc-gen-grpc-gateway \
	$(GOPATH)/bin/protoc-gen-swagger \
	$(GOPATH)/bin/protoc-gen-validate \
	$(GOPATH)/bin/prototool \
	$(GOPATH)/bin/swagger \
	$(GOPATH)/src/google.golang.org/genproto \
	$(GOPATH)/src/github.com/protocolbuffers/protobuf \
	$(GOPATH)/src/github.com/googleapis/googleapis

$(GOPATH)/src/github.com/protocolbuffers/protobuf:
	git clone \
		--depth 1 \
		https://github.com/protocolbuffers/protobuf \
		$(GOPATH)/src/github.com/protocolbuffers/protobuf

$(GOPATH)/src/github.com/googleapis/googleapis:
	git clone \
		--depth 1 \
		https://github.com/googleapis/googleapis \
		$(GOPATH)/src/github.com/googleapis/googleapis

$(GOPATH)/src/google.golang.org/genproto:
	$(call go-get, google.golang.org/genproto/...)

$(GOPATH)/bin/protoc-gen-go:
	$(call go-get, github.com/golang/protobuf/protoc-gen-go)

$(GOPATH)/bin/protoc-gen-gogo:
	$(call go-get, github.com/gogo/protobuf/protoc-gen-gogo)

$(GOPATH)/bin/protoc-gen-gofast:
	$(call go-get, github.com/gogo/protobuf/protoc-gen-gofast)

$(GOPATH)/bin/protoc-gen-gogofast:
	$(call go-get, github.com/gogo/protobuf/protoc-gen-gogofast)

$(GOPATH)/bin/protoc-gen-gogofaster:
	$(call go-get, github.com/gogo/protobuf/protoc-gen-gogofaster)

$(GOPATH)/bin/protoc-gen-gogoslick:
	$(call go-get, github.com/gogo/protobuf/protoc-gen-gogoslick)

$(GOPATH)/bin/protoc-gen-grpc-gateway:
	$(call go-get, github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway)

$(GOPATH)/bin/protoc-gen-swagger:
	$(call go-get, github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger)

$(GOPATH)/bin/protoc-gen-validate:
	$(call go-get, github.com/envoyproxy/protoc-gen-validate)

$(GOPATH)/bin/prototool:
	$(call go-get, github.com/uber/prototool/cmd/prototool)

$(GOPATH)/bin/protoc-gen-doc:
	$(call go-get, github.com/pseudomuto/protoc-gen-doc/cmd/protoc-gen-doc)

$(GOPATH)/bin/swagger:
	$(call go-get, github.com/go-swagger/go-swagger/cmd/swagger)
