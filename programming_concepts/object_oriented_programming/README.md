# Object-Oriented Programming (OOP) in Python

## Overview
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. In OOP, objects are instances of classes, and these objects can hold data (attributes) and have behaviors (methods) that operate on that data.

OOP in Python allows developers to model real-world entities, which makes it easier to structure, maintain, and scale applications. OOP is based on four main principles: **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**.

This guide covers the core principles of OOP in Python and provides examples to help you understand how to implement these concepts in your own projects.

## Core Principles of OOP



### 1. Inheritance


Inheritance is the process by which one class (child class) acquires the attributes and methods of another class (parent class). It helps in reusing code and building more specialized classes from generic ones.



In this example, we have a parent class Vehicle and a child class Car. The Car class inherits the attributes and methods from the Vehicle class and can also have its own specific behavior.


#### Example:
```python

# Parent class (Vehicle)
class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand  # private att```python
Example:ribute
        self.__model = model  # private attribute

    def get_brand(self):
        return self.__brand  # controlled access to private attribute

    def get_model(self):
        return self.__model  # controlled access to private attribute

    def move(self):
        print(f"{self.__brand} {self.__model} is moving")

# Child class (Car) inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)  # Calling parent class constructor
        self.color = color  # Specific attribute for Car class

    def honk(self):
        print(f"{self.get_brand()} {self.get_model()} is honking")

    def car_details(self):
        return f"{self.get_brand()} {self.get_model()} of {self.color} color"

# Usage
car = Car("Toyota", "Camry", "Red")
car.honk()  # Calls the honk method
car.move()  # Calls the inherited move method
print(car.car_details())  # Calls car_details method to display car details


### 1. Encapsulation
Encapsulation refers to the bundling of data and methods that operate on the data into a single unit called a class. It also involves restricting access to certain components of an object to prevent misuse and accidental modification of its internal state.
## Overview
In Python, encapsulation is achieved by using access modifiers such as public, private, and protected. By default, all attributes in Python are public. To make an attribute private, you can prefix it with double underscores .

#### Example:
class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand  # private attribute
        self.__model = model  # private attribute

    def get_brand(self):
        return self.__brand  # controlled access to private attribute

    def set_brand(self, brand):
        self.__brand = brand  # controlled access to private attribute

    def get_model(self):
        return self.__model  # controlled access to private attribute

    def set_model(self, model):
        self.__model = model  # controlled access to private attribute

    def move(self):
        print(f"{self.__brand} {self.__model} is moving")

# Usage
vehicle = Vehicle("Toyota", "Camry")
print(vehicle.get_brand())  # Output: Toyota
vehicle.set_brand("Honda")
print(vehicle.get_brand())  # Output: Honda

