# #functions

# #pi*r*r*h

# def volume(height,radius):#function declaration
#     """function body"""
#     pi=3.142
#     calculatedVolume=pi*radius*radius*height
#     return calculatedVolume


# my_vol=volume(10,7) #function call
# print(my_vol)


# # Only use ordinary letters, numbers and underscores in your function names. They can’t have spaces, and need to start with a letter or underscore.
# # You can’t use Python's reserved words or keywords for function names, as discussed earlier with variable names. Here again is that table of Python's reserved words(opens in a new tab).
# # Try to use descriptive names that can help readers understand what the function does.


# """"print vs return in functions"""

# def _sayHello(message):
#     print("say hello")

# def ReturnHello(mesage):
#     return mesage


# my_message=_sayHello("hello world")#function call
# print(type(my_message))

# # variable scope
# #local variable & global variables


# #example of a global variable
# my_var="this is my global variable"

# def myFunction():
#     word="hello"    #example of a local variable
#     print(my_var)

# def MyFuction2():
#     print(my_var)
#     #print(word)

# MyFuction2()


# egg_count=0 #global variable

# def buy_eggs(count):
#     egg_count=count*12
#     print(f"your egg count is {egg_count} in the function block")
#     return None

# buy_eggs(1)

# print(f"your egg count is {egg_count}")


#function to check if a numer is odd or even
# def CheckNumber(number):
#     if number%2==0:
#         print("your number is an even number")
#     else:
#         print("your number is odd")

# CheckNumber(3)

def multiply(x,y):
    return x*y
resalt=multiply(2,4)
print(resalt)


#lambda functions
stillMultiply=lambda x,y:x*y
stillMultiply(2,4)

