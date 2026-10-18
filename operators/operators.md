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
- `>` (Less than) - is operator than return True or False as result by checking whether value of left variable is greater than value of right variable.

```
a = 5
b = 2

result = 5 > 2
primt(result) # result is True
```
- `<=` (Less than or equal to) - is operator than return True or False as result by checking whether value of left variable is less than or equal to value of right variable.

```
a = 5
b = 2

result = 5 <= 2
primt(result) # result is False
```
- `>=` (Greater than or equal to) - is operator than return True or False as result by checking whether value of left variable is greater than or equal to value of right variable.

```
a = 5
b = 2

result = 5 >= 2
primt(result) # result is True
```
- `==` (Equal to) - is operator than return True or False as result by checking whether value of left variable is equal to value of right variable.

```
a = 5
b = 2

result = 5 == 2
primt(result) # result is False
```
- `!=` (Not Equal to) - is operator than return True or False as result by checking whether value of left variable is not equal to value of right variable.

```
a = 5
b = 2

result = 5 != 2
primt(result) # result is True
```

4. Unary Operators - are operators that perform operation on value of one variable.
There are 2 types of unary operators -
- Prefix Operator - is operator that performs operation on value before it is used in instruction

```
--a
++a
```
- Postfix Operator - is operator that perform operation after it is used in instruction

```
--a
++a
```

Note - Python doesn't support prefix and postfix operators like other programming languages.

- Unary Minus `-` -  This operator changes the sign of the value
```
a = 3
b = -a
print(a) # --> 3 is positive
print(b) # --> 3 is negative
```

- Unary Logical Operator - not(logical) | `~` (Bitwise)
```
c = 3
print(not c) # returns False since any number that is not equal to 0 is considered True and using not operator on 3 will convert it into False

d = 5
print(~c) # return -6 since ~ is bitwise operator, and python uses -(n + 1) formula to perform not operation.
```

5. Logical Operators - are operators that perform logical operations.

- `and` - is operator that returns value of last variable if both values of variable are not 0 else return 0 if any value is 0.
```
a = 4
b = 2
print(a and b) # return value of b since both are true(not zero)
```
- `or` - is operator that returns value that is not zero if any values of variable are True (or not 0) else return 0 if both values are 0.
```
a = 0
b = 2
print(a or b) # return 2 since 2 is not zero 
```
- `not` - Already discussed in Unary operators, inverts the boolean value of value, return True if original value is False or not zero and vice-versa

6. Bitwise Operators - are operators that performs operations on bit-level of values.

- `&`(and) - is bitwise operation that performs `and` operation on bit-level
```
a = 6 # In Binary lang, it is 110
b = 4 # In Binary lang, it is 100

result = a & b 
print(result) # --> returns 4 (100 in binary)
```
- `|`(oe) - is bitwise operation that performs `or` operation on bit-level
```
a = 3 # In Binary lang, it is 011
b = 6 # In Binary lang, it is 110

result = a & b 
print(result) # --> returns 7 (111 in binary)
```
- `~` - Already discussed in Unary Operator, perform `not` operation on bit level.
```
a = 3 # In Binary lang, it is 011
b = 6 # In Binary lang, it is 110

result = a & b 
print(result) # --> returns 7 (111 in binary)
```
a = 3
a = ~a
print(a) # --> returns -4 since Python uses -(n + 1) formula for bitwise not operator.
```