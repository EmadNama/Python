# number=int(input("Put a three digit number: "))
# if 100<=number<=999:
#     print("Correct!")
# else:print("Error, That's not a three digit number.")
#
#
#
# shirtprice=int(input("Put the shirt price: "))
# shirts=int(input("Put how many shirts: "))
# if shirtprice*shirts>1000:
#     print(f"The total with 10% discount is: {(shirts*shirtprice)*1.17*0.90}")
# else:print(f"The total with TAX is: {(shirts*shirtprice)*1.17}")
#
#
#
#
#
# side1=int(input("Put the side1: "))
# side2=int(input("Put the side2: "))
# side3=int(input("Put the side3: "))
# if (side1+side2)>side3 and(side2+side3)>side1 and(side1+side3)>side2:
#     print("That's a triangle!")
# else:print("ERROR, That's not a triangle!")
#
#
#
#
#
# grade=int(input("What is the student grade?: "))
# if 90<=grade<=100:
#     print("A")
# elif 70<=grade<=90:
#     print("B")
# elif 56<=grade<=70:
#     print("C")
# else:print("F")
#
#
#
#
#
# ticket=float(input("Ticket price: "))
# age=int(input("Age: "))
# if 0<=age<18:
#     print(f"You got 50% discount!!! please pay {ticket*0.50}")
# elif 18<=age<30:
#     print(f"You have to pay full price which is {ticket}")
# elif 30<=age<64:
#     print(f"You got 20% discount!!! please pay {ticket*0.80}")
# elif age>=64:
#     print(f"You got 80% discount!!! please pay {ticket*0.20}")
#
#
#
#
#
# num=int(input("Put a two digits number: "))
# if num%2==0:
#     if num%5==0:
#         print("The number is divided by 2 and 5 so also by 10")
#     else: print("The number is divided by 2 but not 5")
# else: print("The number is odd")
#
#
#
# threedigits=int(input("Put a three digits number: "))
# if not 100<=threedigits<=999:
#     print("Bye bye!")
# if 100<=threedigits<=999:
#     if threedigits%2==0:
#         print("The number can be divided by 2")
#     if not threedigits%2==0:
#        print("The number is odd")
#        print(f"The closest even number is {threedigits-1} or {threedigits+1}")
#        print(f"The first digit is: {threedigits//100}, Second digit: {threedigits%100//10}, Last digit: {threedigits%10}")
#     digit1=threedigits//100
#     digit2=threedigits%100//10
#     digit3=threedigits%10
#     if digit1+digit3<digit2:
#         print("The first digit and last digit sum is less than the middle digit")
#     else:print(f"the first digit and last digit sum is more than the middle digit and their multiplication is {digit1*digit3}")
#
#
#
#
# number1=int(input("Put the first number: "))
# number2=int(input("Put the second number: "))
# number3=int(input("Put the third number: "))
#
#
# if number1>number2 and number1>number3:
#     print(f"The biggest number is {number1}")
# if number2>number1 and number2>number3:
#     print(f"The biggest number is {number2}")
# if number3>number1 and number3>number2:
#     print(f"The biggest number is {number3}")
#
#
#
# if number1<number2 and number1<number3:
#     print(f"The smallest number is {number1}")
# if number2<number1 and number2<number3:
#     print(f"The smallest number is {number2}")
# if number3<number1 and number3<number2:
#     print(f"The smallest number is {number3}")
#
#
#
# if number1>number2 and number1<number3:
#     print(f"The middle number is {number1}")
# if number2>number1 and number2<number3:
#     print(f"The middle number is {number2}")
# if number3>number1 and number3<number2:
#     print(f"The middle number is {number3}")
#
#
#
#
# if n1>n2 and n1>n3:
#     max=n1
# elif n2>n1 and n2>n3:
#     max=n2
# else:
#     max=n3
# if n1<n2 and n1<n3:
#     min=n1
# elif n2<n1 and n2<n3:
#     min=n2
# else:
#     min=n3
#
#
# n1=int(input("Put the first number: "))
# n2=int(input("Put the second number: "))
# n3=int(input("Put the third number: "))
#
# if n1>n2 and n1>n3:
#     max=n1
# elif n2>n1 and n2>n3:
#     max=n2
# else:
#     max=n3
# if n1<n2 and n1<n3:
#     min=n1
# elif n2<n1 and n2<n3:
#     min=n2
# else:
#     min=n3
# if min<n1<max:
#     mid=n1
# elif min<n2<max:
#     mid=n2
# else:
#     mid=n3
# print(f"Biggest is {max}, mid is {mid}, Smallest is {min}")










############################################# Training ##############################################################








#
# #task one
#
# number=int(input("Put a number:"))
# if number > 5:
#     print("Yes")
#
#
#
# #task two
# numberone=int(input("Put number one:"))
# numbertwo=int(input("Put number two:"))
# if numberone%2==0:
#     print("Number one is even")
# if numbertwo%2==0:
#     print("Number two is even")
#
#
#
# #task three
# numberone=int(input("Put number one:"))
# numbertwo=int(input("Put number two:"))
# if numberone%2!=0:
#     print("Number one is odd")
# if numbertwo%2!=0:
#     print("Number two is odd")
#
#
#
# #task four
# number=int(input("Put a number:"))
# if number>100:
#     print("Bigger than 100")
# else: print("Not bigger than 100")
#
#
#
# #task 5
# age=int(input("Put your age:"))
# if age>10:
#     print(f"Your age in months is {age*12}")
#
#
#
# #Task 6
# numberone=int(input("Put number one:"))
# numbertwo=int(input("Put number two:"))
# if numberone>numbertwo:
#     print("Number one is bigger than number two")
# elif numberone==numbertwo:
#     print("The numbers are equal to each other")
# else: print("Number two is bigger than number one")
#
#
#
# #task 7
# numberone=int(input("Put number one:"))
# numbertwo=int(input("Put number two:"))
# numberthree=int(input("Put number three:"))
# if numberone%3==0 and not numberone%2==0:
#     print("Number one can be divided by 3 and cannot be divided by two")
# if numbertwo%3==0 and numbertwo%2!=0:
#     print("Number two can be divided by 3 and cannot be divided by two")
# if numberthree%3==0 and numberthree%2!=0:
#     print("Number three can be divided by 3 and cannot be divided by two")
#
#
#
# #page 2, task 1
# number=int(input("Put a number:"))
# if number>10:
#     print("Bigger than 10")
# elif number<10:
#     print("Smaller than 10")
# else: print("The number is 10")
#
#
#
# #task 2
# temperature=float(input("Howm much is the temperature?: "))
# if temperature>30:
#     print("It's hot")
# elif temperature<30:
#     print("It's Nice")
# else: print("It is exactly 30")
#
#
#
# #task 3
# grade=int(input("Put the grade: "))
# if grade==100:
#     print("Excellent")
# elif 90<=grade<100:
#     print("Very good")
# elif 56<=grade<90:
#     print("Good")
# elif 0<=grade<56:
#     print("Failed")
# else: print("The grade is not between 0-100")
#
#
#
# #task 4
# grade1=int(input("Put grade one: "))
# grade2=int(input("Put grade two: "))
# grade3=int(input("Put grade three: "))
# avg=(grade1+grade2+grade3) / 3
# if avg <= 100 and avg >= 85:
#     print("Excellent")
# elif avg >= 70 and avg < 85:
#     print("Very good")
# elif avg < 70 and avg >= 56:
#     print("Good")
# elif avg >= 0 and avg < 56:
#     print("Failed")
# else: print("Wrong grade!")
#
#
#
# #task 5
# number1=int(input("Put number one: "))
# number2=int(input("Put number two: "))
# number3=int(input("Put number three: "))
#
# if number1>number2 and number1>number3:
#     first=number1
# elif number2>number1 and number2>number3:
#     first=number2
# else:
#     first=number3
#
# if number1<number2 and number1<number3:
#     third=number1
# elif number2<number1 and number2<number3:
#     third=number2
# else:
#     third=number3
#
# if first<number1<third:
#     second=number1
# elif first<number2<third:
#     second=number2
# else:
#     second=number3
# print(first, second, third)
#
#
#
# name=str(input("How can i help?: "))
# if name.startswith("Hello"):
#     print("Hello there!")





# #task 1
# number1=int(input("Please put number one: "))
# number2=int(input("Please put number two: "))
# division=number1/number2
# if type(division)==float:
#     print(number1%number2)
# else:
#     print(number1/number2)



# #task 2
# number1=int(input("Please put number one: "))
# number2=int(input("Please put number two: "))
# number3=int(input("Please put number three: "))
# if number1<number2 and number2<number3:
#     print("Ascending")
# elif number1 > number2 and number2>number3:
#     print("Descending")
# else: print("Not sorted")



# number=int(input("Put a four digits number: "))
# if not 1000<=number<=9999:
#     print("That's not a four digit number")
# else:
#     d1=number//1000
#     d2=number%1000//100
#     d3=number%100//10
#     d4=number%10
#     if d1==d4 and d2==d3:
#         print("Cemetric")
#     else: print("Not cemetric")




# while True:
#     grade = int(input("Put the grade 1: "))
#     if not 0 <= grade <= 100:
#         print("Wrong grade, 0-100 only.")
#     elif grade==100:
#         print(f"(100) (Excellent)")
#     elif 90 <= grade < 100:
#         print(f"(90 to 99) (Very good)")
#     elif 70 <= grade < 90:
#         print(f"(70 to 89) (Good)")
#     elif 56 <= grade < 70:
#         print(f"(56 to 69) (OK)")
#     else: print("(0-55) (Failed)")
#
# while True:
#     temp = float(input("Put the temperature in Celsius to convert to Fahrenheit: "))
#     if not 0<=temp<=100:
#         print("Error, Only 0-100")
#     else:
#         print(f"The temperature in Fahrenheit is {(temp * 1.8) + 32}")
#
#
# number=int(input("Put a two digits number: "))
# if not 10<=number<=99:
#     print("Error, That's not a two digits number.")
# else:
#     d1=number//10
#     d2=number%10
#     mult=d1*d2
#     print(f"The mult of the digits is {mult}")
#     if mult>50:
#         print("The mult is bigger than 50")
#     else: print("The mult is smaller than 50")
#     if d1==d2:
#         print("The two digits are the same")
#     newnumber=d2*10+d1
#     print(f"Your number is {number} and the opposite of it is {newnumber}, it's power: {newnumber**2}")
