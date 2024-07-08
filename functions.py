#פונקציה len

# def mystrlen(str): #function that calculates a string length
#     letterscount=0
#     for i in str:
#         if i==" ":
#             continue
#         letterscount+=1
#     return letterscount
#
#
# while True:
#     str=input("Input a word: ")
#     print(mystrlen(str))


# def division(numbers, x): #division check by x for the numbers in a list
#     list=[] #for the numbers that can be divided by x
#     for i in numbers:
#         if i%x==0:
#             list.append(i)
#     return list
#
# list = [2,4,6,5,7,9]
# x = 2
#
# print(division(list, x))


# def SimanKreaah(str): #checks if a string has only one "!" in it.
#     count=0
#     for i in str:
#         if i == "!":
#             count+=1
#     if count==1:
#         return True
#     else:
#         return False
#
#
# while True:
#     str=input("Put a string: ")
#     print(SimanKreaah(str))


# def startswithupper(str): #checks if a string starts with an upper letter
#     return str[0].isupper()
#
# while True:
#     str=input("Put a string: ")
#     print(startswithupper(str))


# def digitcheck(str): #checks if a string has between 1-3 digits only
#     count=0
#     for i in str:
#         if i.isdigit()==True:
#             count+=1
#     return 1<=count<=3
#
# while True:
#     str = input("Put a string: ")
#     print(digitcheck(str))


