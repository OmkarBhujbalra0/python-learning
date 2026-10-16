# Variables, Data Types and Type Casting

## Variable

Variable is basically used to store the data in the program.
You can either input the data yourself in the variable or assign it in program itself.
Variable allows users to store the input data for later use in the program.

```
a = 5  # Here, a is variable to which the value of 5 is assigned.
print(a + a) # This code adds the value of a with a and prints it (using the value of a for addition)
```

There are rules for writing variable name:
- The variable name should always start with a alphabet or _
- As already discussed, Python is case-sensitive, so variable name age and Age are treated as different variables.
- Variable name can only contain alphabets,underscore and numbers(not decimal numbers, negative numbers).
- Variables are identifiers so their names should not be a keyword.

## Data Types

Data Type basically means what type of data a variable is holding.

In programming, you will be dealing with different types of data, they are as follows:
- Integer (int) - Any positive or negative number (excluding decimals)
- Floating point Number (float) -  Any number containing decimal(floating) point.
- String (str) - is basically group of symbols, characters, digits,etc.
- None (None) - represents null value (absence of value)
- Collection Literal (list,tuple,set,dict) - are types of different native data structure in python.

You can check the type of value any variable is holding using type function.

```
b = 3
c = "Apple"
d = 3.14
e = None

print(type(b))
print(type(c))
print(type(d))
print(type(e))
```

## Typecasting

You can also change the data type of the value by using int(),float(),str() as respective.
This is called as Typecasting.

```
f = 3
print(float(f))
```

You can use this while inputting the data.

```
g = int(input("Enter a number:"))
print(g - 3) # Since the value of g is integer, it will be subtracted by 3.

h = "Apple"
print(int(h)) # This will return error, because variable b contains value consisting alphabets.

i = "34"
print(int(i)) # This will not error, since the string only contains numbers.

j = 45
print(str(45)) # This will print "45" instead of 45.
```

`int` <---> `float` 
`int`,`float` ----> `string` 
`string` ---> `int` or `float` (only when string contains only numbers.)

The process of using int(),float(),str() function to convert the data type is called as `Explicit Type Casting`, manually done by programmer.

Implicit Type Casting

In Implicit Type Casting, the data type of value is automatically converted to another data type.

```
k = 45
print(type(k/3)) # This will return float 
```

Performing division on integer or arithmetic operation between int and float values will always convert the result into float data type. 
