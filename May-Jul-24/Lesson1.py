'''
28/05/2024
'''

#Basic mult, sum and minus
print("Hello World!")
print("This is my first project")
print("Let me show you my skills")
anynumber=int(input("Put any number :"))
print("Your number multiplied by 2 is", anynumber*2)
print("Your number multiplied by itself is", anynumber*anynumber)
number1=int(input("Put number one:"))
number2=int(input("Put number two:"))
print("The sum is",number1+number2)
print("The minus is",number1-number2)
print("The mult is",number1*number2)
#two digits
twodigits=int(input("Put a number with two digits:"))
print("The first digit is",twodigits//10)
print("The second digit is",twodigits%10)
#three digits
threedigits=int(input("Put a number with three digits:"))
print("The first digit is",threedigits//100)
print("The second digit is", threedigits%100//10)
print("The third digit is", threedigits%10)
#four digits
fourdigits=int(input("Put a number with four digits:"))
print("The first digit is",fourdigits//1000)
print("The second digit is", fourdigits%1000//100)
print("The third digit is", fourdigits%100//10)
print("The fourth digit is", fourdigits%10)
#name and age task
name = (input("Put your name:"))
age = (input("Put your age:"))
print("Your name is:",name)
print("And your age is:",age)
#triangle task
base = int(input("Put the base of the triangle:"))
height = int(input("Put the height of the triangle:"))
print("The space of the triangle is",base*height/2)