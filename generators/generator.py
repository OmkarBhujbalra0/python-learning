# Generators

def generate():
    yield "Result One"
    yield "Result Two"
    yield "Result Three"

res = generate() # Create generator object

for i in res:
    print(i) # Result One  Result Two  Result Three

# print(next(res)) # StopIteration Error since generator is not iterating any more values.

res2 = generate() # Create new generator object
print(next(res2)) # Result One
print(next(res2)) # Result Two

print(res)

# send() function -> inputs data in the generator 

def input_gen():
    while True:
        input_data = yield
        print(f"Your input: {input_data}")

input_obj = input_gen()

print(next(input_obj))

input_obj.send("My First Input")

# yield from -> yields all the values from another generator

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

# close() -> closes the execution of the generator object

def close_gen():
    for i in range(1,6):
        yield i

gen = close_gen()

print(next(gen))
print(next(gen))

gen.close() # Closes the execution

# print(next(gen)) # Returns error since the execution has been stopped.