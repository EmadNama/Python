def sum_even_numbers(n):
    if n <= 2:
        return 0
    if (n - 1) % 2 == 0:
        return (n - 1) + sum_even_numbers(n - 2)
    return sum_even_numbers(n - 1)

def print_odd_numbers(n):
    if n <= 1:
        return
    if n % 2 != 0:
        print(n, end=" ")
    print_odd_numbers(n - 1)

def sum_of_digits(n):
    if n <= 9:
        return n
    return sum_of_digits(n%10) + sum_of_digits(n//10)

def reverse_string(str):
    if len(str) <= 1:
        return str
    return str[-1] + reverse_string(str[:-1])

def positive_sum(list):
    if len(list) == 0:
        return 0
    if list[0] > 0:
        return list[0] + positive_sum(list[1:])
    else:
        return positive_sum(list[1:])

def character_count(str, ch):
    if len(str) == 0:
        return 0
    if str[0] == ch:
        return 1 + character_count(str[1:], ch)
    else:
        return character_count(str[1:], ch)

def str_fix(str):
    if len(str) <= 1:
        return str
    if str[0] == " ":
        return str_fix(str[1:]) + " "
    return str[0] + str_fix(str[1:])

def isAscending(list):
    if len(list) == 1:
        return True
    if list[0] < list[1]:
        return isAscending(list[1:])
    return False

def EvenMult(list):
    if len(list) == 0:
        return 1
    if list[0] % 2 == 0:
        return list[0] * EvenMult(list[1:])
    return EvenMult(list[1:])

def RemoveCh(str, ch):
    if len(str) <= 1:
        return str
    if str[0] == ch:
        return RemoveCh(str[1:], ch)
    return str[0] + RemoveCh(str[1:], ch)

def isPalindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[-1]:
        return isPalindrome(str[1:-1])
    return False
#