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

######################################## dictionaries and tuples ############################################


dictionary = {"Alice": 72, "Bob": 81, "Edward": 94}

for student, grade in dictionary.items():
    print(f"{student, grade}")