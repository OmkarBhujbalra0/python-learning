# How to get a output in Python
print("<------ Print Function ------>")

print("Hello World") # --> Prints the content within the brackets.
print(3) # --> Also prints numbers.

# Using print function, you can also print the value assigned to variable.

a = 5
print(a) # --> Prints 5

# Suppose you want to print the message:
# The value of a is 5
# But instead of writing 5 on your own, you can use variable like this.

print("The value of a is", a)

# Another way of using value assigned to variable with message you want to print is String Formatting.
# To perform String Formatting, you need f and {}

print(f"The value of a is {a}")
# Here, you are inserting the value of a directly into message.

print("<------ Input Function ------>")

# In Python, to input the data we use input function, which is later stored in variable.

input_data = input()  # --> This will store the input data in the variable input_data
print(input_data) 

# Now, let's use input function to perform simple subtraction.

b = input() # --> Input value assigned to b
print(b - 3) # --> The value assigned to b is subtracted by 3

# This will give you an error, because input function by default accepts input value as string.
# And you cannot subtract 3 from string.
# The simple solution is to convert the input value into integer first and then subtract it by 3.

c = input("Enter your name:") # When you run this code, it will print this message and then you can input the value.
print(c)

# Without any message, there will be blank space, you will have to directly input the data and the data will be printed.