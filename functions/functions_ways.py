# Functions

# No Argument, No return

def check_status():
    status = 'active'
    if status == 'active':
        print("Machine is Active")

check_status()

# No Arguments, return statement

def check_status():
    status = 'active'
    if status == 'active':
        return "Status is Active"

message = check_status()
print(message)

# Arguments without return statement

def check_status(status):
    if status == 'active':
        print("Status is Active")

check_status("active")

# Arugments with return statement

def check_status(status):
    if status == 'active':
        return "Status is Active"

message = check_status("active")
print(message)

# Positional Arguments

def input_data(name, age, gender):
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Gender:{gender}")

input_data("Rajesh",23,"Male")

# Keyword Arguments

def input_data(name, age, gender):
    print(f"Name:{name}")
    print(f"Age:{age}")
    print(f"Gender:{gender}")

input_data(name="Rajesh",age=23,gender="Male")

# Multiple return statements

age = 24

def eligibility_checker():
    if age >= 18:
        return "Eligible"
    return "Not Eligible"

result = eligibility_checker()
print(result)

# Multiple values returned by return statement

def multi_return():
    return 1, 2, 3

a, b, c = multi_return()
print(a)
print(b)
print(c)

# Functions with arbitrary number of parameter

# Arbitrary Parameter -> used when number of arguments are not known

def multi_params(*numbers):
    return f"List of Numbers: {numbers}"

result = multi_params(1,2,3,4,5,6)
print(result)

def multi_params(single,*numbers):
    return single,f"List of Numbers: {numbers}"

single_num,result = multi_params(1,2,3,4,5,6)
print(single_num,result)

def multi_params(*numbers,single): # Always use regular argument before arbitrary arguments
    return single,f"List of Numbers: {numbers}"

single_num,result = multi_params(1,2,3,4,5,single=6)
print(single_num,result)

# Arbitrary Keyword Arguments -> Works like Arbitrary Arguments

def multi_kw_params(**details):
    return details

result = multi_kw_params(name="rajesh",age=34,gender="Male",course="computer")
print(result)