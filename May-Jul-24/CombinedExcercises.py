#Sunday, 4th of Aug, 2024


#Task 1: A function that swap letter case from small to capital and vice versa


# def toggle_case(string):
#     new_string = ""
#     for letter in string:
#         if letter.isupper():
#             new_string += letter.lower()
#         else:
#             new_string += letter.upper()
#     return new_string
#
# string = "Em2342Ad"
# print(toggle_case(string))


#Task 2: A function that returns a list with only prime numbers


# def is_prime(num): #function that checks a specific number
#     if num <= 1:
#         return False
#     for i in range (2, num):
#         if num%i == 0:
#             return False
#     return True
#
# def prime_list(list): #list check
#     new_list = []
#     for number in list:
#         if is_prime(number):
#             new_list.append(number)
#     return new_list
#
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(prime_list(list))


#Task 3: Function that checks a range of a number and returns Fizz for numbers that divide 3, and FizzBuzz for 5



# def FizzBuzz(num):
#     for i in range(1, num+1):
#         if i%3 == 0 and i%5 == 0:
#             print("FizzBuzz", end=" ")
#         elif i%3 == 0:
#             print("Fizz", end=" ")
#         elif i%5 == 0:
#             print("Buzz", end=" ")
#         else:
#             print(i, end=" ")
#
#
# FizzBuzz(15)


# Task 4: A function that recieves a text and returns the longest word in it


# def highest_len(text):
#     temp = text.split()
#     length = 0
#     longest = " "
#     for word in temp:
#         if len(word)>length:
#             length = len(word)
#             longest = word
#     return longest
#
# text = "Hello this is the longestword"
# print(highest_len(text))


#Task 5: A function that returns numbers that exist even times


# def func(list):
#     sum = 0
#     for number in list:
#         if list.count(number) % 2 == 0:
#             sum += number
#     return sum
#
# list = [2,2,2,4,4,1,1,1,1,5]
# print(func(list))


#Task 6: a function that returns the letter with the highest count in a string


# def letter(str):
#     count = 0
#     letter = ""
#     for i in str:
#         if str.count(i) > count:
#             count = str.count(i)
#             letter = i
#     return letter
#
# print(letter("Helllooo"))


#Task 7: primes between two numbers


# def is_prime(num): #function that checks a specific number
#     if num <= 1:
#         return False
#     for i in range (2, num):
#         if num%i == 0:
#             return False
#     return True
#
# def primes_between(num1, num2):
#     list = []
#     for number in range (num1,num2):
#         if is_prime(number):
#             list.append(number)
#     return list
#
# print(primes_between(1,20))


#Task 9: make a function that gets a string and returns the longest word that starts with a specific letter


def highest_len(text, letter):
    temp = text.split()
    length = 0
    longest = " "
    for word in temp:
        if word.startswith(letter) and len(word)>length:
            length = len(word)
            longest = word
    return longest

print(highest_len("my mye myeye mo myeyi emadasdkaskd", "m"))


#Task 10:


# def GetDict(d): #a function that recieves a dict of students and their grades and returns a dict with the students and their average
#     newDict = {}
#     for key in d:
#         avg = sum(d[key])/len(d[key])
#         newDict[key]=avg
#     return newDict
#
# dictionary = {"emad":(70,80,90), "itay":(78,85,80)}
# print(GetDict(dictionary))


#Task 13: write a function that gets a text and returns the words that appear more than once


def repeated_words(text):
    list_words = text.split()
    for word in list_words:
        if list_words.count(word) > 1:
            return word
print(repeated_words("emad emad hello hello my"))



# tasks in loops, conditions, lists and dictionaries.
# 26/08/2024

# task 1

def func1(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num ** 2)
        else:
            new_list.append(num)
    return new_list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(func1(list))


# task 2

def func2(dict):
    for product, price in dict.items():
        if price > 100:
            dict[product] = price * 0.90
        else:
            dict[product] = price
    return dict


dict = {
    "cola": 10,
    "rice": 50,
    "meat": 200
}

print(func2(dict))


# task 3

def func3(list):
    x = 0
    y = ""
    for word in list:
        if len(word) > x:
            x = len(word)
            y = word
    return y


list = ["lnflsd", "emad", "helloeveryone", "test"]
print(func3(list))


# task 4

def func4(list):
    dict = {}
    for num in list:
        dict[num] = "Even" if num % 2 == 0 else "Odd"
    return dict


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(func4(list))


# task 5

def func5(list):
    list_students = []
    for dict in list:
        for name, grade in dict.items():
            if grade >= 75:
                list_students.append(name)
    return list_students


list = [
    {"Emad": 75},
    {"Itay": 90},
    {"Adar": 60, "Lidor": 70},
    {"Gal": 80, "Atar": 40}
]

print(func5(list))


# task 6:

def func6(list):
    new_list = []
    for word in list:
        if word.startswith("A") or word.startswith("a"):
            new_list.append(word)
    return new_list


list = ["adar", "Adar", "Emad", "ability", "sami shamoon"]
print(func6(list))


# task 7:

def func7(dict):
    studentaverage = 0
    studentname = ""
    for student, grades in dict.items():
        x = sum(grades)
        average = x / len(grades)
        if average > studentaverage:
            studentaverage = average
            studentname = str(student)
    return studentname


dict = {
    "Emad": [10, 20, 30],
    "Adar": [30, 40, 50],
    "Lotem": [5, 10, 15]
}

print(func7(dict))


# task 8:

def func8(list):
    new_list = []
    for num in list:
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
        if flag == True:
            new_list.append(num)
    return new_list


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(func8(list))


def func9():
    list = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            list.append("FizzBuzz")
        elif num % 3 == 0:
            list.append("Fizz")
        elif num % 5 == 0:
            list.append("Buzz")
        else:
            list.append(num)
    return list


print(func9())


# task 10:

def func10(string):
    new_dict = {}
    for letter in string:
        new_dict[letter] = string.count(letter)
    return new_dict


string = "aaaaa"
print(func10(string))