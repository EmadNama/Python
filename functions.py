#09-07-2024


#פונקציה len

# def mystrlen(str): #function that calculates a string length
#     letterscount=0
#     for i in str:
#         if i==" ":
#             continue
#         letterscount+=1
#     return letterscount
#
#
# while True:
#     str=input("Input a word: ")
#     print(mystrlen(str))


# def division(numbers, x): #division check by x for the numbers in a list
#     list=[] #for the numbers that can be divided by x
#     for i in numbers:
#         if i%x==0:
#             list.append(i)
#     return list
#
# list = [2,4,6,5,7,9]
# x = 2
#
# print(division(list, x))


# def SimanKreaah(str): #checks if a string has only one "!" in it.
#     count=0
#     for i in str:
#         if i == "!":
#             count+=1
#     if count==1:
#         return True
#     else:
#         return False
#
#
# while True:
#     str=input("Put a string: ")
#     print(SimanKreaah(str))


# def startswithupper(str): #checks if a string starts with an upper letter
#     return str[0].isupper()
#
# while True:
#     str=input("Put a string: ")
#     print(startswithupper(str))


# def digitcheck(str): #checks if a string has between 1-3 digits only
#     count=0
#     for i in str:
#         if i.isdigit()==True:
#             count+=1
#     return 1<=count<=3
#
# while True:
#     str = input("Put a string: ")
#     print(digitcheck(str))



#-------------------------10-07-2024--------------------------------------

# gradeslist = []
# gradescount = 0

# def grades(g):
#     gradeslist.append(g)

# def gradesplusten():
#     # Iterate through the list and modify grades accordingly
#     for i in range(len(gradeslist)):
#         if gradeslist[i] < 90:
#             gradeslist[i] += 10
#         else:
#             gradeslist[i] = 100
#     return gradeslist  # Return the modified grades list

# while gradescount < 10:
#     g = float(input("Enter grade: "))
#
#     # Validate the input grade
#     while not (0 <= g <= 100):
#         print("Wrong Grade! Please enter a grade between 0 and 100.")
#         g = float(input("Enter grade: "))
#
#     # Add grade to the list
#     grades(g)
#     gradescount += 1
#
# # Call the function to modify grades and print the final list
# modified_grades = gradesplusten()
# print("Modified grades list:", modified_grades)



# def divisions(): #checks a number's dividers sum, e.g in=27 out=13 (1+3+9)
#     sum=0
#     list=[]
#     number=int(input("Put a number: "))
#     for i in range(1,number):
#         if number%i==0:
#             sum+=i
#             list.append(i)
#     return sum, list
# l = divisions()
# print(l)



# def SumOfDividers(x): #checks a number's dividers sum, e.g in=27 out=13 (1+3+9)
#     sum=0
#     for i in range(1,x):
#         if x%i==0:
#             sum+=i
#     return sum
#
# def EqualCheck(x,y): #checks if a number's dividers equal a second number and vice versa.
#     if SumOfDividers(x)==y and SumOfDividers(y)==x:
#         return True
#     return False
#
# while True:
#     numberone=int(input("Put number one: "))
#     numbertwo=int(input("Put number two: "))
#     print(EqualCheck(numberone, numbertwo))



def SumOfDividers(x): #checks a number's dividers sum, e.g in=27 out=13 (1+3+9)
    sum=0
    for i in range(1,x):
        if x%i==0:
            sum+=i
    return sum

def EqualCheck(x,y): #checks if a number's dividers equal a second number and vice versa.
    if SumOfDividers(x)==y and SumOfDividers(y)==x:
        return True
    return False

def ListOfCouples():
    list=[]
    for i in range(10, 100000):
        for j in range(i, 100000):
            if i!=j and EqualCheck(i,j):
                list.append([i,j])
    return list

result=ListOfCouples()
print(result)