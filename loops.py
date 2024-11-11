# # # for loops

# # list_fruits=['banana','apple','mango','grapes','tommato']


# # for fruit in list_fruits:
# #     print(fruit)

# # #range(min,max,step)


# # #memory leak


# # for i in range(0,100):
# #     if i<20:
# #         print(i)


# # #
# # # while loops

# my_list=[4,11,8,5,13,2]


# for i in range(0,5):
#     print(my_list[i])

# added_values=0
# i=0

# #while (condition):
# #   execute

# a=1
# b=(a>1)

# while (added_values<20):
#     added_values+=my_list[i]
#     i+=1





# #Break and continue


# #quiz -print even numbers in the range 0-100 using while,continue
# # for number in range(1,51):
# #     if number %2==0:
# #         print(number)
# #     else:
# #         continue

# break
savedPassword='password'
passwordCount=0
while True:
    print(f"your password count is {passwordCount}")
    if passwordCount<3:
        passwordCount+=1
        password=input("what is your password")
        if password==savedPassword:
            break
        else:
            continue
    else:
        break




