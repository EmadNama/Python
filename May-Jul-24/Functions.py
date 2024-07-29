#09-07-2024


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



#-------------------------10-07-2024--------------------------------------

# gradeslist = []
# gradescount = 0

# def grades(g):
#     gradeslist.append(g)

# def gradesplusten():
#     # Iterate through the list and modify grades accordingly
#     for i in range(len(gradeslist)):
#         if gradeslist[i] < 90:
#             gradeslist[i] += 10
#         else:
#             gradeslist[i] = 100
#     return gradeslist  # Return the modified grades list

# while gradescount < 10:
#     g = float(input("Enter grade: "))
#
#     # Validate the input grade
#     while not (0 <= g <= 100):
#         print("Wrong Grade! Please enter a grade between 0 and 100.")
#         g = float(input("Enter grade: "))
#
#     # Add grade to the list
#     grades(g)
#     gradescount += 1
#
# # Call the function to modify grades and print the final list
# modified_grades = gradesplusten()
# print("Modified grades list:", modified_grades)



#or :

# def getGrades():
#     grades=[]
#     count = 4
#     i = 0
#     while i<count:
#         grade = int(input("Please enter grade: "))
#         if 0<=grade<=100:
#             grades.append(grade)
#             i+=1
#         else:
#             print("Error, type again")
#
#     return grades
#
# def updateFactor(l):
#     for i in range(len(l)):
#         #l[i]=min(l[i]+10,100)
#         l[i]+=10
#         if l[i]>100:
#             l[i]=100
#
#
# def calc(l):
#     print(max(l))
#     print(min(l))
#     return sum(l)/len(l)
#
#
#
#
# l = getGrades()
# print(l)
# updateFactor(l)
# print(l)




# def divisions(): #checks a number's dividers sum, e.g in=27 out=13 (1+3+9)
#     sum=0
#     list=[]
#     number=int(input("Put a number: "))
#     for i in range(1,number):
#         if number%i==0:
#             sum+=i
#             list.append(i)
#     return sum, list
# l = divisions()
# print(l)



# def SumOfDividers(x): #checks a number's dividers sum, e.g in=27 out=13 (1+3+9)
#     sum=0
#     for i in range(1,x):
#         if x%i==0:
#             sum+=i
#     return sum
#
# def EqualCheck(x,y): #checks if a number's dividers equal a second number and vice versa.
#     if SumOfDividers(x)==y and SumOfDividers(y)==x:
#         return True
#     return False
#
# while True:
#     numberone=int(input("Put number one: "))
#     numbertwo=int(input("Put number two: "))
#     print(EqualCheck(numberone, numbertwo))



# def SumOfDividers(x): #checks a number's dividers sum, e.g in=27 out=13 (1+3+9)
#     sum=0
#     for i in range(1,x):
#         if x%i==0:
#             sum+=i
#     return sum
#
# def EqualCheck(x,y): #checks if a number's dividers equal a second number and vice versa.
#     if SumOfDividers(x)==y and SumOfDividers(y)==x:
#         return True
#     return False
#
# def ListOfCouples():
#     list=[]
#     for i in range(10, 500):
#         for j in range(i, 500):
#             if i!=j and EqualCheck(i,j):
#                 list.append([i,j])
#     return list
#
# result=ListOfCouples()
# print(result)


# OR:


# def sumOfDividers(num):
#     sum = 0
#     for i in range (1,num):
#         if num%i==0:
#             sum+=i
#     return sum
#
#
# def checkCouples(num1,num2):
#     if num1==sumOfDividers(num2) and num2 == sumOfDividers(num1):
#         return True
#     return False
#
#
#
#
# def listOfCouples(low,high):
#     l = []
#     for i in range(low,high):
#         for j in range(i,high):
#             if i!=j and checkCouples(i,j):
#                 l.append([i,j])
#                 print(l)
#     return l
#
# print(listOfCouples(100,7000))



################################################# TRAINING ##############################################################


#task 1
#function that returns a number squared

def GetSquare(num):
    return num ** 2

#task 3
#function that gets and returns a string in uppercase

def UpperCase(str):
    return str.upper()

#task 4
#a function that gets a number and returns a list for all the numbers from 1 to that number

def ListNumbers(number):
    list = []
    for num in range(1, number+1):
        list.append(num)
    return list

#task 5
#a function that gets a string and returns words count in it

def CountWords(string):
    return len(string.split())

#task 6
#gets a list of numbers and returns the average

def CalcAvg(list):
    return sum(list)/len(list)

#task 7
#gets a string and returns it opposite

def oppositestring(str):
    return str[::-1]

#task 8
#a function that checks a prime number

def PrimeNumber(number):
    if number<=1:
        return False
    for i in range(2, number):
        if number%i==0:
            return False
    return True

#task 9
#return how much letters are used in a string

def uniqueletters(str):
    list = []
    for i in str:
        if i not in list:
            list.append(i)
    return len(list)

#task 11
#return the sum of a number digits.

def DigitsCount(number):
    sum = 0
    number = str(number)
    for i in number:
        sum+=int(i)
    return sum

#task 12
#gets a number and returns it opposite

def OppositeNumber(number):
    number = str(number)
    return int(number[::-1])

#task 14
#gets a string and returns it without spaces

def ClearSpaces(str):
    return str.replace(" ", "")

#task 16
#returns all the even numbers from 1 to any specific number

def EvenNumbers(number):
    list = []
    for i in range(1, number):
        if i % 2 == 0:
            list.append(i)
    return list

#task 17
#gets a string and returns it in small letters only

def LowerCase(str):
    return str.lower()

#task 18
#unique list

def UniqueList(list):
    newList = []
    for i in list:
        if i not in newList:
            newList.append(i)
    return newList

#task 19
#gets a num and returns all the prime numbers from 0 to num

def RangePrimeNumber(num):
    list = []
    for i in range(0,num):
        if PrimeNumber(i):
            list.append(i)
    return list


#task 25
#gets a string and returns words count that start with a capital letter

def CapitalWordsCount(str):
    list = str.split()
    sum = 0
    for word in list:
        if word[0].isupper():
            sum+=1
    return sum







#PHONE BOOK

# phoneBook={'avishay':'052-1234567'}
#
# def getPhoneNumber(name,phoneBook):
#     return phoneBook.get(name,'Not founded!')
#
# def addContact(name,phone,phoneBook):
#     if name in phoneBook:
#         print('Error, name already exist!')
#     else:
#         phoneBook[name]=phone
#         print('contact added to the phonebook')
#
# def updatePhoneNumber(name,phone,phoneBook):
#     if name in phoneBook:
#         phoneBook[name]=phone
#         print("contact updated!")
#     else:
#         print("Error, there is no such name!")
#
# def searchContact(letters,phoneBook):
#     founded = []
#     for key in phoneBook:
#         if key.startswith(letters):
#             founded.append((key,phoneBook[key]))
#     return founded
#
# def deleteContact(name,phoneBook):
#     if name in phoneBook:
#         phoneBook.pop(name)
#         print('contact deleted!')
#     else:
#         print('there is no such contact!')
#
#
#
# addContact('avishay','1234',phoneBook)
# addContact('avli','054-98765432',phoneBook)
# updatePhoneNumber('jjj','053-2233221',phoneBook)
# updatePhoneNumber('eli','7776663332',phoneBook)
# print(phoneBook)
# print(searchContact('av',phoneBook))
# deleteContact('hhh',phoneBook)
# deleteContact('avishay',phoneBook)
# print(phoneBook)





# def digitcheck(number, digit): #checks a number if it contains a specific digit
#     number = str(number)
#     digit = str(digit)
#     for i in number:
#         if i==digit:
#             return True
#     return False
#
# def digitcheck(num, digit):
#     while num>0:
#         if (num%10)==digit:
#             return True
#         num//10
#     return False
#
#
# def rangecheck(low, high):
#     list = []
#     for i in range(low, high):
#         digitcheck(i, 2)
#         if digitcheck(i, 2):
#             continue
#         else:
#             list.append(i)
#     return list
# print(rangecheck(10, 11))

