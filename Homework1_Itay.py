#עבודה מספר 1 – קורס צעדים ראשונים בתכנות


#תרגיל 1: בדיקת שנה מעוברת
while(True):
    year=int(input("Put a year to check if it's a leap year: "))
    if year%4==0 and year%100!=0 or year%400==0:
        print("Yes, It's a leap year.")
    else: print("No, It's not a leap year.")

    #תרגיל 2: המרת טמפרטורה
    temp=float(input("Put the temperature in Celsius to convert to Fahrenheit: "))
    print(f"The temperature in Fahrenheit is {(temp*1.8)+32}")

    #תרגיל 3: בדיקת תקינות כתובת דואר אלקטרוני
    email=input("Put an Email address: ")

    length=4<len(email)<30
    sht=email.count("@")==1
    capital=email[0].isupper()

    if length==True and sht==True and capital==True:
        print("Valid!!")
    elif length==False:
        print("Not Valid, The length must be 4-30.")
    elif sht==False:
        print("Not Valid, The Email doesn't have a (@) in it.")
    else:
        print("Not Valid, The first letter should be capital.")

    #תרגיל 4: מחשבון בסיסי
    firstnumber=float(input("Put the first number: "))
    operation=input("Operation? (+, -, *, /) : ")
    secondnumber=float(input("Put the second number: "))
    if operation=="+":
        print(firstnumber+secondnumber)
    elif operation=="-":
        print(firstnumber-secondnumber)
    elif operation=="*":
        print(firstnumber*secondnumber)
    elif operation=="/":
        if secondnumber == 0:
            print("Error, You can't divide a number by zero.")
        else: print(firstnumber/secondnumber)
    else: print("The operation you have put is not correct")

    # תרגיל 5: חישוב ציונים
    grade1=int(input("Put grade 1: "))
    grade2=int(input("Put grade 2: "))
    grade3=int(input("Put grade 3: "))
    avg=(grade1+grade2+grade3)/3
    if not 0<=grade1<=100 or not 0<=grade2<=100 or not 0<=grade3<=100:
        print("Wrong grades, 0-100 only.")
    elif 95<=avg<=100:
        print(f"(95 to 100) (Excellent), The average is {avg}")
    elif 70<=avg<95:
        print(f"(70 to 95) (Very good), The average is {avg}")
    elif 56<=avg<70:
        print(f"(56 to 70) (Enough), The average is {avg}")
    else: print(f"(0 to 56) (Failed), The average is {avg}")