# Conditionals and Match Statement

## Conditionals

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

Note - You can have multiple number of elif statements between if and else statements for performing tasks based on multiple conditions.

3. `if` - if statement can be used if you only want to perform one task if condition is True and no task if the condition is False.
- Below code will print the statement only if age is greater than or equal to 18.
```
age = 18

if age >= 18:
    print("You are Eligible for Driving License.")
``` 

4. Nested if-else - Nested if-else statements are used if you want to perform task if condition within condition is True.
- Here, we use if and elif statement multiple times for checking multiple conditions and based on that we perform tasks.
- In the below code, we are checking the year and course name of student, where if `course` name is computer and `year` is first then it will print `First Year Student of Computer Engineering` else it will move forward to elif or else statements.
```
course = 'computer'
year = 'first'

if year == 'first':
    if course == 'computer':
        print("First Year Student of Computer Engineering")
    elif course == 'it':
        print("First Year Student of IT")
    else:
        print("First Year Student")
elif year == 'second':
    print("Second Year Student")
elif year == 'third':
    print("Third Year Student")
elif (year == 'final') or (year == 'fourth'):
    print("Final Year Student")
```

Note -  `else` statement is optional, usually used when you need to perform some other task without stating the condition when the if statement fails, you can perform task based on conditions by only using `if` or `elif` as we did above. 

5. One-line Conditional Statement (Ternary Operator) - are used to simple conditionals statements to perform simple tasks.

`print("Eligible") if age > 18 else print("Not Eligible")`