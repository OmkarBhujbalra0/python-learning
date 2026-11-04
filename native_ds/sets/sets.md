# Sets

Sets are another data structure in Python that stores only unique values.
- You have seen the concept of sets in mathematics, just like that, sets in Python also deals with operations like Intersection, Union, etc.
- Sets are mutable, it can be modified.
- An empty set is defined using set() function.
- You can also create set with multiple values in it using `{}`
- If you try to define an empty set using only {}, it will create a dictionary instead of set.

```
a = set()
print(type(a))

b = {23,51,21,53,52}
print(b)
```
- If you try to create a set with duplicate values, it will only consider the first occurence.

```
c = {23,25,24,25,23}
print(c)
```
- Sets are unordered, unlike lists and tuples you cannot access values from set using indexing.

```
d = {23,25,24,25,23}
print(d[0]) # Sets are unordered, meaning accessing through indexing will return error.
```

The following are the operations that could be performed on Sets:

1. Adding values to the set:
- You can add values to the set using add() function.

```
e = {2,5,12}
e.add(34)
print(e)
```

2. Adding multiple values to the set:
- You can add multiple values to the set using update() function by passing it as a list.

```
f = {23,25,24,25,23}
f.update([34,62])
print(f)
```

3. Removing a value from the list:

- Remove function: Using remove() function you can remove a given value but if the given value doesnt exist in the set, it returns error.

```
g = {34,13,52,31,41}
g.remove(3) # This will return error since 3 is not in set
g.remove(34)
print(g) # 34 will not be in the set
```

- Discard function - Using discard function, you can remove a given value and it doesnt returns any error if the given value doesnt exist in the set.

```
h = {34,13,52,31,41}
h.discard(3) # Does nothing since 3 is not in set
h.discard(34) # Removes 34
print(h)
```

- Pop function - Using pop() function, you can remove a random value from the set.

```
i = {35,41,25,15,13}
i.pop() # Random value will be removed
print(i) 
```

## Mathematical Operations on Set

### Union 

Union basically combines two or more sets.
- You can perform Union Operation using `union()` function or `|` operator
```
set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
result_1 = set_one | set_two # {1,2,3,4,5,52} (the order will be random)
print(result_1)

set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
result_2 = set_one.union(set_two)
print(result_2)
```

### Intersection

The Intersection operation basically creates a new set that consists of only those values that are common among two or more sets.
- The Intersection operation can be perform using `intersection()` function or `&` operator.

```
set_one = {4,2,41,24,23}
set_two = {2,42,24,41}
result_1 = set_one & set_two # {2,24,41}
print(result_1)

set_one = {4,2,41,24,23}
set_two = {2,42,24,41}
result_2 = set_one.intersection(set_two)
print(result_2)
```

### Difference

- Difference Operation basically creates set which consists only values of one set that is not common with another set.
- Difference Operation is performed using `difference()` function or `-` operator

```
set_one = {35,21,36,23,12}
set_two = {24,51,3,23,21}
result_1 = set_one - set_two # {35,36,12}
print(result_1)

set_one = {35,21,36,23,12}
set_two = {24,51,3,23,21}
result_2 = set_one.difference(set_two)
print(result_2)
```

 ### Symmetric Difference

 Symmetric Difference basically create a new set with values that are not common among two or more sets.
 - Symmetric Difference operation can be performed using `symmetric_difference()` or `^` operator.

 ```
set_one = {3,2,41,22,43}
set_two = {24,51,2,12,41}
result_1 = set_one ^ set_two # {3,22,43,51,12,24}
print(result_1)

set_one = {3,2,41,22,43}
set_two = {24,51,2,12,41}
result_2 = set_one.symmetric_difference(set_two)
print(result_2)
```

### intersection/difference/symmetric_difference_update()

- Using `intersection_update()`, you can perform intersection operation and instead of creating new set, it updates the existing set by result of intersection.

```
set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
set_one.intersection_update(set_two)
print(set_one)
```

- Using `difference_update()`, you can perform difference operation and instead of creating new set, it updates the existing set by result of difference.

```
set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
set_one.difference_update(set_two)
print(set_one)
```

- Using `symmetric_difference_update()`, you can perform symmetric difference operation and instead of creating new set, it updates the existing set by result of symmetric difference.

```
set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
set_one.symmetric_difference_update(set_two)
print(set_one)
```

## Frozen Set

- Frozen Sets are sets that are immutable, it cannot be changed.
- A frozen set is defined using frozen set and values are passed in form of list.
```
j = frozenset([12,34,14,53,21])
print(type(j))
print(j)
```