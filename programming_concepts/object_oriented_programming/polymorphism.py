#inheritance,
#polymorphism
#abstraction
#encapsulation


#polymorphism/{"many forms"}-refers to the ability of different classes to be treated as instances of the same class through a common interface
# in simpler terms it allows us to have different classes with  same method name that can be called through a common interface
#example Demonstartation

#Base class



#parent class
class Animal:
    def sound(self):
        return "Some generic animal sound"
    
#derived classes
class Dog(Animal):
    def sound(self):
        return "Bark" #overiding the sound method
    
class Cat(Animal):
    def sound(self):
        return "Meow"


#instances Objects

my_dog=Dog()
my_cat=Cat()

print(my_dog.sound())
print(my_cat.sound())

animals=[Dog(),Cat(),Animal()]
for animal in animals:
    print(animal.sound())