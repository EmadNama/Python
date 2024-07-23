phoneBook={'avishay':'052-1234567'}

def getPhoneNumber(name,phoneBook):
    return phoneBook.get(name,'Not founded!')

def addContact(name,phone,phoneBook):
    if name in phoneBook:
        print('Error, name already exist!')
    else:
        phoneBook[name]=phone
        print('contact added to the phonebook')

def updatePhoneNumber(name,phone,phoneBook):
    if name in phoneBook:
        phoneBook[name]=phone
        print("contact updated!")
    else:
        print("Error, there is no such name!")

def searchContact(letters,phoneBook):
    founded = []
    for key in phoneBook:
        if key.startswith(letters):
            founded.append((key,phoneBook[key]))
    return founded

def deleteContact(name,phoneBook):
    if name in phoneBook:
        phoneBook.pop(name)
        print('contact deleted!')
    else:
        print('there is no such contact!')



addContact('avishay','1234',phoneBook)
addContact('avli','054-98765432',phoneBook)
updatePhoneNumber('jjj','053-2233221',phoneBook)
updatePhoneNumber('eli','7776663332',phoneBook)
print(phoneBook)
print(searchContact('av',phoneBook))
deleteContact('hhh',phoneBook)
deleteContact('avishay',phoneBook)
print(phoneBook)


