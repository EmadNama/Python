
#task one
'''
number=int(input("Put a number:"))
if number > 5:
    print("Yes")
'''

'''
#task two
numberone=int(input("Put number one:"))
numbertwo=int(input("Put number two:"))
if numberone%2==0:
    print("Number one is even")
if numbertwo%2==0:
    print("Number two is even")
'''

'''
#task three
numberone=int(input("Put number one:"))
numbertwo=int(input("Put number two:"))
if numberone%2!=0:
    print("Number one is odd")
if numbertwo%2!=0:
    print("Number two is odd")
'''

'''
#task four
number=int(input("Put a number:"))
if number>100:
    print("Bigger than 100")
else: print("Not bigger than 100")
'''

'''
#task 5
age=int(input("Put your age:"))
if age>10:
    print(f"Your age in months is {age*12}")
'''

'''
#Task 6
numberone=int(input("Put number one:"))
numbertwo=int(input("Put number two:"))
if numberone>numbertwo:
    print("Number one is bigger than number two")
elif numberone==numbertwo:
    print("The numbers are equal to each other")
else: print("Number two is bigger than number one")
'''

'''
#task 7
numberone=int(input("Put number one:"))
numbertwo=int(input("Put number two:"))
numberthree=int(input("Put number three:"))
if numberone%3==0 and not numberone%2==0:
    print("Number one can be divided by 3 and cannot be divided by two")
if numbertwo%3==0 and numbertwo%2!=0:
    print("Number two can be divided by 3 and cannot be divided by two")
if numberthree%3==0 and numberthree%2!=0:
    print("Number three can be divided by 3 and cannot be divided by two")
'''

'''
#page 2, task 1
number=int(input("Put a number:"))
if number>10:
    print("Bigger than 10")
elif number<10:
    print("Smaller than 10")
else: print("The number is 10")
'''

'''
#task 2
temperature=float(input("Howm much is the temperature?: "))
if temperature>30:
    print("It's hot")
elif temperature<30:
    print("It's Nice")
else: print("It is exactly 30")
'''

'''
#task 3
grade=int(input("Put the grade: "))
if grade==100:
    print("Excellent")
elif 90<=grade<100:
    print("Very good")
elif 56<=grade<90:
    print("Good")
elif 0<=grade<56:
    print("Failed")
else: print("The grade is not between 0-100")
'''

'''
#task 4
grade1=int(input("Put grade one: "))
grade2=int(input("Put grade two: "))
grade3=int(input("Put grade three: "))
avg=(grade1+grade2+grade3) / 3
if avg <= 100 and avg >= 85:
    print("Excellent")
elif avg >= 70 and avg < 85:
    print("Very good")
elif avg < 70 and avg >= 56:
    print("Good")
elif avg >= 0 and avg < 56:
    print("Failed")
else: print("Wrong grade!")
'''

'''
#task 5
number1=int(input("Put number one: "))
number2=int(input("Put number two: "))
number3=int(input("Put number three: "))

if number1>number2 and number1>number3:
    first=number1
elif number2>number1 and number2>number3:
    first=number2
else:
    first=number3

if number1<number2 and number1<number3:
    third=number1
elif number2<number1 and number2<number3:
    third=number2
else:
    third=number3

if first<number1<third:
    second=number1
elif first<number2<third:
    second=number2
else:
    second=number3
print(first, second, third)
'''

'''
name=str(input("How can i help?: "))
if name.startswith("Hello"):
    print("Hello there!")
'''

