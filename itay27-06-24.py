#itay 27/06/2024


#מעבדה 4 - תרגילים מורכבים לולאות
#3

# count = 0
# for num in range(1000, 10000):
#     if num%7==0 and (num%11==2 or num%11==3) and num%10!=8:
#         count+=1
# print("Count: ", count)


#מעבדה 4 - תרגילים מורכבים לולאות
#4

# numbers = []
# numbers.append(0)
# numbers.append(1)
# for i in range(2, 10):
#     numbers.append(numbers[i-1] + numbers[i-2])
# print(numbers)

#or:

# a = 1
# b = 1
#
# print(a, b, end=" ")
# for i in range(8):
#     next = a + b
#     a = b
#     b = next
#     print(b, end=" ")


#idk

# list=[]
# howmany=int(input("How many numbers you want in the list?: "))
# for i in range(howmany):
#     number1=int(input("Put a number: "))
#     list.append(number1)
# print(list)



'''sum = 0
count = 0
number=int(input("Put an ascending number: "))
while True:
    if number>next:
        sum-=next
    sum+=number
    next=int(input("Put an ascending number: "))
    sum+=next
    count += 2
    if number>next:
        sum-=next
        break
print("You've not entered an ascending number")
print(f"You've entered {count} numbers, sum is {sum} the average is {sum/count}")'''


#Task:

# כתוב תכנית הקולטת רשימה של ציונים )מספרים שלמים בין 0 ל-100(. מספר הציונים אינו ידוע מראש. הרשימה מסתיימת בציון לא חוקי )קטן מ-0 או גדול מ-100(. התוכנית מדפיסה את
# הממוצע )מספר שלם( של הציונים החוקיים שנקלטו. אם לא נקלטו ציונים חוקיים תודפס הודעה  מתאימה.
#  לדוגמא:
# Enter grades: 90 89 899
# Average: 89

# Answer:

# count=0
# sum=0
# while True:
#     grade=float(input("Put a grade: "))
#     if not 0<=grade<=100:
#         break
#     count+=1
#     sum+=grade
# print(f"Not legal grade, The average is {sum/count}")


#Task:

# כתוב תכנית המבצעת את המשחק שבע בום.
# התוכנית תרוץ מ-1 עד 100 ותדפיס כל מספר שלא מתחלק ב-7, אחרת תדפיס  "בום" במקום.

#Answer:


# for i in range(1,101):
#     if i%7!=0:
#         print(i, end=" ")
#     else: print("BOOM!", end=" ")



# Task:

# כתוב תכנית הקולטת מספרים ממשיים:
# המספר הראשון הוא סכום הכסף שיש לי ביד.
# המספר השני זה כמות המוצרים שאני צריך לקנות.
# לאחר-מכן יש להכניס לכל מוצר את מחירו.
# התוכנית תדפיס את היתרה הנותרת – בין אם מדובר בעודף )+( ובין אם מדובר בגירעון) -(..

#Answer:

# number=0
# sum=0
# cash=float(input("How many cash do you have?: "))
#
# products=int(input("How many products are you buying?: "))
# if products<0:
#     print("Wrong products amount!!!!")
# else:
#     for i in range(products):
#         next="Product"
#         number+=1
#         price=float(input(f"{next}{number} price?: "))
#         sum+=price
# print(f"The total is {sum}, you have {cash}")
# print(f"Now you have {cash-sum}")


'''while True:
    number=int(input("Put a number to check if it's prime: "))

    if number <= 1:
        print(f"{number} is not a prime number")
    else:
        is_prime = True

        for i in range(2, number):
            if number%i==0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")'''


'''for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print("\n")'''


'''list=[]
number=int(input("Put a number:")) #6
for i in range(number):
    temp_list = []
    for j in range(1, i):
        list.append([i+1])
print(list)'''

'''for i in range(1, 11):
    for j in range(1, 11):
            print(f"{i*j:3}", end=" ")
    print()'''

'''list_of_lists = [[1,2,3,49,6,48,125], [9,-9,12,34], [100]]
list=[]
for emad in list_of_lists:
    list.append([max(emad)])
print(list)'''

'''list_of_lists = [[1,2,3,49,6,48,125], [9,-9,12,34], [100]]
list=[]
for emad in list_of_lists:
    list.append([sum(emad)])
print(list)'''


# תרגילים_ב_תכנות_לולאות_ורשימות
# Task: 3

# list=[3,4,8,5,9,19]
# for i in list:
#     if i%2==0:
#         print(i, end=" ")

