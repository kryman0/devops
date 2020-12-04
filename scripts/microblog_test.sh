#! /bin/bash

set -eu

source .venv/bin/activate

make test-for-docker

bandit -c .bandit.yml -r tests/