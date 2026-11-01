# Empty List

empty_list = []
print(empty_list) # prints []

# List with data of multiple data types

multi_type = [1,2,True,"Apple"]
print(multi_type)

# Accessing the values from the list

alphabets = ["A","B","C","D","E"]
print(alphabets[0]) # prints "A"
print(alphabets[4]) # prints "E"
print(alphabets[2:5])
print(alphabets[-2:1])
# Adding the values in the list

a = [1,2,3,4,5,6]
a.append(8)
print(a) # prints [1,2,3,4,5,6,8]

# Inserting the value in the list

b = [1,2,3,4,5]
b.insert(3,7)
print(b)

c = []
c.insert(4,3)
c.insert(1,5)
print(c)

# Remove the last value or any value using index from list

d = [1,2,3,4,5,6]
d.pop(3) # [1,2,3,5,6]
d.pop() # [1,2,3,5]
print(d)

e = [1,2,3,4,2,6]
e.remove(2) # removes first occurence of 2 which is at index 1
print(e) # [1,3,4,2,6]

# Delete the list

f = [2,4,7,3,8]
del f
# print(f)

# Sort the values in the list

g = [4,67,1,85,5]

g.sort()
print(g)

h = [53,51,57,124,21]

h.sort(reverse=True)
print(h)