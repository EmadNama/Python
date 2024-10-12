def func1(dict):
    count = 0
    sum = 0
    for student, grade in dict.items():
        count += 1
        sum += grade
    return sum/count

# dict = {
#     "Emad": 70,
#     "Yosef": 80,
#     "Yarin": 90
# }
#
# print(func(dict))

def func2(list):
    sum = 0
    for num in list:
        if num<0:
            sum+=num
    return sum

# list = [1,-1,2,-2]
# print(func2(list))

def func3(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    return True


# string = "level"
# print(func3(string))

def func4(string):
    dict = {}
    list = []
    for i in string:
        dict[i] = string.count(i)
    for letter, count in dict.items():
        if count > 1:
            list.append(letter)
    return list

# string = "Emmmmaaaaad"
# print(func4(string))


def check_ascending(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

def check_descending(list):
    for i in range(len(list) - 1):
        if list[i] < list[i + 1]:
            return False
    return True

def func5(list):
    if check_ascending(list):
        return "Ascending"
    elif check_descending(list):
        return "Descending"
    else:
        return "Numbers not ascending or descending!!"

# list = [1,2,3,4,5,6]
# print(func5(list))

def func6(list1, list2):
    temp = 0
    list = list1 + list2
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list

print(func6([2,4,6], [1,3,5]))