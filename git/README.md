# Git Hooks

These hooks are intended to increase the readability and consistency of the code committed to this repository. We follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style standards for python.


## Setting up a pre-commit hook

1) Add code-quality repo as submodule

From the top level of your repo:

```shell
git submodule add git@github.com:ftb-dataengineering/code-quality.git
```

Note: This assumes you have ssh keys setup, if this does not work, you can try the following:

```shell
git submodule add https://github.com/ftb-dataengineering/code-quality.git
```

2) Run setup script
IMPORTANT: run this script from the top-level of your repo (the repo you want to add the pre-commit hook to)!

```shell
code-quality/git/setup_precommit_hook.sh
```


## Pylint Usage

Before committing code [Pylint](http://www.pylint.org) can be used to check for non-convential code errors. Otherwise, a report will be generated upon usage of `git commit`.

```shell
pylint sample_script.py
```

Settings for Pylint are stored in `pylintrc` and relevant changes are welcome.


## ToDo

- Make setup script more robust to directory structure

