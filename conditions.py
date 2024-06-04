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

ticket=int(input("Ticket price: "))
age=int(input("Age: "))
if 0<age<18:
    print(f"You got 50% discount!!! please pay {ticket*0.50}")
elif 18<=age<=30:
    print(f"You have to pay full price which is {ticket}")
elif 30<age<64:
    print(f"You got 20% discount!!! please pay {ticket*0.80}")
elif age>=64:
    print(f"You got 80% discount!!! please pay {ticket*0.20}")