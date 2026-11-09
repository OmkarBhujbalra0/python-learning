# Comprehensions

Comprehension means interpreting the content of one thing and expressing it in another thing.

In Python you can perform List Comprehension, Set Comprehension and Dicitionary Comprehension.

`a = [value for value in loop/list/tuple/dictionary]`

## List Comprehension

In List Comprehension, we basically create a list from elements from other code like for loop or another list.
- In the code below, we are using for loop and appending all the values from 0 to 10 in the list.
```
a = []

for i in range(0,11):
    a.append(i)
    
print(a) # [0,1,2,3,4,5,6,7,8,9,10]
```

- You can simplify this process by using List Comprehension and you will get same results.

```
a = [x for x in range(0,11)]

print(a) # [0,1,2,3,4,5,6,7,8,9,10]
```

- Not only you can make a list containing values from for loop, but also from another list/tuple/set/dictionary.
- Along with that you can also specify a condition based on which you can add only values satisfying that condition.
```
b = [12,31,14,51,125,51]

c = [x for x in b if x % 2 == 0]
print(c) # [12,14]
```

## Comprehension using nested loops

- In Comprehension, you can also make a list/set/dictionary containing not only the values from list but also values containing in nested lists
- In the example below, there is list containing multiple lists, using list comprehension you can create a list of all the values inside the nested lists.
- Each value is accessed from inner lists and appended to new list.
```
d = [[14,51],[15,11],[63,12]]
e = [inner_element for outer_element in d for inner_element in outer_element]
print(d) # [[14,51],[15,11],[63,12]]
print(e) # [14,51,15,11,63,12]
```

- The above code works like nested loops

```
f = [[14,51],[15,11],[63,12]]
g = []

for outer_element in f: # [[14,51],[15,11],[63,12]] -> [14,51] [15,11] [63,12]
    for inner_element in outer_element: # [14,51] -> 14,51 [15,11] -> 15,11 [63,12] -> 63,12
        g.append(inner_element)
        
print(f) # [[14,51],[15,11],[63,12]]
print(g) # d = [14,51,15,11,63,12]
```

## Set Comprehension

- Just like List Comprehension, you can perform Set Comprehension and other comprehension operations except only unique values will be present in the set.

```
a = [24,41,53,13,53,24,41]
b = {x for x in a} # {24,41,53,13}
print(b)
```

- Works just like appending the values from list in set one by one using for loop

```
c = [24,41,53,13,53,24,41]
d = set()
for i in c:
    d.add(i)
print(d)
```

## Dictionary Comprehension

- To performs Comprehension on Dictionary becomes tricky since you cannot directly access values from dictionary just like we did for lists and sets.

```
e = {"Red":"Scarlet","Blue":"Cyan","Violet":"Lavender"}
f = {key:value for key,value in e.items()}
print(f)
```

- The above code works same as 

```
g = ["Red","Blue","Violet"]
h = ["Scarlet","Cyan","Lavender"]
i = {}
for j in range(0,len(g)):
    i[g[j]] = h[j] # "Red": "Scarlet" "Blue":"Cyan "Violet":"Lavender"
print(i) # {"Red": "Scarlet","Blue":"Cyan,"Violet":"Lavender"}
```

## Generator Comprehension

- Generator Comprehension basically is way of creating a generator in Python, just like lists and sets.
- Generator Comprehension is done using `()`
- You can learn more about Generators from [generators](https://github.com/OmkarBhujbalra0/python-learning/tree/main/generators) folder.
```
k = (x for x in range(1,6))
print(k) # This will return generator object <generator object <genexpr> as an output instead of displaying values.

for value in k:
    print(value) # 1 2 3 4 5
```

In Generators, you basically access the values whenever required instead of accessing all the values at once like list or set.
- Using `next()` function while printing the values, you can access the one value and the execution continues from next value

```
j = (x for x in range(1,6))
print(next(j)) # 1
print(next(j)) # 2
```