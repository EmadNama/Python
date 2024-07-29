# def CalcMulList(xlist):
#     res = 1
#     for i in xlist:
#         res*=i
#     return res
#
# list = []
# while True:
#     number = int(input("Please enter a number: "))
#     if number<0:
#         print(list)
#         break
#     list.append(number)
#
# m = CalcMulList(list)
# print(f"The multiplication of all numbers is: {m}")

def Palindrome(str): #a function that checks a word if it is a palindrome with statement of True/False
    return str == str[::-1]

points = 15 #begin points
listwords = [] #used words

print("""Welcome to the Palindrome game!
For each Palindrome word you enter, you get 10 points.
If it wasn't a Palindrome word, you lose 5 points.
You start with 15 points""")

while True:
    word=input("Put a word: ")
    for i in listwords: #check if the word is used before
        while word == i:
            print("You already used this word, Try another!")
            word = input("Put a word: ") #asks again
    if Palindrome(word):
        points+=10
        print(f"Word is Palindrome, you now have {points}")s
        listwords.append(word) #adds the word to the list
    else:
        points-=5
        print(f"Word is not Palindrome, you now have {points}")


    if points<=0:
        print("You've lost!")
        break
    if points>=100:
        print("You've won!")
        break