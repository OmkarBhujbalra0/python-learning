# Dictionary

Dictionary is another data structure in Python that stores the data in the form of key-value pairs.
- An empty dictionary can be defined using `{}` or using `dict()` function.

```
a = {}
print(type(a)) # <class 'dict'>

b = dict()
print(type(b)) # <class 'dict'>
```

- You can create a dictionary with data through following ways.

- Using dict() function
```
c = dict(name="rajesh",age=38,branch="computer")
print(c) # {"name":"rajesh","age":38,"branch":"computer"}
```
- Using {}
```
d = {"name":"harshad","age":37,"branch":"civil"}
print(d) # {"name":"harshad","age":37,"branch":"civil"} 
```

- Dictionary consists of keys and values, where a value is attached to the key, as seen in above examples.

Unlike list or tuple, you cannot access the values using indexing, since the values are attached to the keys in the dictionaries, you have to using the key name to access a specific value.

```
e = {"red":"apple","blue":"sky","green":"grass"}
print(e["red"]) # prints "apple"
```

## Dictionary Functions

1. `get()` function - 
You can also use get() function to access the value by passing the key.

```
f = {"red":"apple","blue":"sky","green":"grass"}
print(f.get("red")) # prints "apple"
```

2. `keys()` function - The keys function basically returns a list of keys present in the dictionary.

```
g = {"name":"dakshesh","age":40,"branch":"Mech"}
print(g.keys()) # dict_keys(['name','age','branch'])

for key in g.keys(): # Loops through list of keys and prints the keys
    print(key)
```

3. `values()` function - The values() function returns the list of values present in the dictionary.

```
h = {"name":"dakshesh","age":40,"branch":"Mech"}
print(h.values()) # dict_values(['dakshesh',40,'Mech'])

for value in h.values(): # Loops through list of values and prints the values
    print(value)
```

4. `items()` function - The items() function basically returns a list of tuples containing both keys and values.

```
i = {"name":"dakshesh","age":40,"branch":"Mech"}
print(i.items()) # dict_items([('name','dakshesh'),('age',40),('branch','Mech')])

for key, value in i.items(): # Loops through list of tuples and prints the keys anf values
    print(f"{key} is {value}")
```

## Adding an element in the dictionary

You can add an element to the dictionary through following ways.

```
j = {"name":"dakshesh","age":40,"branch":"Mech"}
j["gender"] = "male"
print(j) # {"name":"dakshesh","age":40,"branch":"Mech","gender":"male"}
```

Another method to add an element is using `update()` function

```
k = {"name":"dakshesh","age":40,"branch":"Mech"}
k.update({"gender":"male"})
print(k) # {"name":"dakshesh","age":40,"branch":"Mech","gender":"male"}
```

Note - Dictionary cannot have duplicate keys, if you try to add same key with different value, it will update the value of existing key instead of adding new key to the dictionary instead.

```
l = {"name":"dakshesh","age":40,"branch":"Mech"}
l["age"] = 35
print(l) # {"name":"dakshesh","age":35,"branch":"Mech"}
```

# Removing an element from the dictionary

You can remove an element through its key by using `pop()` function.

```
m = {"name":"dakshesh","age":40,"branch":"Mech","gender":"male"}
m.pop("gender")
print(m)
```

You can remove the last key and value from the dictionary using `popitem()` function.

```
n = {"name":"dakshesh","age":40,"branch":"Mech","gender":"male"}
n.popitem()
print(n)
```

## Looping through Dictionary

You can loop through dictionary using for loop
While looping through dictionary, you will be looping through keys instead of values, using those keys you can access the values from the dictionary

```
o = {"name":"dakshesh","age":40,"branch":"Mech","gender":"male"}

for key in o:
    print(o[key])```