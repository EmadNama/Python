# def GetTuple(tuple): #a function that gets a tuple and returns a dictionary that has strings from the tuple as keys, and it's length as a value
#     dictionary = {}
#     for words in tuple:
#         dictionary[words] = len(words)
#     return dictionary
#
# tuple = ("emad", "hello World!", "avishay", "h", "12", "lotem")
# print(GetTuple(tuple))


# def GetTuple(y): #a function that gets a tuple of numbers and returns a dictionary with these numbers as a key, and the value of all the numbers that can divide it
#     dictionary = {}
#     list = []
#     for key in y:
#         for numbers in range(1,key+1):
#             if key%numbers==0:
#                 list.append(numbers)
#         t = tuple(list)
#         dictionary[key] = t
#         list = []
#     return dictionary
#
# xtuple = (12,14,16)
# print(GetTuple(xtuple))



# def GetDict(d): #a function that recieves a dict of students and their grades and returns a dict with the students and their average
#     newDict = {}
#     for key in d:
#         avg = sum(d[key])/len(d[key])
#         newDict[key]=avg
#     return newDict
# dictionary = {"alice":(85,90,92), "bob":(78,85,80)}
# print(GetDict(dictionary))


contacts = {"Emad": "0542534577", "Michael": "0582345656"}

def FindContactNumber(contact):
    return contacts.get(contact, "Not Found")

contact = input("Put the name of the contact: ")
print(FindContactNumber(contact))


def AddNewContact(contact, number):
    if contact in contacts:
        print("Contact Exists")
    else:
        contacts[contact] = number

NewContact = input("Put New Contact Name: ")
NewContactNumber = input("Put New Contact Number: ")
AddNewContact(NewContact,NewContactNumber)
print(contacts)


def UpdateContact(contact, number):
    if contact in contacts:
        contacts[contact] = number
    else:
        print("Contact Doesn't Exist!")

contactupdate = input("Put a Contact Name to update: ")
UpdateContactNumber = input("Put Contact new Number: ")
UpdateContact(contactupdate, UpdateContactNumber)
print(contacts)


def SearchContact(twoletters):
    list = []
    for i in contacts:
        if i.startswith(twoletters):
            list.append((i))
    return list

tletters = input("Put two letters: ")
SearchContact(tletters)
