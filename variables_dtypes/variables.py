# Variable

a = 5  # Here, a is variable to which the value of 5 is assigned.
print(a + a) # This code adds the value of a with a and prints it (using the value of a for addition)

# Data Types

b = 3
c = "Apple"
d = 3.14
e = None
f = True

print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# You can also change the data type of the value by using int(),float(),str() as respective.

# This is called as Typecasting.

g = 3
print(float(g))

# You can use this while inputting the data.

h = int(input("Enter a number:"))
print(h - 3) # Since the value of g is integer, it will be subtracted by 3.

i = "Apple"
# print(int(i)) # This will return error, because variable b contains value consisting alphabets.

j = "34"
print(int(j)) # This will not error, since the string only contains numbers.

k = 45
print(str(k)) # This will print "45" instead of 45.

l = True
m = False

print(int(l))
print(int(m))

# The process of using int(),float(),str(),bool() function to convert the data type is called as Explicit Type Casting, manually done by programmer.

# Implicit Type Casting

n = 45
print(type(n/3)) # This will return float 
