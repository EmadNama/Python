
import time

def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def recSum(n):
    if n == 1:
        return 1
    return n + recSum(n - 1)

# startTime = time.perf_counter()
# print(sum(500))
# endTime = time.perf_counter()
# print(f"{endTime - startTime:.10f}")


# startTime = time.perf_counter()
# print(recSum(500))
# endTime = time.perf_counter()
# print(f"{endTime - startTime:.10f}")

def sleep():
    x = 0
    while x < 10:
        print("Message")
        time.sleep(2)
        x += 2

def fiveSec():
    while True:
        input("Press Enter To Start")
        start = time.perf_counter()
        input("Press Enter To Stop")
        end = time.perf_counter()
        print(f"{end - start:.10f}")

# fiveSec()

def twodigitssum(lst, n):

    dict = {}
    pairs = []

    for i in lst:
        x = n - i
        if x in dict:
            pairs.append((x, i))
        dict[i] = True
    return pairs

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(twodigitssum(lst, 6))

def twolists(list1, list2):
    dict = {}
    pst = []
    for i in list1:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
    for i in list2:
        if i in dict:
            dict[i] += 1
    for key, val in dict.items():
        if val >= 2:
            pst.append(key)
    return pst


print(twolists([1,2,2,2,2,2,2,2], [1,6,2,2,2,2,2,7,7,7,7,7]))