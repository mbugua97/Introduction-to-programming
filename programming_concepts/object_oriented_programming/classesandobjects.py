#class is a blueprint for creating objects,it defines a set of attributes and methods that the created object will have

#Template 
# class ClassName:#class declaration
#     #class attributes
#     class_atrribute='value'

#     def Method_name():
#         #method block



# class Dog:
#     species='canis lupus'
#     def __init__(self,name,age):
#         print("the constractor is called")
#         self.name=name #instance attribute
#         self.age=age #instance attribute

#     def bark(self): #self is a special parameter in a class method that refers to the instance of the class itself
#         print("the class method is called")
#         return f"says woof!"
    
# #object- an object is an instance of a class (my_dog)
# my_dog=Dog("Buddy",5)
# print(my_dog.age) #acces instance attribute age
# print(my_dog.name) #acces instance attribute name


#dry
# code reusability

# class Car:
#     #constractor
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.speed=0

#     #method
#     def accelerate(self,speed):
#         self.speed+=speed
#         return f"The {self.make} {self.model} has accelerated to {self.speed} "
    
#     #method
#     def brake(self,decelerate):
#         self.speed-=decelerate
#         return f"the {self.make} slowed down to {self.speed}"
    
#     #method
#     def displaySpeed(self):
#         return f"the speed is {self.speed}"
    
# my_car=Car("Toyota","Camry",2024)
# print(my_car.displaySpeed())#speed is at 0
# print(my_car.accelerate(5)) #accelerate by 5
# print(my_car.displaySpeed()) #new speed of 5
# print(my_car.accelerate(15)) #increment speed by 15
# print(my_car.displaySpeed())
# print(my_car.brake(10))
# print(my_car.displaySpeed())

# my_car2=Car("mercedes","c200",2015)
# print(my_car2.displaySpeed())
# print(my_car2.accelerate(10))
# print(my_car2.displaySpeed())


class Book:
    #constructor
    def __init__(self,title,page):
        self.title=title
        self.page=page

    def showBookDetail(self):
        return f"your book title is {self.title} with {self.page} pages"


my_book_1=Book("blossoms of the savanna",900)#object declaration
my_book_2=Book("1984",900)#object declaration
my_book_3=Book("The midnight library",1000)#object declaration
my_book_4=Book("kigogo",600)#object declaration
my_book_5=Book("circle",1200)#object declaration



print(my_book_1.showBookDetail())#method call for my_book_1 object
print(my_book_5.showBookDetail())
