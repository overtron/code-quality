# Data Engineering Code Quality

This repository is focused on providing the information and tools necessary to write high quality Python and well documented [Kettle](http://community.pentaho.com/projects/data-integration/) Jobs & Transformations.

Read more on Code Styling, [here](https://github.com/ftb-dataengineering/code-quality/blob/master/CodeStyling.md).

## Setup

To setup the tools in this repository, please refer to [git/README.md](https://github.com/ftb-dataengineering/code-quality/blob/master/git/README.md)


## Python Review Guidelines

__Contents:__

* [Minimum Expectations](#min_expectations)
  * [Main](#main)
  * [Comments](#comments)
  * [Duplicate Code](#dupe_code)
* [Advanced Code Review](#adv_code_review)


## Minimum Expectations<a name="min_expectations"></a>:

The topics in this section are critical components of our code review; focusing on speed, modularity, and maintainability. Many of these concepts have been directly ported from [Python.org's Performance Tipcs](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)


### Main: should allow your script to be importable without execution<a name="main"></a>
```python
def foo():
  ...

if __name__ == '__main__':
  foo()
```


---


### Comments: should convey intent of code<a name="comments"></a>


__Docstrings:__ can be used as the first statement in any package, module, class or function.
```python
def foo_bar(param1, param2, param3=None):
  """
  Brief description of what this method is doing.
  :param param1: some string
  :param param2: some int
  :param param3: some optional param
  :return: thing returned by foo_bar
  """
```

According to [Google's Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html), a docstring should exist unless the following criteria are __all__ met:

* not externally visible
* very short
* obvious

__Block and inline comments:__

* should be used for "tricky" parts of the code.
* _"If you're going to have to explain it at the next code review, you should comment it now."_
* Complicated operations get a few lines of comments before the operations commence.
* Non-obvious ones get comments at the end of the line.

```python
# Some lines describing what you're trying to do
# This is different than describing the code
# You should assume the person reading your code can read Python

if i & (i - 1) == 0:  # true iff i is a power of 2
```


---


### Duplicate Code: should be avoided at all costs and made into modular methods<a name="dupe_code"></a>


___TODO: THIS NEEDS AN EXAMPLE___


---


### Defending Against Input: keeps things accurate and safe<a name="input_defense"></a>

___TODO: THIS NEEDS AN EXAMPLE___


## Advanced Code Review<a name="adv_code_review"></a>

___TODO: ALL OF THIS___
