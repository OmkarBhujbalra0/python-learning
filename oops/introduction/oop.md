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

Note - self is not a keyword so you can use any word (not a keyword) as self parameter but the reason we usually use self parameter is because its a convention of writing parameter to pass the object reference.

What if we don't use self parameter?
- In the below example, we are creating a class `Screen` containing display method, now the problem is there is no `self` parameter, due to which the method doesnt get the reference of the current object `s1` and it raises error.
Note - The methods need the reference of the object to work with, and it expects the reference as parameter, that's why `self` parameter is used.
- The `Screen.display()` will execute the method since the method is directly accessed from class without using any object.

```
class Screen:
    def display():
        print("This will not be printed due to error")
        
s1 = Screen()
Screen.display() # This method will be executed since the method is now directly accessed from class

s1.display() # returns error since the class except self parameter for passing the reference of the object
``` 

## init constructor

init constructor is special method that initializes the object in the class.
- You don't need to call init constructor like other methods, it is executed automatically when object is created.
- The self parameter is passed in init constructor to pass the object reference to work with.
- init constructor allows you to input the data to work with during creation of object, instead of manually inputting the data after creating object.

```
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        return f"Name of Student {self.name} and age is {self.age}."
```

## without init 

- In the code below, the class `Noinit` does have init constructor due to which you cannot input data while creating the object at the same time, so you have to run the `adder` method which takes `self` and `amount` as a parameters and inputs data into the parameter amount.
- Unless you don't call `adder` method with argument, there is no attribute called `amount`
```
class Noinit:
    def adder(self,amount):
        self.amount = amount
        
s1 = Nonit()
print(s1.amount) # Attribute doesn't exist

s1.display(345) 
print(s1.amount) # 345
```

Methods that works with objects are called as `Instance Methods`.
To work with instance methods you have to create object first.
The instance methods works on data passed by objects separately.

## Static Methods

Static Methods are the methods that are used in classes without any need of using object or class data.
You can explicitly pass object or class data in static methods, but usually the static methods are used with class.
As it does not need to work with object data, you don't need to create object to access static methods.

```
class statics:

    @staticmethod
    def add(age):
        if age > 18:
            print("Eligible")
        else:
            print("Not eligible")

statics.add(19) # prints Eligible
```

## Class Methods

Class Methods are methods that allows you to use attributes that are defined in the class.
- It uses `cls` parameter to pass the class as an argument.
- In the below example, the class `Cl` contains attribute `name`, which contains class method display which uses `cls` as a parameter and `name` as argument to pass new value during method call.
```
class Cl:
    name = "Raj"

    @classmethod
    def display(cls,name): # the class itself is passed as argument
        cls.name = name # the argument name is changed 

Cl.display("raman") 
print(Cl.name) # Accessed value of the attribute
```