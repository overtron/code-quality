#!/bin/sh

GIT_ROOT=$(git rev-parse --show-toplevel)
SRC=code-quality/git

# install all pre-reqs
sudo pip install -r ${SRC}/requirements.txt

# setup precommit hook by linking the pre-commit script to the git hooks directory
cd ${GIT_ROOT}/.git/hooks/ && ln -s $(pwd)/${SRC}/pre-commit.py pre-commit
