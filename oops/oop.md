# Object Oriented Programming

Object Oriented Programming is a paradigm where core ideas is to use objects which allows you to reuse the code and works with attributes and methods of the objects.

## Class

Class is basically a blueprint to create objects.
- In Python, you can create a class using `class` keyword.
- In the below example, we have created `Student` class with two attributes(variables) `name` and `age`, we can access the attributes of the class by `Student.name` and `Student.age`.

```
class Student:
    name = "Rajesh"
    age = 35
    
print(Student.name) # Rajesh
print(Student.age) # 35
```

## Object

Object is basically instance of a class.
- In the code below, we have created an object `props` and accessed its attributes.
```
class Car:
    brand = "Storm"
    color = "Blue"
    
props = Car()

print(props.brand)
print(props.color)
```

You can also add attributes to objects.
- In the code below, the class `A` actually contains 2 attributes `name` and `age`, we create an object `s1` and create an attribute `year` for object `s1`.
- We can access the attribute `year` from object `s1` but not from original class `A`, since class `A` doesn't have attribute `year`.
```
class A:
    name = "ram"
    age = 23
    
s1 = A()

print(s1.name) # "ram"
print(s1.age) # 23

print(A.name) # "ram 

s1.year = 2003 # Adding an attribute outside the object.
print(s1.year) # 2003
print(A.year) # AttributeError since the attribute is added to object s1 not the original class A
```

## self parameter

The `self` parameter is parameter that provides reference of the current object(instance) of the class.
- In the code below, we have created a class `Fruits` with a method (function defined inside the class) `input_name` with `self` and `name` parameters passed to it.
- We create two objects `s1` and `s2` from Fruits and pass the arguments to them.
```
class Fruits:
    def input_name(self,name):
        self.name = name
        
s1 = Fruits()
s2 = Fruits()

s1.input_name("Apple")
print(s1.name) # Apple

s2.input_name("Banana")
print(s2.name) # Banana
``` 

What if we don't use self parameter?
- In the below example, we are creating a class `Screen` containing display method, now the problem is there is no `self` parameter, due to which the method doesnt get the reference of the current object `s1` and it raises error.
Note - The methods need the reference of the object to work with, and it expects the reference as parameter, that's why `self` parameter is used.
```
class Screen:
    def display():
        print("This will not be printed due to error")
        
s1 = Screen()

s1.display() # returns error since the class except self parameter for passing the reference of the object
``` 

