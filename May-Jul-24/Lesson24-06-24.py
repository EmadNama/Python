'''l = [[1,2,3] , [4,5,6], [7,8,9]]
sum=0
for i in range(len(l)):
    for j in range(len(l[i])):
        sum+=l[i][j]
print(sum)'''

'''l = [[1,2,3] , [4,5,6], [7,8,9]]
sum=0
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], '*', end="")'''

'''for i in range(1,11):
    for j in range(1,11):
        if i==j:
            print("0", end=" ")
        else:
            print(i*j, end=" ")
    print()'''

'''#Task 1
l = [[1,2,3] , [4,5,6] , [7,8,9]]
l2 = []
for i in range(len(l)):
    for j in range(len(l[i])):
        l2.append(l[i][j])
print(l2)'''

'''#Task 2 list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
list3=[5,6,7,8,9]
common=[]
for i in list1:
    if i in list2 and i in list3:
        common.append(i)
print(common)'''

'''#Task3
listnumbers=["1","2","3","4","5","6","7","8","9"]
listnumbers2=["1","2","3","4","5","6","7","8","9"]
listempty=[]
for i in listnumbers:
    for x in listnumbers2:
        print(i+x, end=" ")
    print()'''

c = []
x = []
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            x.append([i,j,k])
            for a in x:
               while a not in i and a not in j and a not in k:
                c.append(x)
print(c)