# Decorators

Decorators are the functions that allows you to add extra features to the functions without changing the anything in the original code.
- In the code below, we define a decorator `extra` with parameter as `func` within which we create a a wrapper function which prints two lines and calls the `func` parameter, so whenever the `extra` decorator code is run, the wrapper function inner_fun is returned by it which contains extra features( just like printing 2 lines).
- Then we pass the function `third()` to the extra decorator using `@extra` which is same as writing `third = extra(third)`, then we define the function third() below it which prints a line.
- When we call the function third(), it prints three lines instead of only one, since it is passed to the decorator.

```
def extra(func):
    def inner_fun():
        print("First printing call")
        print("Second printing call")
        func()
    return inner_fun() 

@extra
def third():
    print("Third printing call")

third() # First printing call -> Second printing call -> Third printing call
```

## Passing Arguments in Decorators

- You can also pass values along with the function inside decorator.
- In the below example, the decorator `system` consist of a wrapper function `wrap` which takes parameters from the function that will be passed to the decorator and the wrapper function will return the result of execution done by the function passed to the decorator.
- Here, the wrapper function wrap will return the result of `addition` function which adds all the parameters passed to it.
```
def system(func):
    def wrap(*args):
        print(f"Starting the func {func.__name__}")
        result = func(*args)
        print(f"func {func.__name__} execution is complete.")
        return result
    return wrap 

@system
def addition(a,b,c):
    return a + b + c

a = addition(34,51,12) # Starting the func addition -> func addition execution is complete.

print(a) # 97
```
