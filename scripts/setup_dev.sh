#!/bin/bash

### Bash Options
set -o errexit
set -o nounset
set -o pipefail


### Configuration
PROJECT_NAME="modeliter"
PYTHON_VENV_NAME=".venv"


### Operations

printf "1. Creating your Python virtual environment in \`$PYTHON_VENV_NAME\`... "
python -m venv $PYTHON_VENV_NAME &> /dev/null
printf "Done.\n\n"

printf "2. Activating your virtual environment... "
source $PYTHON_VENV_NAME/bin/activate &> /dev/null
printf "Done.\n\n"

printf "3. Upgrading \`pip\` and installing Python dependencies... "
pip install --upgrade pip &> /dev/null
printf "Done.\n\n"

printf "4. Installing Python dependencies... "
pip install --requirement requirements.txt &> /dev/null
printf "Done.\n\n"

printf "5. Installing \`$PROJECT_NAME\` in editable mode... "
pip install --editable . &> /dev/null
printf "Done.\n\n"

printf "6. Deactivating your virtual environment... "
deactivate &> /dev/null
printf "Done.\n\n"

printf "Finished your development setup! Run the following:\n\n"
printf "\tsource $PYTHON_VENV_NAME/bin/activate\n\n"
printf "to activate your virtual environment and begin development on $PROJECT_NAME!\n"
