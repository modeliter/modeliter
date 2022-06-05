#!/bin/bash

### Bash Options
set -o errexit
set -o nounset
set -o pipefail


### Configuration
PROJECT_NAME="modeliter"


### Operations
uvicorn $PROJECT_NAME.http:create_app --factory --reload
