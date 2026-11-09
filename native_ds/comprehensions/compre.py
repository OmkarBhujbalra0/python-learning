# List Comprehension

a = []
for i in range(1,11):
    a.append(i)

print(a)

# Same code using List Comprehension

b = [x for x in range(1,11)]
print(b)

# List Comprehension with Condition

c = [x for x in range(1,11) if x % 2 == 0]
print(c)

# List Comprehension using another List

d = [41,43,51,12,51,13]
e = [x for x in d if x % 2 != 0]
print(d)
print(e)

# List comprehension with nested loops

f = [[1,2],[3,2],[5,6]]
g = [inner_element for outer_element in f for inner_element in outer_element]
print(f)
print(g)


# To understand the above code, its like writing nested loops

h = [[1,4],[15,31],[51,32]]
i = []
for outer_element in h:
    for inner_element in outer_element:
        i.append(inner_element)

print(h)
print(i)

# Set Comprehension

a = [24,41,53,13,53,24,41]
b = {x for x in a}
print(b)

c = [24,41,53,13,53,24,41]
d = set()
for i in c:
    d.add(i)
print(d)

# Dictionary Comprehension

e = {"Red":"Scarlet","Blue":"Cyan","Violet":"Lavender"}
f = {key:value for key,value in e.items()}
print(f)

g = ["Red","Blue","Violet"]
h = ["Scarlet","Cyan","Lavender"]
i = {}
for j in range(0,len(g)):
    i[g[j]] = h[j]
print(i)

# Dictionary Comprehension using List