# Operators

Operators are type of tokens which is used to perform various operations.

The following are the types of Operators:

1. Arithmetic Operators - are operators used for arithmetic operations.

- `+` - is used to perform addition between values of two or more variables.
For ex - `result = a + b`
- `-` - is used to perform subtraction between values of two or more variables.
Subtracting value of `b` from value of `a`
For ex - `result = a - b`
- `*` - is used to perform multiplication between values of two or more variables.
For ex - `result = a * b`
- `/` - is used to perform division between values of two or more variables.
Dividing value of `b` by `a` returning quotient.
For ex - `result = a / b`
- `//` - is used to perform floor division between values of two or more variables.
Floor division basically divide one number by another number and returns floor value of quotient.
Floor value is basically value less than or equal to given value.
For example - Usually dividing 5 by 2 will return 2.5 as quotient but by performing floor division you get floor value of 2.5 which is 2
For ex - `result = a // b`
- `%` (Modulus) - is an operator which is used to divide 2 numbers to return remainder as result
For ex - `result = a % b`
- `**` (Exponent) - is an operator which calculates value of left variable raised to value of right variable.
For ex - `result = a ** b`

2. Assignment Operators - are operators that is used to assign value to the variable.

- `+=` - is used to add one value with value assigned to variable and assign the result to variable.
For example - 

```
a = 5 # 5 is assigned to a
a+=3 # 3 is added to 5 and the result is assigned to a
print(a)  # --> The result will be 8 
```
- `-=` - is used to subtract value from value assigned to variable and assign the result to variable.

```
a = 5
a -= 3
print(a) # --> Returns 2
``` 
- `*=` - is used to multiply value with value assigned to variable and assign the result to variable.

```
a = 5
a *= 3
print(a) # --> Returns 15
``` 
- `/=` - is used to divide value assigned to variable with another value and assign the result to variable.

```
a = 6
a /= 3
print(a) # --> Returns 2.0
``` 
- `%=` - is used to divide value assigned to variable with another value and assign the result(remainder) to variable.

```
a = 5
a %= 3
print(a) # --> Returns 2
``` 

3. Relational (Comparison) Operators - are used to compare the values of 2 or more variables.

- `<` (Less than) - is operator than return True or False as result by checking whether value of left variable is less than value of right variable.

```
a = 5
b = 2

result = 5 < 2
primt(result) # result is False
```