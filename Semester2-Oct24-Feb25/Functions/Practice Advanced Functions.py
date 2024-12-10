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






























def func7(list):
    new_list = []
    for num in list:
        if num in new_list:
            continue
        else:
            new_list.append(num)
    return new_list

# list = [1,1,3,4,3]
# print(func7(list))

def func8(list1,list2, num):
    dict = {}
    for i in range(len(list1)):
        dict[i] = num - list1[i]
    for j in range(len(list2)):
        if list2[j] == dict[list2[j]]:
            return True


# list1 = [1,2,3,4]
# list2 = [4,6,3,2]
# print(func8(list1, list2, 10))


def func9(list1, list2, num):
    dict = {}
    for i in range(len(list1)):
        dict[i] = num - i
        for j in range(len(list2)):
            if list1[i]+list2[j] == num:
                return i,j
    return dict

# list1 = [1,2,3,4]
# list2 = [4,6,3,2]
# print(func9(list1, list2, 10))



def func10(list1,list2,num):
    temp_list = []
    for i in list1:
        for j in list2:
            if i + j == num:
                temp_list.append([i,j])
    return temp_list

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [3,4,5,6,1,2,3,4,5,7,8,9,5]
# print(func10(list1, list2, 5))


def func11(list, k):
    n = len(list)
    k = k%n
    temp_list = []
    for i in range(len(list)):
        new_index = (i+k)%n
        temp_list[new_index] = list[i]
    return temp_list

# list = [1,2,3,4]
# print(func11(list, 1))


def func12(list):
    dict = {}
    avg = sum(list) / len(list)
    for i in list:
        dict [i] = abs(i-avg)
    return dict

# list = [70,80,90]
# print(func12(list))

def func13(list):
    new_list = []
    for i in range(1, max(list)):
        if i in list:
            continue
        else:
            new_list.append(i)
    return new_list

# list = [1,10]
# print(func13(list))

def func14(list):
    dict = {}
    for num in list:
        dict[num] = list.count(num)
    return dict

# list = [1,2,2,4,5,6,5]
# print(func14(list))

def func15(list1, list2):
    new_list = []
    for num in list1:
        if num in list2:
            new_list.append(num)
    return new_list

# list1 = [1,2,3,4,5,6]
# list2 = [7,8,9,5,1,2]
# print(func15(list1,list2))

def func16(num):
    for i in range(0,num+1):
        if i * i == num:
            return i
        elif i * i < num and (i+1)*(i+1)>num:
            return i

# print(func16(36))

def func17(list):
    new_list = []
    count = 0
    for num in list:
        if num != 0:
            new_list.append(num)
        else:
            count += 1
    while count != 0:
        new_list.append(0)
        count -= 1
    return new_list

# list = [1,2,3,0,1,2,0,1,4,0]
# print(func17(list))



class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def __repr__(self):
        return (f"Student Name: {self.name}, Student Age: {self.age}, Student ID: {self.id}")


class Course:

    def __init__(self, name, students_list, students_count):
        self.name = name
        self.students_list = students_list
        self.students_count = students_count

    def __repr__(self):
        return (f"Course name: {self.name}, Course Students: {self.students_list}, Students Count: {self.students_count}")

    def add_student(self, student):
        self.students_list.append(student)
        self.students_count += 1

    def sort_ages(self):
        sorted_list = []
        for student in self.students_list:
            sorted_list.append(student.age)
        sorted_list.sort()
        return sorted_list


student1 = Student("Emad", 23, "311526523")
student2 = Student("Atar", 15, "311526523")
student3 = Student("Gal", 65, "311526523")
student4 = Student("Elchai", 32, "311526523")
student5 = Student("Yarin", 28, "311526523")
student6 = Student("Yousef", 23, "311526523")

course1 = Course("Mathematics", [], 0)

course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
course1.add_student(student4)
course1.add_student(student5)
course1.add_student(student6)

# print(course1)
print(course1.sort_ages())