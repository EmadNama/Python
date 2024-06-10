'''
while True:
    grade = int(input("Put the grade 1: "))
    if not 0 <= grade <= 100:
        print("Wrong grade, 0-100 only.")
    elif grade==100:
        print(f"(100) (Excellent)")
    elif 90 <= grade < 100:
        print(f"(90 to 99) (Very good)")
    elif 70 <= grade < 90:
        print(f"(70 to 89) (Good)")
    elif 56 <= grade < 70:
        print(f"(56 to 69) (OK)")
    else: print("(0-55) (Failed)")

while True:
    temp = float(input("Put the temperature in Celsius to convert to Fahrenheit: "))
    if not 0<=temp<=100:
        print("Error, Only 0-100")
    else:
        print(f"The temperature in Fahrenheit is {(temp * 1.8) + 32}")


number=int(input("Put a two digits number: "))
if not 10<=number<=99:
    print("Error, That's not a two digits number.")
else:
    d1=number//10
    d2=number%10
    mult=d1*d2
    print(f"The mult of the digits is {mult}")
    if mult>50:
        print("The mult is bigger than 50")
    else: print("The mult is smaller than 50")
    if d1==d2:
        print("The two digits are the same")
    newnumber=d2*10+d1
    print(f"Your number is {number} and the opposite of it is {newnumber}, it's power: {newnumber**2}")
'''