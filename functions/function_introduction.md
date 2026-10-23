# Functions

A function is basically a block of code that can be reused multiple times, instead of writing same code in multiple places in program, you can wrap the code in the function and call the function whenever you want to reuse that code.

Function consists of 2 things -
1. Function Definition - is defining what task will be performed by the function
- You can define a function by using a `def` keyword and writing the name of the function (the name should be descriptive).
- The below code define the function `check_number` which checks whether the number is positive or negative.
```
def check_number(number):
    if number >= 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is negative")
```

2. Function Call - is using the function by calling its name.
- The code below is calling the function `check_number` which will print `4 is positive`.

```
check_number(4)
```

(Note - Function Declaration is when you declare that function exists in the program, Function Declaration and Definition are separate steps in languages like C/C++, but in case of python, both are the same thing.)

- Functions can also be used to split the complex tasks into functions performing one specific task.
- Below code splits two tasks, checking whether the number is even or odd and checking whether the number is positive or negative into 2 functions, which are then called by another function `number_checker` after it is called.
```
def check_positive_or_negative(number): # -> Function to check whether the number is positive or negative is defined.
    if number >= 0:
        print("Number is Positive")
    else:
        print("Number is Negative")

def check_even_or_odd(number): # function to check whether number is even or odd is defined. 
    if number % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

def number_checker(number):
    check_positive_or_negative(number) # check_positive_or_negative function written to be called
    check_even_or_odd(number) # check_even_or_odd function written to be called

number_check(5) # number_checker function is called which calls both the functions under it and prints the respective results.
```