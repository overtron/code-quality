# Data Engineering Code Styling

This README focuses specifically on the __styling__ of your script, job, or transformation.

## Python Code Styling

When writing Python scripts we rely on the [PEP 8 - Style Guide for Python](https://www.python.org/dev/peps/pep-0008/) as well as [Google's Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html).

## Minimum Expectations:

### Imports: should always be as specific as possible<a name="imports"></a>
```python
"""
Never, ever:
from x import *
"""
import x  # for importing packages and modules
from x import y  # where x is the package prefix and y is the module name with no prefix
from x import y as z  # if two modules named y are to be imported or if y is a long name.

# imports should be on separate lines
# Yes:
import os
import sys

# No:
import os, sys
```

---

#### Naming: should be easily readable and descriptive<a name="naming"></a>

_Ported directly from Google's Python Style Guide_

|Type|Public|Internal|
|----|------|--------|
|Packages|`lower_with_under`||
|Modules|`lower_with_under`|`_lower_with_under`|
|Classes|`CapWords`|`_CapWords`|
|Exceptions|`CapWords`||
|Functions|`lower_with_under()`|`_lower_with_under()`|
|Global/Class Constants|`CAPS_WITH_UNDER`|`_CAPS_WITH_UNDER`|
|Global/Class Variables|`lower_with_unders`|`_lower_with_under`|
|Instance Variables|`lower_with_under`|`_lower_with_under` (protected) or `__lower_with_under` (private)|
|Method Names|`lower_with_under()`|`_lower_with_under()` (protected) or `__lower_with_under()` (private)|
|Function/Method Parameters|`lower_with_under`||
|Local Variables|`lower_with_under`||

__Avoid__:

* single character names except for counters or iterators
* dashes (-) in any package/module name
* `__double_leading_and_trailing_underscore__` names (reserved by Python)
