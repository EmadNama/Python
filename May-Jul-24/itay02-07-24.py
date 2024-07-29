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