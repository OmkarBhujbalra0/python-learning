# Generators

Generators are Python objects that basically returns the value when demanded and pauses the execution at the state wherever its left, so when the user calls the generator again, the execution starts from same point where its left.
- Unlike functions which performs a tasks and completes the execution, generators can pause the execution and perform task when called.
- Generators uses Lazy Evaluation Concept meaning it will only provide when asked, instead of wasting memory by storing unwanted data that will never be used, generators will perform tasks when asked, so it doesn't waste the memory till any task is performed.
- A Generator function uses `yield` keyword, the yield keyword performs a task and stops the execution.
- Let's understand how the generators works.

```
def gen_func():
    for i in range(0,3):
        yield i

gen = gen_func()
print(gen) # <generator object gen_func>

for i in gen:
    print(i) # 0  1  2
```

- `next()` function basically asks the generator for next value and resumes the execution 
- In the code below, the generator function uses for loop from which the values are yielded and execution is paused at each yield.
- The generator function is assigned to `gen` variable to create a generator object.
- Using next() function, the gen generator object yields the first value 0 and pauses the execution. This process can be repeated till the generator object iterates values till 2, if you try to use next() function third time, it will return error since there are no values to iterate for generator.

```
def generate():
    for i in range(2):
        yield i
        
gen = generate()

print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # Stop Iteration Error since the iteration stops at 1
```

- `send()` function - allows you to pass value to the generator.

```
def gene():
    while True:
        input_data = yield
        print(f"Your data: {input_data}")

input_gen = gene()

print(next(input_gen)) # None since no value is passed to the generator
input_gen.send("My Input") # "Your data: My Input"
```

- `yield from` statement basically yields all the values from another generator.
- In the below example, there are three generator functions, the first two generator functions `one_gen` and `two_gen` yields two values each and third generator function `all_gen` yields all the values from both `one_gen` and `two_gen` along with its own values.

```
def one_gen():
    yield "one"
    yield "two"

def two_gen():
    yield "five"
    yield "six"

def all_gen():
    yield from one_gen()
    yield "three"
    yield "four"
    yield from two_gen()

all_vals = all_gen()

for i in all_vals:
    print(i)
```

- `close()` function - The close function closes the execution of the generator object.
- In the code below, the `close_gen` generator function yields values from 1 to 5, we yield first two values and close the generator, and if we try to yield the value this time, it will return Stop Iteration Error since the execution has been stopped.

```
def close_gen():
    for i in range(1,6):
        yield i

gen = close_gen()

print(next(gen)) # 1
print(next(gen)) # 2

gen.close() # Closes the execution

print(next(gen)) # Returns Stop Iteration error instead of 3
```