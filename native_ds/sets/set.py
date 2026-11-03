# An empty set

a = set()
print(type(a))

b = {}
print(type(b)) # This will return type as dict instead of set

# Creating set with values

c = {24,25,13,61,53}
print(c)

# Creating Set with duplicate values

d = {34,34,52,12,42,12}
print(d)

# Adding the values to the set

e = {23,42,12,4}
e.add(32)
print(e)

f = {35,62,23}
f.update([24,51,32])
print(f)

# Removing the values from the list

g = {34,13,52,31,41}
# g.remove(3) # Remove function returns error if the value doesnt exist
g.discard(14) # Removes given value from the set, if it doesnt exist it does nothing
g.pop() # Removes random value
print(g)

print("Mathematical Operations")

# Union

set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
result_1 = set_one | set_two
print(result_1)

set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
result_2 = set_one.union(set_two)
print(result_2)

# Intersection

set_one = {4,2,41,24,23}
set_two = {2,42,24,41}
result_1 = set_one & set_two
print(result_1)

set_one = {4,2,41,24,23}
set_two = {2,42,24,41}
result_2 = set_one.intersection(set_two)
print(result_2)

# Difference

set_one = {35,21,36,23,12}
set_two = {24,51,3,23,21}
result_1 = set_one - set_two
print(result_1)

set_one = {35,21,36,23,12}
set_two = {24,51,3,23,21}
result_2 = set_one.difference(set_two)
print(result_2)

# Symmetric Difference

set_one = {3,2,41,22,43}
set_two = {24,51,2,12,41}
result_1 = set_one ^ set_two
print(result_1)

set_one = {3,2,41,22,43}
set_two = {24,51,2,12,41}
result_2 = set_one.symmetric_difference(set_two)
print(result_2)

# Intersection Update

set_one = {1,2,3,4,5}
set_two = {2,3,52,3,5}
set_one.intersection_update(set_two)
print(set_one)

# Difference Update

set_one = {4,2,41,24,23}
set_two = {2,42,24,41}
set_one.difference_update(set_two)
print(set_one)

# Symmetric Difference Update

set_one = {35,21,36,23,12}
set_two = {24,51,3,23,21}
set_one.symmetric_difference_update(set_two)
print(set_one)
