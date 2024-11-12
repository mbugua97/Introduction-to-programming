#import the add function and the Multply function

#libraries are a collection of pre written code -enhasing dry concept and code reusability


#D.R.Y-code resusability



import math_opperation

from math_opperation import name,add,Hello
print(name)

result1=add(1,2)
print(result1)

say_hello=Hello("hello world")
say_hello.sayHello()


#using the math library -sqrt,pow,-
import math

number=25
result=math.sqrt(number)
pi=math.pi
print(result)
print(pi)

#import as alias
from math_opperation import divide as Dev
result_of_division=Dev(4,2)
print(result_of_division)