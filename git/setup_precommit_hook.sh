#!/bin/sh

# install all pre-reqs
sudo pip install -r requirements.txt

# setup precommit hook by linking the pre-commit script to the git hooks directory
cd ../.git/hooks/ && ln -s ../../git/pre-commit.py pre-commit
