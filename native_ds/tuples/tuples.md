# Tuples

Tuple is another data structure in Python that stores values.
- Tuples are immutable (cannot be changed).
- A Tuple is defined using `()` or using `tuple()`
- Like lists, tuples can also be concatenated,stores data of multi types and its values can be accessed through index.

```
a = (1,4,6,13,23)
print(type(a))
```

Note - If you try to create a tuple with single value, and try to check the type of data, it will return `int` instead of `tuple`.

Because, parentheses are also used for mathematical operations, so values like (12) will just be considered as 12 instead of (12)
- To defined a tuple with single value, always add a comma after the value.

```
b = (23,)
print(type(b)) # data type is tuple
```

# Concatenation of Tuples

- You can combine two or more tuples into a single tuple.

```
c = (23,53,15,64)
d = (54,13,74,12)
print(c + d)
```

# Slicing Tuples

- Slicing basically means accessing a part of data structure, you have already done this for list.

```
e = (34,12,51,32,64,13)
print(e[2:5])
```

# Deleting Tuples

- Just like list you can delete tuples using `del` keyword

```
f = (34,2,1,53,12)
del f
```