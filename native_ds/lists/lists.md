# List 

List is one of native data structures used in Python, for storing multiple values.
- An empty list is basically defined using `[]`

```
empty_list = []
print(empty_list) # prints []
```

- A list can store different types of data.
- The list below store integers,Boolean `True` value and String `"Apple"`
```
multi_type = [1,2,True,"Apple"]
print(multi_type)
```

# Accessing values stored in List

You can access values stored in list using index, index is basically position of values in the list.
- The indexes of list basically starts from 0, so to access the value at first position, you have to use index 0.
- You can access value in the list using `list_name[index]`
```
alphabets = ["A","B","C","D","E"]
print(alphabets[0]) # prints "A"
print(alphabets[4]) # prints "E"
```

# Adding the values in the list

You can add the values in the list using `append` function.
Append Function basically adds the value at the end of the list.

```
a = [1,2,3,4,5,6]
a.append(8)
print(a) # prints [1,2,3,4,5,6,8]
```

- Lists are mutable (something that you can modify), you can add,insert,update or delete the list.

# Inserting the value in the list

You can insert the values using `insert` function, which takes 2 arguments.
- The first argument is index where you want to insert the value
- The second argument is value that you want to insert at the given index.
The below code inserts value `7` at index `3` of list assigned to variable `b`
```
b = [1,2,3,4,5]
b.insert(3,7)
print(b) # [1,2,3,7,4,5]
```
When you try to insert the value in empty list, the value will be inserted at 0th index, and then inserting another value greater than the last index of the list, will basically append the value at the end of the list 
```
c = []
c.insert(4,3) # [3] -> value 3 inserted at index 0 even after trying to insert at index 4 since index 4 > index 0
c.insert(1,5) # [3,5] -> value 5 is inserted at index 1 
print(c) # [3,5]
```

# Removing the value from the list

- `pop` function - takes index as a argument and removes the value from that index of the list, if no argument is passed then it removes value at last index of list.

```
d = [1,2,3,4,5,6]
d.pop(3) # [1,2,3,5,6] -> Since value 4 is at index 3, 4 is removed from list
d.pop() # [1,2,3,5] -> Since no argument is passed, value 6 is removed.
print(d)
```

- `remove` function - basically removes the first occurence of the value from the list.
```
e = [1,2,3,4,2,6]
e.remove(2) # removes first occurence of 2 which is at index 1
print(e) # [1,3,4,2,6]
```

# Delete the list

- You can delete the list using `del` keyword before the variable to which the list is assigned.
```
f = [2,4,7,3,8]
del f
print(f) # Since list is deleted, there is no value assigned to f, so it will return error
```

# Sort the values in the list

- Using sort function you can sort the values in the list.

```
g = [4,67,1,85,5]

g.sort()
print(g)
```
```
h = [53,51,57,124,21]

h.sort(reverse=True)
print(h)
```