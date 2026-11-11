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
