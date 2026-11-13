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

