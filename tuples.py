#tuple- collection of elements nad tuples are immutable

my_tuple=(1,2,3,4,"apple",4.7,True,("ugali","chapo"))

empty_tuple=()

#creating a single element tuple
single_elemnt_tuple=(42,)

print(my_tuple[0]) #expect 1
print(my_tuple[-1])

print(my_tuple[0:4])

#modifying 
new_tuple=my_tuple+(9,)

print(new_tuple)

#counting occurence
print(my_tuple.count(3))

print(my_tuple.index(3))