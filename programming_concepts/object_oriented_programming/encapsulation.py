#encapsulation-it refers to the concept of bundling data(attributes)and methods(functions) that operate data in  a single unit

class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    
    #getter method
    def get_name(self):
        return self.__name
    
    #setting function
    def setName(self,name):
        self.__name=name

    def get_Age(self):
        return self.__age
    
    #setting function
    def setAge(self,age):
        self.__name=age

    
person1=Person("John",20)
print(f"{person1.get_name()}")

#modification

person1.setName("mbugua")
person1.setAge=22


print(person1.get_name())
