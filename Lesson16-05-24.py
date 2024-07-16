# def digitcheck(number, digit): #checks a number if it contains a specific digit
#     number = str(number)
#     digit = str(digit)
#     for i in number:
#         if i==digit:
#             return True
#     return False

def digitcheck(num, digit):
    while num>0:
        if (num%10)==digit:
            return True
        num//10
    return False


def rangecheck(low, high):
    list = []
    for i in range(low, high):
        digitcheck(i, 2)
        if digitcheck(i, 2):
            continue
        else:
            list.append(i)
    return list
print(rangecheck(10, 30))