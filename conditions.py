'''

number=int(input("Put a three digit number: "))
if 100<=number<=999:
    print("Correct!")
else:print("Error, That's not a three digit number.")
'''

'''
shirtprice=int(input("Put the shirt price: "))
shirts=int(input("Put how many shirts: "))
if shirtprice*shirts>1000:
    print(f"The total with 10% discount is: {(shirts*shirtprice)*1.17*0.90}")
else:print(f"The total with TAX is: {(shirts*shirtprice)*1.17}")

'''

'''

side1=int(input("Put the side1: "))
side2=int(input("Put the side2: "))
side3=int(input("Put the side3: "))
if (side1+side2)>side3 and(side2+side3)>side1 and(side1+side3)>side2:
    print("That's a triangle!")
else:print("ERROR, That's not a triangle!")

'''

'''

grade=int(input("What is the student grade?: "))
if 90<=grade<=100:
    print("A")
elif 70<=grade<=90:
    print("B")
elif 56<=grade<=70:
    print("C")
else:print("F")

'''


'''
ticket=float(input("Ticket price: "))
age=int(input("Age: "))
if 0<=age<18:
    print(f"You got 50% discount!!! please pay {ticket*0.50}")
elif 18<=age<30:
    print(f"You have to pay full price which is {ticket}")
elif 30<=age<64:
    print(f"You got 20% discount!!! please pay {ticket*0.80}")
elif age>=64:
    print(f"You got 80% discount!!! please pay {ticket*0.20}")
    
'''

'''

num=int(input("Put a two digits number: "))
if num%2==0:
    if num%5==0:
        print("The number is divided by 2 and 5 so also by 10")
    else: print("The number is divided by 2 but not 5")
else: print("The number is odd")

'''
'''
threedigits=int(input("Put a three digits number: "))
if not 100<=threedigits<=999:
    print("Bye bye!")
if 100<=threedigits<=999:
    if threedigits%2==0:
        print("The number can be divided by 2")
    if not threedigits%2==0:
       print("The number is odd")
       print(f"The closest even number is {threedigits-1} or {threedigits+1}")
       print(f"The first digit is: {threedigits//100}, Second digit: {threedigits%100//10}, Last digit: {threedigits%10}")
    digit1=threedigits//100
    digit2=threedigits%100//10
    digit3=threedigits%10
    if digit1+digit3<digit2:
        print("The first digit and last digit sum is less than the middle digit")
    else:print(f"the first digit and last digit sum is more than the middle digit and their multiplication is {digit1*digit3}")
'''


'''
number1=int(input("Put the first number: "))
number2=int(input("Put the second number: "))
number3=int(input("Put the third number: "))


if number1>number2 and number1>number3:
    print(f"The biggest number is {number1}")
if number2>number1 and number2>number3:
    print(f"The biggest number is {number2}")
if number3>number1 and number3>number2:
    print(f"The biggest number is {number3}")
    
    
    
if number1<number2 and number1<number3:
    print(f"The smallest number is {number1}")
if number2<number1 and number2<number3:
    print(f"The smallest number is {number2}")
if number3<number1 and number3<number2:
    print(f"The smallest number is {number3}")
    
    
    
if number1>number2 and number1<number3:
    print(f"The middle number is {number1}")
if number2>number1 and number2<number3:
    print(f"The middle number is {number2}")
if number3>number1 and number3<number2:
    print(f"The middle number is {number3}")
'''


'''
if n1>n2 and n1>n3:
    max=n1
elif n2>n1 and n2>n3:
    max=n2
else:
    max=n3
if n1<n2 and n1<n3:
    min=n1
elif n2<n1 and n2<n3:
    min=n2
else:
    min=n3

'''
n1=int(input("Put the first number: "))
n2=int(input("Put the second number: "))
n3=int(input("Put the third number: "))

if n1>n2 and n1>n3:
    max=n1
elif n2>n1 and n2>n3:
    max=n2
else:
    max=n3
if n1<n2 and n1<n3:
    min=n1
elif n2<n1 and n2<n3:
    min=n2
else:
    min=n3
if min<n1<max:
    mid=n1
elif min<n2<max:
    mid=n2
else:
    mid=n3
print(f"Biggest is {max}, mid is {mid}, Smallest is {min}")