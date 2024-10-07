def add_bonus_points(dict, bonus):
    new_dict = {}
    for student, grade in dict.items():
        grade+=bonus if grade+bonus>100 else grade=100
        new_dict[student] = grade
    return new_dict


dict = {
    "Emad": 40,
    "Lotem": 60
}

print(add_bonus_points(dict, 50))