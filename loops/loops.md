# Loops (Looping Statements)

Looping Statements are statements that are used to perform repetitive tasks.
- Each step of repeating the task is called Iteration.

## for Loop

`for` statement basically repeats the task by initiating the value of given variable and increasing its value after each execution or by running it over a data structures like list or arrays for printing element from data structures.
- In the code below, the variable `i` is initiated with value of 0 and increased by 1 after executing task till value of i is less than 5 (5 is exclusive(not included)),printing the given message 5 Times (Only 5 Iterations).
```
for i in range(0,5):
    print("This will be printed 5 Times.")
```
`i` -> 0 (1st iteration)-> 1(2nd iteration) -> 2(3rd iteration) -> 3(4th iteration) -> 4(5th iteration) -> 5 (The loop stops)

### for loop with steps

You can also allow the for loop to repeat the task by skipping the steps.
- The code below will print the number assigned to the variable `i` and the value wil move 3 steps forward  with each iteration.
- So, from 1 to 10 only 1,4,7,10 will be printed by moving 3 steps forward between them instead of all the numbers.
```
for i in range(1,11,3):
    print(i)
```

You can also set negative value to step for moving steps backward
- In the code below, the variable value starts at 21 and moves 2 steps backwards to 19 and so on till 13, not 11 since 11 is exclusive.
```
for i in range(21,11,-2):
    print(i)
```

## While Loop

while loop is looping statement that will repeat the task until the condition is true.

- The while statement will check whether the condition is True, since value of variable a is True, so it will print * till the condition is False, which in this case is not going to happen, so the * will keep on printing until you dont stop it.
- Also, anything written below this code will be not executed, since the program will continue to execute this code, so make sure to write while statements in such a way that it should stop eventually.
```
a = True

while a:
    print("*")
```

- while statement will repeat the task until the condition is not False so if you don't want the program to keep running and repeating tasks, you have to writing while statement in such a way that eventually, the condition becomes False
- In the code below, we assigned value 1 to variable a and while statement will check before repeating the task whether value of a is less than 6, if yes then it will continue to repeat else stop the loop, also after each iteration the value of a will be increased by 1. (The while loop below will print value of a 5 times)
1 -> 2 -> 3 -> 4 -> 5 ->X 6 ( It will not print 6 since the loop stops when value becomes equal to 6)
```
a = 1

while a < 6:
    print(a)
    a+=1
```

### Loops with Conditionals

You can also use loops with condition statements.

- The code below uses for loop with if-else statement, where value of variable i iis initiated from 1 and increased by 1 till the value is less than 11. The if-else statement checks whether the value of i is even or odd by checking whether i % 2 returns 0 as remainder (its even else odd)

```
for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
```

## break and continue

### break

The break statement will basically end the loop. It is often used with if-else statements to end the loop after a specific condition is satisfied/not satisfied
- The code below assigned 1 to variable a and then while loop repeats the task till the condition is False and keeps adding 1 to value of variable a, since we are using break statement after checking whether a is greater than 10, the loop stops after reaching 10.
```
a = 1

while True:
    if a > 10:
        break
    else:
        print(a)
    i+=1
```

### continue statement

continue statements will basically end the current iteration and start next iteration.
- The code below uses for loop which initiates the value of i from 1 and keeps on increasing till 25, while increasing the value of i if value of i is divisible by 4, the iteration for that value will be skipped and other values will be printed. 
- It will print like this: 1 2 3 5 6 7 9 10 11 13 --> Skipping all the values divisible by 4
```
for i in range(1,25):
    if i % 4 == 0:
        continue
    else:
        print(i)
```