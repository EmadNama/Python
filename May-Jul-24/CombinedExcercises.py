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
print(repeated_words("emad emad hello hello my"))