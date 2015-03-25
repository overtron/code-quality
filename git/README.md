# Git Hooks

These hooks are intended to increase the readability and consistency of the code committed to this repository.

## Initial Setup

After pulling the repository for the first time:
```shell
sudo pip install -r requirements.txt
cd ../.git/hooks/ && ln -s ../../git/pre-commit.py pre-commit
```

## Pylint Usage

Before committing code [Pylint](http://www.pylint.org) can be used to check for non-convential code errors. Otherwise, a report will be generated upon usage of `git commit`.

```shell
pylint sample_script.py
```

Settings for Pylint are stored in `pylintrc` and relevant changes are welcome.
