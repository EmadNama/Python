def sumOfDividers(num):
    sum = 0
    for i in range (1,num):
        if num%i==0:
            sum+=i
    return sum


def checkCouples(num1,num2):
    if num1==sumOfDividers(num2) and num2 == sumOfDividers(num1):
        return True
    return False




def listOfCouples(low,high):
    l = []
    for i in range(low,high):
        for j in range(i,high):
            if i!=j and checkCouples(i,j):
                l.append([i,j])
                print(l)
    return l

print(listOfCouples(100,7000))