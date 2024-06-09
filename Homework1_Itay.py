#עבודה מספר 1 – קורס צעדים ראשונים בתכנות


#תרגיל 1: בדיקת שנה מעוברת
year=int(input("Put a year to check if it's a leap year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Yes, It's a leap year.")
else: print("No, It's not a leap year.")

#תרגיל 2: המרת טמפרטורה
temp=float(input("Put the temperature in Celsius to convert to Fahrenheit: "))
print(f"The temperature in Fahrenheit is {(temp*1.8)+32}")

#תרגיל 3: בדיקת תקינות כתובת דואר אלקטרוני
email=input("Put an Email address: ")
if 4<len(email)<30 and email.count("@")==1 and email[0].isupper():
    print("Valid")
else: print("Not Valid!!!")

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



