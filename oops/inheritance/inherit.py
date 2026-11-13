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