def recFactorial(num):
    if num == 0:
        return 1
    return num * recFactorial(num-1)


def recFib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return recFib(num - 1) + recFib(num - 2)


def recRevString(string):
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string
    return string[-1] + recRevString(string[:-1])