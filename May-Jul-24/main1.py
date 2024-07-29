def getGrades():
    grades=[]
    count = 4
    i = 0
    while i<count:
        grade = int(input("Please enter grade: "))
        if 0<=grade<=100:
            grades.append(grade)
            i+=1
        else:
            print("Error, type again")

    return grades

def updateFactor(l):
    for i in range(len(l)):
        #l[i]=min(l[i]+10,100)
        l[i]+=10
        if l[i]>100:
            l[i]=100


def calc(l):
    print(max(l))
    print(min(l))
    return sum(l)/len(l)




l = getGrades()
print(l)
updateFactor(l)
print(l)


