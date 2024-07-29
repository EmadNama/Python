
name=input("Please enter a name:")
print(name[0], name[-1])
print(name[1:3])
print("Hello My name is Emad")
print(name[1:])
print(len(name))


fullname=str(input("Please put your full name: "))
print(fullname.upper())
print(fullname.lower())
print(len(fullname))
middleIndex=len(fullname)//2
print(fullname[middleIndex])

################################################################ TRAINING ##################################################

#task 1
string=input("Put a string: ")
print(f"The size of the given string is: {len(string)}")

#task 2
string=input("Put a string: ")
if string.isalpha():
    print("Good job, It's just letters")
else: print("It's not letters!!!!!")

#task 3
string=input("Put a string: ")
print(string.lower())

#task 4
string=input("Put a string: ")
print(string.upper())

#task 5
string=input("Put a string: ")
if string.startswith("s"):
    print("Good Job!!! it starts with s")
else: print("It doesn't starts with s!!")

#task 6
string=input("Put a string: ")
if string.endswith("s"):
    print("Good Job!!! it ends with s")
else: print("It doesn't end with s!!")

#task 7
string=input("Put a string with spaces: ")
print(string.strip())

#task 8
string=input("Put a string: ")
string=string.replace("a", "b")
print(string)

#task 9
string=input("Write a string that have more than one hello in it: ")
print(f"The word hello is duplicated {string.count("hello")} times")

#task 10
string=input("Put a string for capitalization of each word first letter: ")
print(string.title())

#task 11
string=input("Put a string to check if its just numbers: ")
if string.isdigit()==True:
    print(f"{string.isdigit()}, the string youve put contains only numbers")
else: print(f"{string.isdigit()}, It's not just numbers!!!!")

#task 12
string=input("Put a string to convert it to a list: ")
print(string.split())

#task 14
string=input("Put a string with just spaces only: ")
print(string.isspace())

#task 15
string=input("Put a string to switch capital to small and vice versa: ")
print(string.swapcase())

#task 16
string=input("Put a string to count how many words in it: ")
string=string.split()
print(f"The string has {len(string)} words in it")

#task 17
string=input("Put a string to have it in the opposite way: ")
print(string[::-1])

#task 18
string=input("Put a string to check if it's a palindrome: ")
if (string[::-1]) == (string[0::]):
    print("The string is a palindrome")
else: print("The string is not a palindrome!!!!!")


#task 19
string=input("Put a string with symbols and spaces to get rid of them: ")
if string.isalnum()==True:
    print("No symbols or spaces found")


email=str(input("Inesrt your E-mail: "))
if email.endswith(".com")


#task 20

string=input("Put a string to count how many words in it: ")
string=string.split()
print(f"The string has {len(string)} words in it")
