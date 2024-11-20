import time

def LinearSearch(list, num):
    for i in range(len(list)):
        if list[i] == num:
            return i
    return -1

def BubbleSort(list):
    for i in range(len(list) -1):
        for j in range(len(list) -1 -i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def BinarySearch(list, num):
    low = 0
    high = len(list) - 1
    mid = (low+high) // 2
    while (low <= high) and (list[mid] != num):
        if list[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low <= high:
        return mid
    return -1

def checkTimes(func, *args):
    startTime = time.time()
    res = func(*args)
    endTime = time.time()
    return (endTime - startTime)


def main():
    sList = list(range(10000))
    medList = list(range(100000))
    lrgList = list(range(100000))

    #linear
    print(checkTimes(LinearSearch, sList, 500))
    print(checkTimes(LinearSearch, medList, 1700))
    print(checkTimes(LinearSearch, lrgList, 1700))

    # list = [2,1,12,40,13,90,88]
    # print(list)
    # print(BubbleSort(list))
    # print(LinearSearch(list, 40))
    # print(BinarySearch(BubbleSort(list), 40))
    # print(LinearSearch(list, 14))
    # print(BinarySearch(BubbleSort(list), 14))

main()
