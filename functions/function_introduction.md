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

## Scope of Function

Scope is basically area within which we can access the value of the variable.
- In the below example, the function `scope checker` assigns `"Hello"` to `message` variable which is printed after the function is called.
- Variable defined within a function is called Local Variable.
- But when you try to print the value of message manually outside the function, it returns error because you are trying to access the variable outside its scope.
```
def scope_checker():
    message = "Hello" # We defined the variable message with value "Hello"
    print(message)

scope_checker() # prints "Hello"
print(message) # raises error since we are trying to access the message variable  outside its scope.
```
When the variable can be only accessed within a function, it is called Local Scope.
- Variables within local scope can be only used within the local scope.

When the variable can be accessed from anywhere in the program, it is called Global Scope.
- The variable defined outside any function is called Global Variable.
- In the below example, the variable age is defined outside the function, so the function below can use the value of variable age.
```
age = 34 # Global Variable

def age_checker():
    if age >= 18:
        print("Eligible")
    else:
        print("Ineligible")

age_checker()
```
- But the function cannot change the value of variable age, it will return an error.
```
age = 34 # Global Variable

def age_changer():
    age = age + 10 # Changing the value of Global Variable 
    print(age)

age_checker()
```

Enclosing Scope - is scope where variable defined in outer function can be accessed by inner function.
- In the code below, there are 2 functions, one within another, the inner function can access the variable defined in outer function.
- Just like Global variable, the inner function cannot change the value of variable defined in outer function.
```
def outer_function():
    outer_var = "Outer Value"
    print(f"This is printed using outer function, {outer_var}")

    def inner_function():
        print(f"This is printed using inner function, {outer_var}")

    inner_function()

outer_function()
```

## global and nonlocal

`global` keyword is used when you want to change the value of global variable.

```
age = 34

def change_age():
    global age
    age = age + 4
    print(age)
    
change_age()
```

`nonlocal` keyword is used to modify the value of enclosing variable in outer function from inner function.

```
def outer_function():
    age = 35
    print(f"Outer function:{age}")
    
    def inner_function():
        nonlocal age
        age = age + 6
        print(f"Inner function:{age}")
        
    inner_function()
    
outer_function()
```

## Pure and Impure Functions

Pure Functions are the function that performs tasks without any side effects.
- The function below returns `"hello world"` message and this message is assigned to `message` variable which is then used to print.
- The function below has no side effects and returns the message.
```
def hello():
    return "hello world"
    
message = hello()
print(message)
```

Impure Functions are functions that performs tasks with side effects.
- The function below is impure since it prints the message in the console.
```
def print_hello():
    print("Hello World")

print_hello()
```
- Another example could be function using `global` and `nonlocal keyword` for modifying the value of global or enclosing scope variable, the side effects would be comple data flow.

## Lambda Function

lambda function is basically for functions that can be defined in one line or expression.
- It is defined using `lambda` keyword

```
sum_result = lambda x, y: x + y
print(sum_result(4, 5))  # prints 9 as result
```

- lambda function using if-else
- You can also use if-else statement by using ternary operator.
```
check_num = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_num(3))  # prints "Odd"
```

## Recursion 

Recursion is method where you call a same function within a function.
- Function using Recursion is called Recursive Function.

```
def fact(num):
    if num == 0:
        return 1

    return num * fact(num - 1)

print(fact(5))
```