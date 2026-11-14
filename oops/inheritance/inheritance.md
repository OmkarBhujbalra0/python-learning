# Inheritance

Inheritance is phenomenon that allows one class to use attributes and methods from another class.
- A class that inherits from another class is Child Class.
- A class from which another class inherits is Parent Class

Let's understand this with an example.
- The code below consists of parent class `College` and child class `Student`, the `Student` class inherits attributes and methods from parent class `College` and also use its methods on inherited attributes.
- When you create object from `Student` class, you can use both methods, one method from class `College` (`display`) and another method from class `Student` (`autobio`).
```
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
```

## Accessing attributes from Parent Class init constructor

- As you have seen above you can access the attributes from parent class init constructor, but there is one thing to keep in mind.
- If child class also have init constructor, then init constructor in child class will override the init constructor of parent class.
- Let's understand this with an example.

- In the example below there are 2 classes Vehicle and Car, in Vehicle we have 2 attributes brand and color defined in init constructor along with a print statement, which will print the message when the init constructor in class Vehicle is triggered.
Along with that, there is display method which prints a message containing model and color of vehicle.
- Another class is Car, which has its own init constructor where 2 attributes wheel_count and type_ are defined along with print statement which will print the message.
- Since the Car is child class and Vehicle parent class, the init constructor in class Vehicle will be overrided due to which, attributes like brand and color will not be passed to class Car and print statement in init constructor of class Vehicle will not print any message.
- When you create an object from class Car, you can pass only 2 arguments for 2 parameters wheel_count and type, and the print statement in class Car will print the message.
- You will also only be able to access the attributes that are present only in class Car.

```
class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand # This will not be passed
        self.color = color # This will also not be passed
        print("Vehicle Class is Executed") # This will not be printed
    
    def display(self):
        print(f"The brand of Vehicle is {self.brand} and color is {self.color}.")

class Car(Vehicle):
    def __init__(self,wheel_count,type_):
        self.wheel_count = wheel_count 
        self.type = type_

        print("Car Class is executed.") # Only this will be printed
    
    def type_display(self):
        print(f"Car details printed successfully!")

s1 = Car(4,"Car") # Only 2 arguments are passed for wheel_count and type attributes
print(s1.wheel_count)
print(s1.color) # Returns error since there is no attribute color in class Car
```

To prevent this problem and allow child class to accept arguments during object creation, you can do these.

## Inheritance using Explicit Call

- In the below example, the code remains same except this time we use another init constructor within init constructor in the class Car and the init constructor is also containing 5 parameters to accept 4 arguments during object creation.
- The init constructor within init constructor is explicitly calling the init constructor in Vehicle Class.

```
class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand # This will be passed
        self.color = color # This will also be passed
        print("Vehicle Class is Executed") # This will be printed.
    
    def display(self):
        print(f"The brand of Vehicle is {self.brand} and color is {self.color}.")

class Car(Vehicle):
    def __init__(self,brand,color,wheel_count,type_):
        Vehicle.__init__(self,brand,color) # This will inherit the attributes from the Vehicle class
        
        self.wheel_count = wheel_count
        self.type = type_

        print("Car Class is executed.")
    
    def type_display(self):
        print(f"Car details printed successfully!")

s1 = Car("Storm","Blue",4,"Car")
print(s1.wheel_count) # 4
# print(s1.color) # Blue 
```

## Inheritance using super() function

- The same thing can be done using super() function.

```
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
```

## Method Resolution Order

Method Resolution Order is basically the order in which the child class inherits methods or attributes from multiple parent classes.
- When there are multiple parent classes with same method or attribute names, Method Resolution Order resolves ambiguity.
- It controls which attribute or method to access first out of multiple classes having methods or attributes of same name.
Let's understand this with an example.

```
class Vehicle():
    def display(self): # This will be inherited and accessed by class Car
        print("This is printed from Vehicle Class") 
 
class Driver():
    def display(self): # This will also be inherited but not accessed.
        print("This is printed from Driver Class")

class Car(Vehicle, Driver):
    pass 
 
s1 = Car()
s1.display()

print(Car.__mro__) # prints the order in which Python searches for attributes or methods. (<class '__main__.Car'>, <class '__main__.Vehicle'>, <class '__main__.Driver'>, <class 'object'>)
```
