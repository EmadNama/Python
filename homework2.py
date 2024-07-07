#עבודה מספר 2 – קורס צעדים ראשונים בתכנות
#עמאד נעמה


#task 1
#כתוב  תוכנית  שמקבלת רשימה של מספרים ומחזירה את המספר הגדול ביותר ברשימה אסור להשתמש בפונקציה מובנת max

# list=[2,4,8,16,32,256,64,128]
# maxnumber=list[0]
# for i in list:
#     if i>maxnumber:
#         maxnumber=i
# print(maxnumber)


#task 2
#כתוב תוכנית המקבלת מהמשתמש מספר שלם ומדפיסה את כל המספרים הזוגיים מ1 עד המספר שנקלט.

# number=int(input("Put a number: "))
# list=[]
# for i in range(1,number):
#     if i%2==0:
#         list.append(i)
# print(list)


#task 3
#כתבו תוכנית הקולטת מהמשתמש מחירים למוצרים שקנה בסופר עד לקליטת המחיר -1 . בסוף קליטת המחירים יודפס למשתמש כמה עלה לו ומה המחיר ממוצע פר מוצר .

# sum=0
# count=0
# while True:
#     product=float(input("Put the product price: "))
#     if product==-1:
#         break
#     elif product==0 or product<-1:
#         print("Wrong price!")
#     else:
#         count+=1
#         sum+=product
# print(f"{count} products with a total of {sum} and a product average of {sum/count}")


#task 4
#כתוב   תוכנית   שמקבלת רשימה של מחרוזות ומחזירה רשימה חדשה שמכילה רק את המחרוזות שאורכן גדול מ-3 תווים .

# list_words=["hi", "avishay", "itay", "emad", "bye"]
# new_list=[]
# for i in list_words:
#     if len(i)>3:
#         new_list.append(i)
# print(new_list)


#task 5
#כמה מספרים בני 4 ספרות מקיימים את שלושת התכונות הבאות:
#⦁	מתחלקים ב-7 ללא שארית
#⦁	מתחלקים ב-11 עם שארית 2 או .3
#⦁	ספרת האחדות שלהם אינה 8.

# count=0
# for i in range(1000,10000):
#     if i%7==0 and (i%11==2 or i%11==3) and i%10!=8:
#         count+=1
# print(count)


#task 6
#כתוב תוכנית הקולטת מספר מהשתמש ובודקת האם המספר הוא ראשוני .

# while True:
#     number=int(input("Put a number to check if it's prime: "))
#     if number <= 1:
#         print(f"{number} is not a prime number")
#     else:
#         is_prime = True
#         for i in range(2, number):
#             if number%i==0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(f"{number} is a prime number")
#         else:
#             print(f"{number} is not a prime number")


#task 7
#כתוב תוכנית שמקבלת מספר שלם ומדפיסה ריבוע של מספרים. לדוגמה, עבור קלט 4:

# number=int(input("Put a number: "))
# for i in range(1, number+1):
#     for x in range(1, number+1):
#         print(x, end=" ")
#     print()


#task 8
# כתוב תוכנית שמדפיסה משולש מספרים. מספר השורות של המשולש נקבע על ידי המשתמש. לדוגמה, עבור קלט 5 :

# number=int(input("Put a number: "))
# for i in range(1,number+1):
#     for x in range(1, i+1):
#         print(x, end=" ")
#     print()

