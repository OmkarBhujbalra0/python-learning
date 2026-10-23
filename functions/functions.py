# Functions

def check_number(number):  # Function Definition
    if number >= 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is negative")

check_number(4) # Function Call

# Split the tasks using Functions

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

number_checker(5) # number_checker function is called which calls both the functions under it and prints the respective results.

# function with return statement

def addition(a, b):
    return a + b

result = addition(3,4)
print(result)