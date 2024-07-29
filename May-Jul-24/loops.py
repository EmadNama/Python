#תרגילי while
#Task 1

# while True:
#     avg = float(input("Put an average: "))
#     if avg==999:
#         break
#     if avg==85:
#         print("Excellent Student")
#     elif 65<=avg<=85:
#         print("Good Student")

#תרגילי while
#Task 2

# school=0
# while True:
#     payment=float(input("Payment: "))
#     if payment<0:
#         break
#     if payment>250:
#         print(f"Debts has been paid, Change is {payment-250}")
#         school+=250
#     else:
#         print(f"You have to pay first!!!!!, {250-payment} is missing")
# print(f"Today, the school has made {school}")

#תרגילי while
#Task 3

# sum=0
# failed=0
# count=0

# while True:
#     grade=float(input("Put a grade: "))
#     if not 0<=grade<=100:
#         break
#     sum+=grade
#     count+=1
#     if grade<56:
#         failed+=1
# if count > 0:
#     print(f"There are {failed} failed grades")
#     print(f"The average is {sum/count}")
# else:
#     print("No grades")

#תרגילי while
#Task 4

# count=0
# heightsum=0
# under=0
# while True:
#     height=float(input("Put the height: "))
#     if height<0:
#         break
#     if height<1.65:
#         under+=1
#     count+=1
#     heightsum+=height
#
# if count > 0:
#     print(f"{under} students under 1.65, The average height is {heightsum/count} ")

#תרגילי while2
#Task 1

# success = 0
# while True:
#     name=input("Put your name: ")
#     while name.isalpha()==False:
#         print("Wrong name")
#         name = input("Put your name: ")
#     if name=="FINISH":
#         print(f"{success} students have succeeded.")
#         break
#     grade=input("Put your grade: ")
#     while grade.isdigit()==False:
#         print("Wrong grade")
#         grade = input("Put your grade: ")
#     grade=int(grade)
#     while not 0<=grade<=100:
#         print("Wrong grade")
#         grade = float(input("Put your grade: "))
#     if grade>95:
#         success+=1

#תרגילי while2
#Task 2

# clients = 0
# mealscount = 0
# while True:
#     name=input("Put your name: ")
#     if name=="SOF":
#         print(f"{clients} clients for today!")
#         break
#     while name.isalpha()==False:
#         print("Wrong name")
#         name = input("Put your name: ")
#     clients+=1
#     meals=input("How many meals?: ")
#     while meals.isdigit()==False:
#         print("Wrong meals count")
#         meals = input("How many meals?: ")
#     meals=int(meals)
#     print(f"Hey {name}, You have to pay {meals*9}")


#תרגילי while2
#Task 3

# minute = 2
# sum = 0
#
# while True:
#     name=input("Put your name: ")
#     if name=="BYE":
#         print(f"The company has made a total of {sum}")
#         break
#     while name.isalpha()==False:
#         print("Wrong name")
#         name = input("Put your name: ")
#     minutes=input("How many minutes?: ")
#     while minutes.isdigit()==False:
#         print("Wrong minutes count")
#         minutes = input("How many minutes?: ")
#     minutes=int(minutes)
#     sum+=minutes*minute
#     print(f"Hey {name}, You have to pay {minutes*minute}")


#תרגילי while2
#Task 4

# hagi = 0
# hadas = 0
# while True:
#     name=input("Put your name: ")
#     if name=="SOF":
#         print(f"hagi has {hagi} votes, hadas has {hadas} votes")
#         if hagi>hadas:
#             print("hagi won!")
#         else:
#             print("hadas won!")
#         break
#     while name.isalpha() == False:
#         print("Wrong name")
#         name = input("Put your name: ")
#     vote = input("Vote [1] for hagi or, [2] for hadas: ")
#     while vote!="1" and vote!="2":
#         print("Wrong vote!")
#         vote = input("Vote [1] for hagi or, [2] for hadas: ")
#     if vote=="1":
#         hagi+=1
#     elif vote=="2":
#         hadas+=1


#תרגילי while2
#Task 5

# count = 0
# while True:
#     hogi=input("Enter class name: ")
#     while hogi.isalpha() == False:
#          print("Wrong name!")
#          hogi=input("Enter class name: ")
#     if hogi=="BYE":
#         print(f"Total money the organization made is: {count*10}")
#         break
#     students=input("How many students?: ")
#     while students.isdigit()==False:
#         print("Wrong amount!")
#         students = input("How many students?: ")
#     students=int(students)
#     count+=students


#תרגילי while2
#Task 6

# sum = 0
# students = 0
# while True:
#     name=input("Put your name: ")
#     while name.isalpha()==False:
#         print("Wrong name!")
#         name = input("Put your name: ")
#     if name=="BYE":
#         print(f"{students} Students participated, {sum} money made.")
#         break
#     machines=input("How many machines?: ")
#     while machines.isdigit()==False:
#         print("Wrong amount!")
#         machines = input("How many machines?: ")
#     machines = int(machines)
#     sum += machines*4
#     students += 1


#תרגילי while2
#Task 8

# books = 0
# giftcard = 0
#
# while True:
#     name=input("Put your name: ")
#     while name.isalpha()==False:
#         print("Wrong name!")
#         name = input("Put your name: ")
#     if name=="BYE":
#         print(f"{books} clients got books, {giftcard} clients got giftcards.")
#         break
#     age=input("Put your age: ")
#     while age.isdigit()==False:
#         print("Wrong age!")
#         age = input("Put your age: ")
#     age=int(age)
#     if age>50:
#         print("You got a giftcard!")
#         giftcard+=1
#     else:
#         print("You got a free book!")
#         books+=1








#itay 27/06/2024


#מעבדה 4 - תרגילים מורכבים לולאות
#3

# count = 0
# for num in range(1000, 10000):
#     if num%7==0 and (num%11==2 or num%11==3) and num%10!=8:
#         count+=1
# print("Count: ", count)


#מעבדה 4 - תרגילים מורכבים לולאות
#4

# numbers = []
# numbers.append(0)
# numbers.append(1)
# for i in range(2, 10):
#     numbers.append(numbers[i-1] + numbers[i-2])
# print(numbers)

#or:

# a = 1
# b = 1
#
# print(a, b, end=" ")
# for i in range(8):
#     next = a + b
#     a = b
#     b = next
#     print(b, end=" ")


#idk

# list=[]
# howmany=int(input("How many numbers you want in the list?: "))
# for i in range(howmany):
#     number1=int(input("Put a number: "))
#     list.append(number1)
# print(list)



'''sum = 0
count = 0
number=int(input("Put an ascending number: "))
while True:
    if number>next:
        sum-=next
    sum+=number
    next=int(input("Put an ascending number: "))
    sum+=next
    count += 2
    if number>next:
        sum-=next
        break
print("You've not entered an ascending number")
print(f"You've entered {count} numbers, sum is {sum} the average is {sum/count}")'''


#Task:

# כתוב תכנית הקולטת רשימה של ציונים )מספרים שלמים בין 0 ל-100(. מספר הציונים אינו ידוע מראש. הרשימה מסתיימת בציון לא חוקי )קטן מ-0 או גדול מ-100(. התוכנית מדפיסה את
# הממוצע )מספר שלם( של הציונים החוקיים שנקלטו. אם לא נקלטו ציונים חוקיים תודפס הודעה  מתאימה.
#  לדוגמא:
# Enter grades: 90 89 899
# Average: 89

# Answer:

# count=0
# sum=0
# while True:
#     grade=float(input("Put a grade: "))
#     if not 0<=grade<=100:
#         break
#     count+=1
#     sum+=grade
# print(f"Not legal grade, The average is {sum/count}")


#Task:

# כתוב תכנית המבצעת את המשחק שבע בום.
# התוכנית תרוץ מ-1 עד 100 ותדפיס כל מספר שלא מתחלק ב-7, אחרת תדפיס  "בום" במקום.

#Answer:


# for i in range(1,101):
#     if i%7!=0:
#         print(i, end=" ")
#     else: print("BOOM!", end=" ")



# Task:

# כתוב תכנית הקולטת מספרים ממשיים:
# המספר הראשון הוא סכום הכסף שיש לי ביד.
# המספר השני זה כמות המוצרים שאני צריך לקנות.
# לאחר-מכן יש להכניס לכל מוצר את מחירו.
# התוכנית תדפיס את היתרה הנותרת – בין אם מדובר בעודף )+( ובין אם מדובר בגירעון) -(..

#Answer:

# number=0
# sum=0
# cash=float(input("How many cash do you have?: "))
#
# products=int(input("How many products are you buying?: "))
# if products<0:
#     print("Wrong products amount!!!!")
# else:
#     for i in range(products):
#         next="Product"
#         number+=1
#         price=float(input(f"{next}{number} price?: "))
#         sum+=price
# print(f"The total is {sum}, you have {cash}")
# print(f"Now you have {cash-sum}")


# while True:
#     number=int(input("Put a number to check if it's prime: "))
#
#     if number <= 1:
#         print(f"{number} is not a prime number")
#     else:
#         is_prime = True
#
#         for i in range(2, number):
#             if number%i==0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(f"{number} is a prime number")
#         else:
#             print(f"{number} is not a prime number")


# for i in range(10):
#     for j in range(10):
#         print(j, end=" ")
#     print("\n")


# list=[]
# number=int(input("Put a number:")) #6
# for i in range(number):
#     temp_list = []
#     for j in range(1, i):
#         list.append([i+1])
# print(list)
#
# for i in range(1, 11):
#     for j in range(1, 11):
#             print(f"{i*j:3}", end=" ")
#     print()'''
#
# '''list_of_lists = [[1,2,3,49,6,48,125], [9,-9,12,34], [100]]
# list=[]
# for emad in list_of_lists:
#     list.append([max(emad)])
# print(list)
#
# list_of_lists = [[1,2,3,49,6,48,125], [9,-9,12,34], [100]]
# list=[]
# for emad in list_of_lists:
#     list.append([sum(emad)])
# print(list)


# תרגילים_ב_תכנות_לולאות_ורשימות
# Task: 3

# list=[3,4,8,5,9,19]
# for i in list:
#     if i%2==0:
#         print(i, end=" ")




# num=100
# while num<1000:
#     if num%10>num//100:
#         print(num,end="/")
#     num+=1






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
# # print(f"The multiplication of all numbers is: {m}")
#
# def Palindrome(str): #a function that checks a word if it is a palindrome with statement of True/False
#     return str == str[::-1]
#
# points = 15 #begin points
# listwords = [] #used words
#
# print("""Welcome to the Palindrome game!
# For each Palindrome word you enter, you get 10 points.
# If it wasn't a Palindrome word, you lose 5 points.
# You start with 15 points""")
#
# while True:
#     word=input("Put a word: ")
#     for i in listwords: #check if the word is used before
#         while word == i:
#             print("You already used this word, Try another!")
#             word = input("Put a word: ") #asks again
#     if Palindrome(word):
#         points+=10
#         print(f"Word is Palindrome, you now have {points}")s
#         listwords.append(word) #adds the word to the list
#     else:
#         points-=5
#         print(f"Word is not Palindrome, you now have {points}")
#
#
#     if points<=0:
#         print("You've lost!")
#         break
#     if points>=100:
#         print("You've won!")
#         break





# l = [[1,2,3] , [4,5,6], [7,8,9]]
# sum=0
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         sum+=l[i][j]
# print(sum)
#
# l = [[1,2,3] , [4,5,6], [7,8,9]]
# sum=0
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j], '*', end="")'''
#
# '''for i in range(1,11):
#     for j in range(1,11):
#         if i==j:
#             print("0", end=" ")
#         else:
#             print(i*j, end=" ")
#     print()
#
# #Task 1
# l = [[1,2,3] , [4,5,6] , [7,8,9]]
# l2 = []
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         l2.append(l[i][j])
# print(l2)'''
#
# '''#Task 2 list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# list3=[5,6,7,8,9]
# common=[]
# for i in list1:
#     if i in list2 and i in list3:
#         common.append(i)
# print(common)
#
# #Task3
# listnumbers=["1","2","3","4","5","6","7","8","9"]
# listnumbers2=["1","2","3","4","5","6","7","8","9"]
# listempty=[]
# for i in listnumbers:
#     for x in listnumbers2:
#         print(i+x, end=" ")
#     print()
#
# c = []
# x = []
# for i in range(1,11):
#     for j in range(1,11):
#         for k in range(1,11):
#             x.append([i,j,k])
#             for a in x:
#                while a not in i and a not in j and a not in k:
#                 c.append(x)
# print(c)