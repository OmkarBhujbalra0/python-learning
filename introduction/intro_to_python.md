# Introduction to Python

Before starting to code in Python, let's understand how the things work in Python and what are the things that makes it different from other languages.

1. Case-Sensitivity -  Python is case-sensitive meaning two same words written in different cases are considered as different words.

```
a = 5  # --> The variable name is a to which value 5 is assigned.
A = 2  # --> The variable name is A to which value 2 is assigned.

# Both will return different results even both are same letters just in different cases.
print(a)
print(A)
```

2. Dynamically Typed - Python is dynamically typed language meaning any type of data can be assigned to any variable without any problem.

- In below example, first value `2` which is integer is assigned to variable `a` then in the next line string(text) `"two"` is assigned to variable `a`
- Printing value of a will return string(text) `"two"` instead of integer `2`

```
a = 2
a = 'two'
print(a)
```

This is called as Dynamic Typing, any type of data can be assigned to variable.
To understand this concept, let's know about concept of static Typing, where a variable can only be assigned with specified type of data. 

Below is a C language code where the variable a is declared with integer type, meaning only integer values can be assigned to a, any other type of value will return error.

```
int a;
a = 'apple' # --> This will return error since 'apple' is string and only integer value can be assigned to a
```

In Python, usually you don't need to declare the type of variable.

3. Indentation - Unlike other languages which uses semicolons or curly brackets for indicating block of code or line of code, Python only uses 4 blank spaces to define a block of code for functions or if-else/loops.

```
a = 15

if a<18:
    print("You are not eligible.")

# Notice how the print line is written after 4 blank spaces, it is to define the if block.
```

The 4 blank spaces (indentation) is basically used in if-else,loops, functions, classes and objects,etc.

4. Interpreted - Python is considered as interpreted language as the lines of code are executed and translated one by one.

- In the example below, there are 4 lines , first one declares the variable a and is assigned with value of 3.
- In second and third line, we are printing the values assigned to variable a and b, but b was never declared before due to which it will return error.
- The fourth line will not be executed since the execution stops at third line with returning error.

```
a = 5    # --> Executed
print(a) # --> Executed
print(b) # --> Returns error.
print(5) # --> Not Executed
```

## Basic Terms in Programming

### Tokens

Tokens are the smallest unit in a program.
For example - 

`a = 3`

In this line, there are 3 tokens.
-  `a` is a variable
-  `=` is an operator
-  `3` is a value

There are 4 different types of tokens in Python:

1. Keywords - are the special words reserved by programming language which are used for specific purpose.

`print = 3`
- In above code, print is a keyword reserved for `print` function to print result, the word `print` cannot be used as variable name.
- In Python, there are many keywords that you will encounter in future.

2. Identifiers - are words used by programmers to name variables, functions,etc.
The Identifiers are those words that are not reserved by programming language.

`age = 21`

Here, word `age` is an identifier since it is not a keyword and can be used as variable name.

3. Literal - is value that is assigned to a variable which is used to perform operations.
These are the following types of literals used in Python -
- Integer `(int)` - 1, 2, 3, 4, 5
- Float `(float)` - 1.3, 3.14
- String `(str)` - "apple","berry"
- Special `(None)` - `None`
- Collection Literal - List, Tuple, Set, Dict, these are built from above tokens.

4. Operators - are the tokens that are used to perform operations on/between one or more values.

These are the types of Operators in Programming Language:

- Arithmetic Operators - +, -, *, /, % 
- Assignment Operator - =, -=, +=, *=
- Comparison Operators - ==, <, >, <=, >+, 
- Unary Operators - Prefix and Postfix 
- Ternary Operator - condition1`?`result1`:`result2 
- Bitwise Operators - &, |, ~
- Logical Operators - and, or, not