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