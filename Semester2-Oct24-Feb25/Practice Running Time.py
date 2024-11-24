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

startTime = time.perf_counter()
print(sum(500))
endTime = time.perf_counter()
print(f"{endTime - startTime:.10f}")


startTime = time.perf_counter()
print(recSum(500))
endTime = time.perf_counter()
print(f"{endTime - startTime:.10f}")

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

