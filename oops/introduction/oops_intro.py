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
Screen.display() # The display method will be executed and the message will be printed since the method is directly accessed from class.
# s1.display() # returns error since the class except self parameter for passing the reference of the object

# init constructor

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"Student Name is {self.name} and age is {self.age}."

s1 = Student("Rajesh",35)
print(s1.display())
print(s1.name)
print(s1.age)


# without init

class Noinit:
    def display(self,amount):
        self.amount = amount

s1 = Noinit()
# print(s1.amount) # Returns error since the attribute amount does not exists
s1.display(45) 
print(s1.amount) # Returns 45 since the attribute is now defined using display method

# Instance Methods

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

s1 = Person("Raj",45) 
s1.display() # Instance Method

# Static Method

class statics:
    @staticmethod
    def add(age):
        if age > 18:
            print("Eligible")
        else:
            print("Not eligible")

statics.add(34)
