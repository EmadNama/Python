class ID:

    def __init__(self, id):
        self.id = id

    def IdWithLastDigit(self):

        if len(self.id) > 8:
            return("8 Digits only!")
        elif len(self.id) < 8:
            while len(self.id) < 8:
                self.id = "0" + self.id

        temp_sum = 0
        for digit in self.id[1::2]:
            if (int(digit) * 2) > 9:
                temp_sum += (int(digit) * 2) - 9
            else:
                temp_sum += int(digit) * 2

        for digit in self.id[0::2]:
            temp_sum += int(digit)

        return self.id + str(10 - temp_sum%10)

    def IdCheck(self):
        if self.id == ID(self.id[:8]).IdWithLastDigit():
            return "Legal ID"
        else:
            return "Not legal"


# 32306989-8
newid = ID("32306989")
print(newid.IdWithLastDigit())
newid = ID("323069898")
print(newid.IdCheck())






# class Person:
#     def __init__(self, firstname, lastname, id):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.id = id