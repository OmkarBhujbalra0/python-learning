# Loops (Looping Statements)

Looping Statements are statements that are used to perform repetitive tasks.

# for Loop

`for` statement basically repeats the task by initiating the value of given variable or by running it over a data structures like list or arrays for printing element from data structures.
- In the code below, the variable `i` is initiated with value of 0 and increased by 1 after executing task till value of i is less than 5 (5 is exclusive(not included)),printing the given message 5 Times.

`i` -> 0 (1st execution)-> 1(2nd execution) -> 2(3rd execution) -> 3(4th execution) -> 4(5th execution) -> 5 (The loop stops)
```
for i in range(0,5):
    print("This will be printed 5 Times.")
```

## for loop with steps

You can also allow the for loop to repeat the task by skipping the steps.
- The code below will print the number assigned to the variable `i` and skip 3 steps with each execution.
- So, from 1 to 10 only 1,4,7,10 will be printed skipping 3 numbers between them instead of all the numbers.
```
for i in range(1,11,3):
    print(i)
```

# While Loop