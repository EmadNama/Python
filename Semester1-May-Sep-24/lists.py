#Task 1
list=[1, 2, 3, 4, 5]
list.sort()
print(f"the list is [1, 2, 3, 4, 5] and the biggest number is {list[-1]}")

#Task 2
list2=[-1, -2, 1, 2, 3]
positive_numbers=[]
if list2[0]>0:
    positive_numbers.append(list2[0])
if list2[1]>0:
    positive_numbers.append(list2[1])
if list2[2]>0:
    positive_numbers.append(list2[2])
if list2[3]>0:
    positive_numbers.append(list2[3])
if list2[4]>0:
    positive_numbers.append(list2[4])

print(f"the list is [-1, -2, 1, 2, 3] and the positive numebrs are {positive_numbers}")

#Task 3
list3=["emad", "hello world", "a", "this is the longest1", "15638"]
print(max(list3))

#Task 4
list4=[4, 2, 9, 5, 6]
print(f"The list is [4, 2, 9, 5, 6], Number 5 exists? {5 in list4}")

#Task 5
list5=[6, 4, 5, 5]
print(f"The list is [6, 4, 5, 5] and the sum is {sum(list5)}")

#Task 1
list6=[0, 1, 2, 3, 4]
print("the list is [0, 1, 2, 3, 4] and the min is", (min(list6)))

#Task 2
list7=[3, 5, 7, 9]
list8=[2, 5, 4, 9]
common=[]
if (list7[0] in list8)==True:
    common.append(list7[0])
if (list7[1] in list8)==True:
    common.append(list7[1])
if list7[2]==list8[2]:
    common.append(list7[2])
if list7[3]==list8[3]:
    common.append(list7[3])

print(common)

#Task 3
list9=[1, 9, 5, 4, 2]
evennumbers=[]
if list9[0]%2==0 and list9[1]%2==0 and list9[2]%2==0 and list9[3]%2==0 and list9[4]%2==0:
    print("All the numbers are even")
if list9[0]%2==0:
    evennumbers.append(list9[0])
if list9[1]%2==0:
    evennumbers.append(list9[1])
if list9[2]%2==0:
    evennumbers.append(list9[2])
if list9[3]%2==0:
    evennumbers.append(list9[3])
if list9[4]%2==0:
    evennumbers.append(list9[4])
print(f"Only the numbers {evennumbers} are even")

#Task 4
list10=["Applepencil", "asbeing", "bigpeanut", "pizzaslice", "Amad"]
list11=[]
if list10[0].startswith("A") or list10[0].startswith("a"):
    if 3<len(list10[0])<10:
        list11.append(list10[0])
if list10[1].startswith("A") or list10[1].startswith("a"):
    if 3<len(list10[1])<10:
        list11.append(list10[1])
if list10[2].startswith("A") or list10[2].startswith("a"):
    if 3<len(list10[2])<10:
        list11.append(list10[2])
if list10[3].startswith("A") or list10[3].startswith("a"):
    if 3<len(list10[3])<10:
        list11.append(list10[3])
if list10[4].startswith("A") or list10[4].startswith("a"):
    if 3<len(list10[4])<10:
        list11.append(list10[4])
list11.sort()
print(list11[-1])

#Task 5
list12=[-4, 2, -14, 17, 1, 103]
list13=[]
if list12[0]>0:
    list13.append(list12[0])
if list12[1]>0:
    list13.append(list12[1])
if list12[2]>0:
    list13.append(list12[2])
if list12[3]>0:
    list13.append(list12[3])
if list12[4]>0:
    list13.append(list12[4])
if list12[5]>0:
    list13.append(list12[5])
print(f"The list is [-4, 2, -14, 17, 1, 103] and the positive numbers are {list13}")

#Task 6
list14=["emad", "gal", "yakov", "emad", "gal"]
list15=[]
if list14[0]==list14[1] or list14[0]==list14[2] or list14[0]==list14[3] or list14[0]==list14[4]:
    list15.append(list14[0])
if list14[1]==list14[2] or list14[1]==list14[3] or list14[1]==list14[4]:
    list15.append(list14[1])
if list14[2] == list14[4] or list14[2] == list14[3]:
    list15.append(list14[2])
if list14[3] == list14[4]:
    list15.append(list14[3])
print(list15)

#task 7
list16=[2, 4, 6, 8, 10, 11]
if len(list16)>5:
    print(sum(list16))
else:
    print(min(list16))

#task 8
list17=[3, 11, 19, 24, 12]
if list17.count(list17[0])>1 or list17.count(list17[1])>1 or list17.count(list17[2])>1 or list17.count(list17[3])>1 or list17.count(list17[4])>1:
    print("Yes, there is equal numbers in the list")
else: print("No, there is no equal numbers in the list")

#task 9
list18=["iphone", "galaxy", "pc", "laptop"]
list19=["laptop", "water", "pc", "emad"]
list20=[]
if list18[0] in list19:
    list20.append(list18[0])
if list18[1] in list19:
    list20.append(list18[1])
if list18[2] in list19:
    list20.append(list18[2])
if list18[3] in list19:
    list20.append(list18[3])
print(list20)

#task 10
