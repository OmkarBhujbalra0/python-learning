# Tuples

a = ()
print(type(a))

b = (64,14,22,75,1)
print(b[0])

c = (34)
print(type(c)) # <class 'int'> 

d = (34,)
print(type(d)) # <class 'tuple'>

# Concatenation

e = (23,53,15,64)
f = (54,13,74,12)
print(e + f)

# Slicing

g = (35,2,53,12)
print(g[1:4])

# Membership Testing

# Membership Testing in List

h = (23,41,25,61,12,51)
if 52 in h:
    print("52 is in m")