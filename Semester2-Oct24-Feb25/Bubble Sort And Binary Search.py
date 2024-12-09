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

def main():
    list = [2,1,12,40,13,90,88]
    # print(BubbleSort(list))
    print(BinarySearch(BubbleSort(list), 90))

main()