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
# print(A.year)

# self parameter

class s:
    def display(self):
        print("Apple")

s1 = s()
s.display(s1)

# Without self parameter

class Screen:
    def display():
        print("This will not be printed due to error")
        
s1 = Screen()

# s1.display() # returns error since the class except self parameter for passing the reference of the object