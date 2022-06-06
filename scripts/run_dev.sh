#!/bin/bash

### Bash Options
set -o errexit
set -o nounset
set -o pipefail


### Operations
uvicorn modeliter.httpserver:create_app --factory --reload
