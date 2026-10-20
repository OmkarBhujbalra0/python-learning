# Conditionals

Conditionals are the statements that performs tasks based on given condition, `if` condition is True, task is performed `else` it is not performed.
- Whatever you learnt in Operators, will be used here.

1. `if`-`else` - `if` keyword is used before stating the condition, which if True,performs given task otherwise the control is given to `else` statement which will perform other task.
- `else` keyword don't need condition to perform given task under it, it will perform the task if the condition in if statement is False, so it is used after if statement.
  
- The below code will print `Not Eligible` if condition (age < 18) after `if` keyword is True, since the condition is not True, it will print `Eligible` instead.  

```
age = 18

if age < 18:
    print("Not Eligible!)
else:
    print("Eligible") # Eligible is printed since age is 18
```

2. `if`-`elif`-`else` - These keywords are used if there are more than 2 conditions by which tasks should be performed.
- `elif` keyword is used after `if` keyword, to check another condition and perform task based on that condition.  
- In the code below, there are 3 variables and if-elif-else statements compare the values of these variables to print the highest value.
```
a = 4
b = 6
c = 2

if a > b and a > c:
    print("a is highest of them all.")
elif b > a and b > c:
    print("b is highest of them all.")
else:
    print("c is highest of them all.")
```

3. `if` - if statement can be used if you only want to perform one task if condition is True and no task if the condition is False.
- Below code will print the statement only if age is greater than or equal to 18.
```
age = 18

if age >= 18:
    print("You are Eligible for Driving License.")
``` 