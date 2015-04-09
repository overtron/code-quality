# Data Engineering Code Quality

This repository is focused on providing the information and tools necessary to write high quality Python and well documented [Kettle](http://community.pentaho.com/projects/data-integration/) Jobs & Transformations.

* Read more on Code Styling, [here](CodeStyling.md).
* Read more on Code Performance, [here](Performance.md).

## Setup

To setup the tools in this repository, please refer to [git/README.md](git/README.md)


## Python Review Guidelines

__Contents:__

* [Main](#main)
* [Comments](#comments)
* [Input Defense](#input_defense)
* [Loops](#loops)
* [Duplicate Code](#dupe_code)
* [Idiomatic Alternatives](#idioms)
* [Commit Messages](#commit_messages)
* [Commented Source Code](#commented)

The bullets outlined below are minimal suggestions of what to look for when embarking on code review. They are meant to be interpreted on a case-by-case basis specific to the code you are reviewing and should take in to account your best judgement.

### Main: should allow your script to be importable without execution<a name="main"></a>

```python
def foo():
  ...

if __name__ == '__main__':
  foo()
```


### Comments: should convey intent of code<a name="comments"></a>

Comments about _why_ the developer did something unusual are the most critical comments to look for. Comments like; `MySQLdb returns long, typecasting to int first` helps the reader understand the developers decision. Additionally, to catch bugs during code review, it's important to know what the code is supposed to do. Thus, when reading, you can compare actuality and intent.

[Read more about Comment styling.](CodeStyling.md/#)


### Input Defense: handling and guarding against bad input<a name="input_defense"></a>

There are two main things to look for:

1. Confirm that input from the end user is scrubbed and encoded.
* Confirm that functions are defended from bad inputs that come from external sources.

```python
# defense example
def foo(int_param):
  if not isinstance(int_param, int):
    try:
      int_param = int(int_param)
    except ValueError:
      return False
  return True
```

### Loops: should be concise and performant<a name="loops"></a>

Loops should be checked for length, appropriate exit criteria, and speed. Loops with many objects may be considerably slower than loops with very few local variables; faster alternatives should always be considered.

Things like incorrect indenting or incorrect boundary conditions for loop exit are usual errors and are bugs that should be caught early on.

[Read more about Loop performance.](Performance.md/#loops)

### Duplicate Code: should be avoided<a name="dupe_code"></a>

Look for code doing similar things; this is an opportunity for refactoring and/or removing duplication. Consider that code doing similar things needs more maintenance, so when an input type changes, multiple places will need to change as well.

### Idiomatic Alternatives<a name="idioms"></a>

Look for code that can be replaced with Python idioms. Sometimes these idioms are more performant and generally makes code more readable.

[Read more about Python idioms](Performance.md/#idioms)

### Commit Messages: should clearly state the Project and what you did to it<a name="commit_messages"></a>

Clearly written commit messages let us go back and find the point where something was changed. It takes longer to find the source of a bug if messages are poorly written.

```sh
git commit -m "Project: debugged issue with foo(). Tests pass."
```

### Commented Source Code: should be deleted<a name="commented"></a>

If code is commented out, it should be deleted. Leaving commented code in-place decreases readability. Utilize source control to re-introduce code that was previously removed.
