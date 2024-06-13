'''
#task 1
number1=int(input("Please put number one: "))
number2=int(input("Please put number two: "))
division=number1/number2
if type(division)==float:
    print(number1%number2)
else:
    print(number1/number2)
'''

'''
#task 2
number1=int(input("Please put number one: "))
number2=int(input("Please put number two: "))
number3=int(input("Please put number three: "))
if number1<number2 and number2<number3:
    print("Ascending")
elif number1 > number2 and number2>number3:
    print("Descending")
else: print("Not sorted")
'''
number=int(input("Put a four digits number: "))
if not 1000<=number<=9999:
    print("That's not a four digit number")
else:
    d1=number//1000
    d2=number%1000//100
    d3=number%100//10
    d4=number%10
    if d1==d4 and d2==d3:
        print("Cemetric")
    else: print("Not cemetric")