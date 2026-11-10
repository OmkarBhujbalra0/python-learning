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