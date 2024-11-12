# #inheritance
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def ShowPersonDetail(self):
#         return f"Hello my name is {self.name} and i am {self.age} years old"


# class Child(Person):#we want to inherit attributes of the Person class
#     def __init__(self,childName,childAge,childsParent):
#         #we call the parent class constractor to inherit the Person attribute
#         super().__init__(childsParent.name,childAge)
#         self.childName=childName
#         self.childsParent=childsParent
#     def showChildDetail(self):
#         return f"hello, i am {self.childName},and my parent is {self.name}"


# parent=Person("john",40)#parent object
# child=Child("joseph",10,parent)#child object is inheriting the parents attributes 

# print(child.showChildDetail())

class Animal: #parent class animal
    def speak(self):
        print("animal is speaking")

class Dog(Animal): #child class Dog {inheriting the attributes of speak from the parent class}
    def speak(self):
        super().speak()#executes the speak method from the parent
        print("Woof!,Woof!") 

my_dog=Dog()#object from the child
my_dog.speak()


# why use Super?
# 1. you can call the parent method and constractor without duplicating code thus maintaining {D.R.Y} and clean code