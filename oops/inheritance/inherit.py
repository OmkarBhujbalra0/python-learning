# Inheritance

class College:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"The student {self.name} is {self.age} years old")
        
class Student(College):
    def autobio(self):
        print(f"My name is {self.name} and my age is {self.age}.")
        
s1 = Student("Raj",35)
print(s1.name)
print(s1.age)

s1.display()
s1.autobio()

# Two init constructors in two classes

class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        print("Vehicle Class is Executed")
    
    def display(self):
        print(f"The brand of Vehicle is {self.brand} and color is {self.color}.")

class Car(Vehicle):
    def __init__(self,wheel_count,type_):
        self.wheel_count = wheel_count
        self.type = type_

        print("Car Class is executed.")
    
    def type_display(self):
        print(f"Car details printed successfully!")

s1 = Car(4,"Car")
print(s1.wheel_count)
# print(s1.color)

# Inheritance using explicit call

class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        print("Vehicle Class is Executed")
    
    def display(self):
        print(f"The brand of Vehicle is {self.brand} and color is {self.color}.")

class Car(Vehicle):
    def __init__(self,brand,color,wheel_count,type_):
        Vehicle.__init__(self,brand,color)
        self.wheel_count = wheel_count
        self.type = type_

        print("Car Class is executed.")
    
    def type_display(self):
        print(f"Car details printed successfully!")

s1 = Car("Storm","Blue",4,"Car")
print(s1.wheel_count)
print(s1.color)

# Inheritance using super() function

class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        print("Vehicle Class is Executed")
    
    def display(self):
        print(f"The brand of Vehicle is {self.brand} and color is {self.color}.")

class Car(Vehicle):
    def __init__(self,brand,color,wheel_count,type_):
        super().__init__(brand,color)
        self.wheel_count = wheel_count
        self.type = type_

        print("Car Class is executed.")
    
    def type_display(self):
        print(f"Car details printed successfully!")

s1 = Car("Storm","Blue",4,"Car")
print(s1.wheel_count)
print(s1.color)

# Method Resolution Order

class Vehicle():
    def display(self):
        print("This is printed from Vehicle Class")
 
class Driver():
    def display(self):
        print("This is printed from Driver Class")

class Car(Vehicle, Driver):
    pass 
 
s1 = Car()
s1.display()

print(Car.__mro__)