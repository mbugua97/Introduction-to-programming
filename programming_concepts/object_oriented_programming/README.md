# Object-Oriented Programming (OOP) in Python

## Overview
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. In OOP, objects are instances of classes, and these objects can hold data (attributes) and have behaviors (methods) that operate on that data.

OOP in Python allows developers to model real-world entities, which makes it easier to structure, maintain, and scale applications. OOP is based on four main principles: **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**.

This guide covers the core principles of OOP in Python and provides examples to help you understand how to implement these concepts in your own projects.

## Core Principles of OOP

### 1. Encapsulation
Encapsulation refers to the bundling of data and methods that operate on the data into a single unit called a class. It also involves restricting access to certain components of an object to prevent misuse and accidental modification of its internal state.

In Python, encapsulation is achieved by using access modifiers such as public, private, and protected. By default, all attributes in Python are public. To make an attribute private, you can prefix it with double underscores (`__`).

#### Example:
```python
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
