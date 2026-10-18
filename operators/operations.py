# Arithmetic Operators

a = 8
b = 2

result1 = a + b # Addition
print(result1)
result2 = a - b # Subtraction
print(result2)
result3 = a * b # Multiplication
print(result3)
result4 = a / b # Division
print(result4)
result5 = a // b # Floor Division
print(result5)
result6 = a ** b # Exponent
print(result6)
result7 = a % b # Modulus
print(result7)

# Assignment Operators

c = 4
c += 3 # Adds 3 to 4 and assigns it to c
print(c)
c = 5
c -= 2 # Subtracts 2 from 5 and assigns it to c
print(c)
c = 6
c *= 3 # Multiplies 3 by 6 and assigns it to c
print(c)
c = 4
c /= 2 # Divides 4 by 2 and assigns it to c
print(c)
c = 4
c //= 2 # Divides 4 by 2 and assigns it to c
print(c)
c = 4
c %= 2 # Divides 4 by 2 and assigns the remainder to c
print(c)

# Relational Operators

d = 5
e = 4

print(d < e) # returns False since 5 is not less than 4
print(d > e) # returns True since 5 is greater than 4
print(d <= e) # returns False since 5 is not less than or equal to 4
print(d <= e) # returns True since 5 is greater than 4
print(d == e) # returns False since 5 is not equal to 4
print(d != e) # returns True since 5 is not equal to 4

# Unary Operators 

# Unary Minus

a = 3
b = -2

result11 = -a
result12 = -b

print(result11) # result is -3
print(result12) # result is 2

# Logical Operator 

c = 5
c = not c
d = 5
print(c)
print(~d)
print(0 or 67)
print(6 and 2)
print(6 & 2)
print(6 | 2)