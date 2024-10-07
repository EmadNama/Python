class ID:

    def __init__(self, id):
        self.id = id

    def IdWithLastDigit(self):
        if len(self.id) > 8:
            return("8 Digits only!")
        elif len(self.id) < 8:
            while len(self.id) < 8: #12340000
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

class Person:

    def __init__(self, firstname, lastname, id, address):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.address = address

    def IdCorrector(self):
        ID(self.id).IdWithLastDigit()
        if ID(self.id).IdCheck() == "Not legal":
            self.id = ID(self.id[:8]).IdWithLastDigit()
            return f"Not correct id, the correct is {self.id}"


name = (input("Name: "))
lastname = input("Last name: ")
id = (input("ID: "))
address = input("Address: ")

person1 = Person(name, lastname, id, address)
print(person1.IdCorrector())



################################# TEACHER SOLUTION  #######################




# class ID:
#     def addCheckDigit(self,id):
#         if len(id)<8:
#             id = '0'*(8-len(id))+id
#         elif len(id)>8:
#             return 'Error! cannot add check digit!'
#         flag = 1
#         sum = 0
#         for char in id:
#             temp = flag*int(char)
#             if temp>9:
#                 temp = (temp//10) + (temp%10)
#             sum+=temp
#             if flag == 1:
#                 flag =2
#             else:
#                 flag =1
#         if sum % 10==0:
#             return id+'0'
#         else:
#             return id+str(10-(sum % 10))
#
#     def checkID(self,id):
#         return id==self.addCheckDigit(id[:-1])
#
#
# class Person:
#     def __init__(self,f_name,l_name,id,addr):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.id = id
#         self.addr = addr
#
#         o = ID()
#         if not o.checkID(self.id):
#             self.id = o.addCheckDigit(self.id[:-1])
#
#     def __repr__(self):
#         return self.f_name+', '+self.l_name+', ID: '+self.id
#
# list_of_persons=[]
# for i in range(3):
#     print("Person number ",(i+1),':')
#     f_name = input("Please enter first name: ")
#     l_name = input("Please enter last name: ")
#     id = input("Please enter id: ")
#     addr = input("Please enter address: ")
#     list_of_persons.append(Person(f_name,l_name,id,addr))
#
#
# for item in list_of_persons:
#     print(item)