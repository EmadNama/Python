def func1(list):
    new_list = []
    for num in list:
        if num in new_list:
            continue
        else:
            new_list.append(num)
    return new_list

# list = [1,1,3,4,3]
# print(func1(list))

def func2(list1,list2, num):
    dict = {}
    for i in range(len(list1)):
        dict[i] = num - list1[i]
    for j in range(len(list2)):
        if list2[j] == dict[list2[j]]:
            return True


# list1 = [1,2,3,4]
# list2 = [4,6,3,2]
# print(func2(list1, list2, 10))


def func2(list1,list2, num):
    dict = {}
    for i in range(len(list1)):
        dict[i] = num - i
        for j in range(len(list2)):
            if list1[i]+list2[j] == num:
                return i,j
    return dict

# list1 = [1,2,3,4]
# list2 = [4,6,3,2]
# print(func2(list1, list2, 10))



def func3(list1,list2,num):
    temp_list = []
    for i in list1:
        for j in list2:
            if i + j == num:
                temp_list.append([i,j])
    return temp_list

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [3,4,5,6,1,2,3,4,5,7,8,9,5]
# print(func3(list1, list2, 5))


def func4(list, k):
    n = len(list)
    k = k%n
    temp_list = []
    for i in range(len(list)):
        new_index = (i+k)%n
        temp_list[new_index] = list[i]
    return temp_list

# list = [1,2,3,4]
# print(func4(list, 1))


def func5(list):
    dict = {}
    avg = sum(list) / len(list)
    for i in list:
        dict [i] = abs(i-avg)
    return dict

# list = [70,80,90]
# print(func5(list))

def func6(list):
    new_list = []
    for i in range(1, max(list)):
        if i in list:
            continue
        else:
            new_list.append(i)
    return new_list

# list = [1,10]
# print(func5(list))