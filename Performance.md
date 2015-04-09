# Data Engineering Code Performance

This README focuses specifically on the __performance__ of your script, job, or transformation.

The topics in this section are critical components of our code review; focusing on speed, modularity, and maintainability. Many of these concepts have been directly ported from [Python.org's Performance Tipcs](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)


## Loops:<a name="loops"></a>

Example: Loop over a list of words and convert them to upper case

```python
# bad
newlist = []
for word in oldlist:
  newlist.append(word.upper())

# instead, use map to push the loop from the interpreter into compiled C code
newlist = map(str.upper, oldlist)
```

### List comprehensions
...are also a good alternative which provide a syntactically more compact and more efficient way of writing the same code:

```python
newlist = [s.upper() for s in oldlist]
```

### Generator expressions
...function more-or-less like list comprehensions or `map` but avoid the overhead of generating the entire list at once. Instead, they return a generator object which can be iterated over bit-by-bit.

```python
iterator = (s.upper() for s in oldlist)
```


## Initializing Dictionary Elements:<a name="dictionaries"></a>

Suppose you are building a dictionary of word frequencies and you've already broken your text up into a list of words. You might execute something like:

```python
wdict = {}
for word in words:
  if word not in wdict:
    wdict[word] = 0
  wdict[word] += 1
```

Except for the first time, each time a word is seen the if statement's test fails. If you are counting a large number of words, many will probably occur multiple times. In a situation where the initialization of a value is only going to occur once and the augmentation of that value will occur many times it is cheaper to use a try statement:

```python
wdict = {}
for word in words:
  try:
    wdict[word] += 1
  except KeyError:
    wdict[word] = 1
```

However, a third alternative became available with the release of Python 2.x. Dictionaries now have a get() method which will return a default value if the desired key isn't found in the dictionary. This simplifies the loop:

```python
wdict = {}
get = wdict.get
for word in words:
  wdict[word] = get(word, 0) + 1
```


## Data Aggregation<a name="data_aggregation"></a>

Function call overhead in Python is relatively high, especially compared with the execution speed of a builtin function. This strongly suggests that where appropriate, functions should handle data aggregates. Here's a contrived example written in Python.

```python
# not as good
import time
x = 0
def doit1(i):
    global x
    x = x + i

list = range(100000)
t = time.time()
for i in list:
    doit1(i)

print "%.3f" % (time.time()-t)
>>> 0.758

# vs ~4x faster
import time
x = 0
def doit2(list):
    global x
    for i in list:
        x = x + i

list = range(100000)
t = time.time()
doit2(list)
print "%.3f" % (time.time()-t)
>>> 0.204
```

## Pythonic Idioms<a name="idioms"></a>

### Tuples

#### Swapping Variables

```python
# instead of
temp = a
a = b
b = temp

# use
a, b = b, a
```

### Iterating over structured data

```python
#instead of
points = [(1, 2), (3, 1), (4, 6)]
for point in points:
  x = point[0]
  y = point[1]
  # do something

# use
points = [(1, 2), (3, 1), (4, 6)]
for x, y in points:
  # do something
```

### Formatting

Use string replacement or `.format()` syntax

```python
name = '%s %s' % ('Jesse', 'Adametz')  # string replacement
greeting = 'Hi, my name is {}'.format(name) # .format()
```

## Loops and Sequences

### Filtering a list

Suppose you want the reflections of all points underneath the line `y = x`

```python
# instead of
points = [(1, 2), (2, 1), (3, 5), (4, 2)]
reflect_under = []
for x, y in points:
  if x < y:
    reflect_under.append((y, x))

# use
points = [(1, 2), (2, 1), (3, 5), (4, 2)]
reflect_under = [(y, x) for x, y in points if x < y]
```

### Iterating over a list

Going backwards

```python
for datum in reversed(data):
  # do something
```

You sometimes need acces to index AND the element:

```python
# instead of
names = 'alice bob clarence dean'.split()
for i in range(len(names)):
  print 'Name {} is {}\n'.format(i, names[i])

# use
for i, name in enumerate(names):
  print 'Name {} is {}\n'.format(i, name)
