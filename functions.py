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


def division(numbers, x): #division check
    list=[] #for the numbers that can be divided by x
    for i in numbers:
        if i%x==0:
            list.append(i)
    return list

list = [2,4,6,5,7,9]
x = 2

print(division(list, x))
