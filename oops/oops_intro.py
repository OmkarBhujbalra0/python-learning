# Class

class Car:
    brand = "Storm"
    color = "Blue"

print(Car.brand)
print(Car.color)

# Objects

props = Car()
print(props.brand)
print(props.color)

# Creating attributes outside of the class

Car.year = 2014
props.year = 2018
print(Car.year)
print(props.year)

class A:
    name = "ram"
    age = 23
    
s1 = A()

print(s1.name) # "ram"
print(s1.age) # 23

s1.year = 2003 # Adding an attribute outside the object.
print(s1.year)
print(A.name)
print(A.year)