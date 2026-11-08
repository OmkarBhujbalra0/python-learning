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
