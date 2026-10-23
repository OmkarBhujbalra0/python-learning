# Functions 

## Arguments and Parameters

Functions uses Arguments and Parameters to work with data.

- Arguments are the values passed to the function during the function call, on which the operations will be performed.

- Parameters are the variables declared during function definition, which is used to store the values passed during function call for further operations.
- The below code uses `a` and `b` as parameters to store the values 3 and 4 passed during function call and performs addition on `a` and `b`.
```
def addition(a, b): # -> a and b are parameters
    print(a + b)

addition(3, 4) # -> 3 and 4 are arguments (values) passed during function call
```

## return statement

`return` statement is statement used inside the function to return the value to user calling the function.
- Using `return` statement, you can use the result of one function for further operations, such as using it as input for another function or variable.
- As the value return by return statement is used by the code, to access the returned value, you have to assign it to a variable.
- The code below is defining a function which takes 2 arguments and performs addition on them, and return the result, the result value is then assigned to result variable, which is then used to print the value.
```
def addition(a,b):
    return a + b

result = addition(3,4)
print(result)
```

Now combining arguments/parameters and return statement, there are four ways to write and call the function.

1. No Arguments, No return - In this method, we neither arguments nor the return statement.
- In the code below, the `check_status` function is definition with a variable `status` with value `active` assigned to it. When the function is called, the function checks whether the status is active or not and print the message based on that (in this case, its active so it will print the message).
- No arguments are used and we are not returning any value in this function, only performing tasks.
```
def check_status():
    status = 'active'
    if status == 'active':
        print("Machine is Active")

check_status()
```

2. No Arguments with return statement - In this method, we use return statement to return value but we don't use arguments to input data.
- In the code below, the function performs same task as previous function but uses return statement to return the message `Status is Active`, when the function is called the message is returned and assigned to the variable `message`, which is then printed.
- The difference is to access the return value, we are using a variable.
```
def check_status():
    status = 'active'
    if status == 'active':
        return "Status is Active"

message = check_status()
print(message)
```

3. Arguments with no return statement - In this method, we use arguments to pass values to the function, but don't use `return` statement.
- In the code below, we're using `status` as parameter to assign the argument value passed during the function call, by checking the argument value, the function will print the message.
- This time we can input the data in the function using arguments and the function will not return any value instead it will print the message.
```
def check_status(status):
    if status == 'active':
        print("Status is Active")

check_status("active")
```

4. Arguments with return statement - In this method, we use both arguments to pass the values and return statement to return the value.
- In the code below, the function does the same task but this time we can input the values using arguments and the function will return the message, which is assigned to a variable using which we can print the message.
```
def check_status(status):
    if status == 'active':
        return "Status is Active"

message = check_status("active")
print(message)
```