#inheritance we in heriting the attributes



#parent class 
class Vehicle:
    def __init__(self,brand): #brand as attribute/argument
        self.brand=brand
    def move(self):
        print(f"{self.brand} is moving")

#child 
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def honk(self):
        print(f"{self.brand},{self.model} is honking")
    
# Creating an object of the Car class, passing brand and model
car = Car("Toyota", "Camry")  # Pass the brand and model separately

car.honk()