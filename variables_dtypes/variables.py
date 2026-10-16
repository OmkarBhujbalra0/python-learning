# Variable

a = 5  # Here, a is variable to which the value of 5 is assigned.
print(a + a) # This code adds the value of a with a and prints it (using the value of a for addition)

# Data Types

b = 3
c = "Apple"
d = 3.14
e = None

print(type(b))
print(type(c))
print(type(d))
print(type(e))

# You can also change the data type of the value by using int(),float(),str() as respective.

# This is called as Typecasting.

f = 3
print(float(f))

# You can use this while inputting the data.

g = int(input("Enter a number:"))
print(g - 3) # Since the value of g is integer, it will be subtracted by 3.

h = "Apple"
print(int(h)) # This will return error, because variable b contains value consisting alphabets.

i = "34"
print(int(i)) # This will not error, since the string only contains numbers.

j = 45
print(str(45)) # This will print "45" instead of 45.

# int <---> float 
# int,float ----> string 
# string ---> int or float (when string contains only numbers.)

# The process of using int(),float(),str() function to convert the data type is called as Explicit Type Casting, manually done by programmer.

# Implicit Type Casting

k = 45
print(type(k/3)) # This will return float 
