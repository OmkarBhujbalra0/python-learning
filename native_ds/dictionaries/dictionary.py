# Dictionary

a = {}
print(type(a))

b = dict()
print(type(b))

# Dictionaries with values

c = dict(name="rajesh",age=32,branch="computer")
print(c)

d = {"name":"harshad","age":34,"branch":"civil"}
print(d)

# Accessing values

print(c.get("name"))
print(c["age"]) # Using get() function

# Accessing keys

print(d.keys()) # Prints a list of keys present in the dictionary

for i in d.keys(): 
    print(i) # Loops through the list of keys and prints them

# Accessing values

print(d.values()) # Prints a list of values present in the dictionary

for j in d.values():
    print(j) # Loops through the list of values

# Accessing keys and values

print(d.items()) # Prints a list of multiple tuples containing keys and values

for key,value in d.items():
    print(f"{key} is {value}") # Loops through the list and prints both values

# Adding new elements to the dictionary

e = {"name":"dakshesh","age":40,"branch":"Mech"}

e["year"] = 1986
print(e) # {"name":"dakshesh","age":40,"branch":"Mech","year":1986}

e.update({"gender":"male"})
print(e) # {"name":"dakshesh","age":40,"branch":"Mech","year":1986,"gender":"male"}

e.update({"age":42}) # Dictionary do not contain duplicate keys, using same key to add a value in the dictionary will update the value instead
print(e) # {"name":"dakshesh","age":42,"branch":"Mech","year":1986,"gender":"male"}

# Removing element from dictionary

f = {"name":"dakshesh","age":40,"branch":"Mech","gender":"male"}
f.pop("age")
print(f)

f.popitem() # Removes the last key and value
print(f) 

# Looping through the dictionary

for i in e:
    print(e[i])