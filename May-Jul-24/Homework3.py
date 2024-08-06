# homework3 31/07/2024

print("------------------------------------------")


students = {
    "Emad": 70,
    "Itay": 80,
    "Avishay": 90,
}
print("Dict is:", students)


#Task 1:


def top_student(dict):
    highest = 0
    student = " "
    for key, value in dict.items():
        if value > highest:
            highest = value
            student = key
    return student, highest
print("Task 1: Student with the highest grade is", top_student(students))


#Task 2:


def add_bonus_points(dict, bonus):
    updated_dict = {}
    for key, value in dict.items():
        value += bonus
        if value>100:
            value = 100
        updated_dict[key]=value
    return updated_dict
print("Task 2: 5 point added as a bonus", add_bonus_points(students, 5))
print("------------------------------------------")


#Task 3:


students_dict = {
    "Emad": (22, "SE"),
    "Michael": (27, "FE"),
    "David": (19, "CE"),
    "George": (27, "QE")
}
def students_by_major(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value[1]] = key
    return new_dict
print("Dict is:", students_dict)
print("Task 3: Major dict", students_by_major(students_dict))
print("------------------------------------------")

#Task 4:


students_dict = {
    "Emad": (22, "SE"),
    "Michael": (27, "EE"),
    "David": (19, "CE"),
    "George": (27, "SE")
}
def oldest_student(dict):
    oldest = 0
    student = " "
    for key,val in dict.items():
        if val[0]>oldest:
            oldest = val[0]
            student = key
    return oldest, student
print("Dict is:", students_dict)
print("Task 4: The oldest student is", oldest_student(students_dict))
print("------------------------------------------")


#Task 5:


def convert_grades_to_letters(dict):
    converted_dict = {}
    for key, val in dict.items():
        if 90<=val<=100:
            val = "A"
        elif 80<=val<=89:
            val = "B"
        elif 70<=val<=79:
            val = "C"
        elif 60<=val<=69:
            val = "D"
        else:
            val = "F"
        converted_dict[key] = val
    return converted_dict

dict = {
    "Emad": 95,
    "Itay": 85,
    "Avishay": 75,
    "Lotem": 65,
    "Ofir": 55
}
print("Dict is: ", dict)
print("Task 5:", convert_grades_to_letters(dict))
print("------------------------------------------")


#Task 6


def sort_students_by_grades(dict):
    sorted_list = []
    while len(dict) > 0:
        highest = top_student(dict)
        sorted_list.append(highest)
        del dict[highest[0]]
    return sorted_list
students = {
    "Emad": 95,
    "Itay": 85,
    "Avishay": 75,
    "Lotem": 65
    "Ofir": 55
}
print(sort_students_by_grades(students))
