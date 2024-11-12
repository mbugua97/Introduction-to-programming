#Abstaraction -is a concept in oop that focuses on hiding complex implementation 
#it allows us to create clear and simplified interface so users can interact with objects without knowing the underlying complexity

#example on abstraction

#modules- is a file containing python code/such as functions ,classes and Variables

from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self,account_number):
        self.__account_number=account_number #'_'protected attribute
        self.__balance=0.0    #private attribute
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print(f"deposited ${amount},New balance:${self.__balance}")
        else:
            print("deposit amount must be positive")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdrew:${amount} New balance:{self.__balance}")
        else:
            print(f"Insufficient funds in account")

class SavingsAccount(BankAccount):
   pass

account=SavingsAccount('1234')

account.deposit(100)
account.withdraw(200)
print(account)
