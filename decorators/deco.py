# Decorators

def extra(func):
    def inner():
        print("One")
        print("Two")
        func()
    return inner

@extra
def third():
    print("Third")

third()

# Passing arguments inside decorators

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

a = addition(34,51,12)

print(a)