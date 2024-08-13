# #30-07-2024
#
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def DistanceFromOrigin(self): #calculates point distance from (0,0)
#         return(self.x**2+self.y**2)**0.5
#     def DistanceFromPoint(self,other): #calculates distance from point to point
#         return((self.x-other.x)**2+(self.y-other.y)**2)**0.5
#     def retPoint(self): #returns point cordinations into a tuple
#         return (self.x, self.y)
#     def __repr__(self): #works for strings only
#         return str((self.x,self.y))
#
#
# p1 = Point(1,2)
# p2 = Point(2,3)
#
# # print(p1.x,p1.y) #manually printing an object
# # print(p2.x,p2.y)
# # print(p1.DistanceFromOrigin()) #refers to line 5
# # print(p1.DistanceFromPoint(p2)) #refers to line 7
# # print(p1) #refers to line 11
# # print(p1.retPoint()) #refers to line 9
#
# class Circle:
#     def __init__(self,radius,point):
#         self.radius = radius
#         self.point = point
#     def area(self):
#         return 3.14*self.radius**2
#     def heikef(self):
#         return 2*3.14*self.radius
#     def koter(self):
#         return self.radius*2
#     def __repr__(self):
#         return str(self.radius)+", "+str(self.point)
#     def DistanceFromAnotherCircle(self, other):
#         return self.point.DistanceFromPoint(other.point)
#     def TouchCheck(self, other):
#         RadiusSum = self.radius + other.radius
#         if self.point.DistanceFromPoint(other.point) > RadiusSum:
#                 return False
#         return True
#
# p1 = Point(2,4)
# p2 = Point(2,4)
#
# c1 = Circle(8, p1)
# c2 = Circle(2, p2)
#
# print(c1.TouchCheck(c2))



############################################## Training #####################################


#Task 1:


# class Student:
#     def __init__(self, Name, Age, Grade):
#         self.Name = Name
#         self.Age = Age
#         self.Grade = Grade
#     def printStudents(self):
#         print(f"Name: {self.Name}, Age: {self.Age}, Grade: {self.Grade}")
#     def BonusPoints(self, points):
#         self.Grade += points
#         if self.Grade > 100:
#             self.Grade = 100
#         return self.Grade
#     def copy_in_test(self):
#         self.Grade = 0
#         return self.Grade
#
# student1 = Student("Emad", "22", 89)
# student2 = Student("Itay", "28", 94)
# student3 = Student("Mark", "19", 67)
#
# student1.printStudents()
# student2.printStudents()
# student3.printStudents()
#
# print("Emad with bonus 60:", student1.BonusPoints(60))
# print("Itay copied in test:", student2.copy_in_test())


#Task 2:


# class BankAccount:
#     def __init__(self, Name, Balance):
#         self.Name = Name
#         self.Balance = Balance
#     def DisplayAccount(self):
#         print(f"Name: {self.Name}, Balance = {self.Balance}")
#     def Withdraw(self, Amount):
#         if (self.Balance - Amount) < 0:
#             print(f"You can't withdraw {Amount} Because you have {self.Balance} Only!")
#         else:
#             self.Balance -= Amount
#             print(f"You've withdrawn {Amount} and your balance now is: {self.Balance}")
#     def Deposit(self, Amount):
#         self.Balance += Amount
#         print(f"You've deposited {Amount} and your balance now is: {self.Balance}")
#
# Bank1 = BankAccount("Emad", 5000)
#
# Bank1.DisplayAccount()
# Bank1.Withdraw(3000)
# Bank1.Withdraw(6000)
# Bank1.Deposit(5000)


#Task 3:


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def circ(self):
#         circ = (self.length*2) + (self.width*2)
#         print(f"The circumference of the rectangle is {circ}")
#     def area(self):
#         area = self.length * self.width
#         print(f"The area of the rectangle is {area}")
#     def setLength(self, newLength):
#         self.length = newLength
#     def setWidth(self, newWidth):
#         self.width = newWidth
#     def isSquare(self):
#         if self.width == self.length:
#             print("That's a square!")
#         else:
#             print("Not a square")
#
#
# rectangle1 = Rectangle(5, 2)
# rectangle1.circ()
# rectangle1.area()
# rectangle1.setLength(8)
# rectangle1.setWidth(4)
# rectangle1.circ()
# rectangle1.area()
#
# rectangle2 = Rectangle(8,8)
# rectangle2.isSquare()


#Task 4:


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def PercentageBonus(self, percent):
#         x = (percent / 100) * self.salary
#         print(self.salary + x)
#     def DisplayEmployee(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")
#     def YearlySalary(self):
#         print(f"Yearly salary of {self.name} is {self.salary*12}")
#
# employee1 = Employee("Emad", 18000)
# employee1.PercentageBonus(10)
# employee2 = Employee("Itay", 1000)
# employee2.DisplayEmployee()
# employee2.YearlySalary()


#Task 4:


# class Circle:
#     def __init__(self, radius, x, y):
#         self.radius = radius
#         self.x = x
#         self.y = y
#     def heikef(self):
#         print(f"The heikef is {2*3.14*self.radius}")
#     def area(self):
#         print(f"The area is {3.14*self.radius**2}")
#     def koter(self):
#         print(f"The koter of this circle is {self.radius * 2}")
#     def setX(self, NewX):
#         self.x = NewX
#     def setY(self, NewY):
#         self.y = NewY
#
# circle1 = Circle(5, 0, 0)
# circle1.heikef()
# circle1.area()


#Task 5:


# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     def DisplayPerson(self):
#         print(f"Full name is: {self.first_name, self.last_name} Age: {self.age}")
#
# person1 = Person("Emad", "Nama", 22)
# person1.DisplayPerson()


#Task 6: (Bank Account, Already done)


#Task 7:


# class Student:
#     def __init__(self, id, name, grades):
#         self.id = id
#         self.name = name
#         self.grades = grades
#     def DisplayStudent(self):
#         print(f"Student Details: Id: {self.id}, Name: {self.name}, Grades: {self.grades}")
#     def Average(self):
#         sum = 0
#         count = 0
#         for i in (self.grades):
#             sum += i
#             count +=1
#         print(f"Student average is {sum/count}")
# student1 = Student(344344344, "Emad", [70,80,90])
# student1.DisplayStudent()
# student1.Average()


# class house:
#     def __init__(self, address, rooms, price):
#         self.address = address
#         self.rooms = rooms
#         self.price = price
#     def DisplayHouse(self):
#         print(f"House Address: {self.address}, Rooms: {self.rooms}, Price: {self.price}")
#
# house1 = house("Israel", 5, 16555)
# house1.DisplayHouse()


############################################## Lesson 05/08/24 #####################################

# class Person:
#     def __init__(self, firstname, lastname, id, gender, age, address, work):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.id = str(id)
#         self.gender = gender
#         self.age = str(age)
#         self.address = address
#         self.work = work
#         self.children = []
#     def __repr__(self):
#         return self.firstname+" "+self.lastname+"\n"+\
#             "id number: "+self.id+"\n"+\
#             "Gender: "+self.gender+"\n"+\
#             "Age: "+self.age+"\n"+\
#             "Address: "+self.address+"\n"+\
#             "Working in: "+self.work+"\n"
#     def AddChild(self,NewChild):
#         self.children.append(NewChild)
#     def ChangeAddress(self, NewAddress):
#         self.address = NewAddress
#     def __eq__(self, other):
#         return self.age == other.age
#     def DisplayChildrens(self):
#         print("My childrens: ")
#         for child in self.children:
#             print(child)
#
# Person1 = Person("Avishay", "Krif", 140133035, "M", 44, "BeerSheva", "SCE")
# print(Person1)

class BankAccount:
    def __init__(self, Name, AccountNumber, Balance):
        self.name = Name
        self.accountnumber = AccountNumber
        self.balance = Balance
        self.limit = Balance * 2
    def withdraw(self, amount):
        if amount <= 0:
            print("Wrong amount!")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
        return self.balance
    def deposit(self, amount):
        if amount <= 0:
            print("Wrong amount!")
        else:
            self.balance += amount
        return self.balance

    def __repr__(self):
        return self.name+"\n"+"Account Number: "+str(self.accountnumber)+"\n"\
    +"Balance: "+str(self.balance)

    def transfer(self, other, amount):
        if amount > self.balance:
            print("You don't have this amount")
        else:
            self.balance -= amount
            other.deposit(amount)
        return other.balance

bank1 = BankAccount("Emad", "93338424", 5000)
bank2 = BankAccount("Yousef", "4558613784", 2000)

# print(f"Welcome, {bank1}")
# while True:
#     operation = input("Choose operation [1] Deposit, [2] Withdraw, [3] Trasnfer: ")
#     if operation == "1":
#         amount = float(input("How much: "))
#         print(bank1.deposit(amount))
#     elif operation == "2":
#         amount = float(input("How much: "))
#         print(bank1.withdraw(amount))
#     elif operation == "3":
#         other = input("To Account Number: ")
#         amount = float(input("How much?: "))
#         print(bank1.transfer(other, amount))

# bank1.transfer(bank2, 200)
# print(bank1)
# print(bank2)





############################################## Lesson 06/08/24 #####################################


'''class student:
    def __init__(self, name, id, courses):
        self.name = name
        self.id = id
        self.courses = courses
        self.courses_grades = {}
        for course in self.courses:
            self.courses_grades[course.coursenumber] = 0
    def __repr__(self):
        return (f"Name: {self.name} ID: {self.id}\nCourses: {self.courses}")
    def new_course(self, course):
        self.courses.append(course)
        self.courses_grades[course] = 0
    def update_grade(self, course, grade):
        self.courses_grades[course] = grade

class course:
    def __init__(self, coursenumber, coursename, coursestudents):
        self.coursenumber = coursenumber
        self.coursename = coursename
        self.coursestudents = coursestudents
    def __repr__(self):
        return (f"Course Number: {self.coursenumber} Course Name: {self.coursename}\n Students In Course: {self.coursestudents}")
    def add_student(self, student):
        self.coursestudents.append(student)


course1 = course(1, "Mathematics", [])
student1 = student("Emad", "1231231230", [])

course1.add_student(student1)
print(course1)
print(student1)'''


# # Teacher solution:
# class Student:
#
#     def __init__(self,name,id,courseList):
#         self.name = name
#         self.id = id
#         self.courseList = courseList
#         self.coursesGrades = {}
#         for course in self.courseList:
#             self.coursesGrades[course.courseNum]=0
#
#     def __repr__(self):
#         return self.name+", "+str(self.id)
#
#     def printCoursesList(self):
#         for course in self.courseList:
#             print("Courses:", course)
#
#     def addCourse(self,course):
#         for c in self.courseList:
#             if course.courseNum == c.courseNum:
#                 return 'Course already exist'
#         self.courseList.append(course)
#         self.coursesGrades[course.courseNum]=0
#         course.addStudent(self)
#
#
# class Course:
#     def __init__(self,courseNum,courseName,studentsList):
#         self.courseNum = courseNum
#         self.courseName = courseName
#         self.studetsList = studentsList
#
#     def __repr__(self):
#         return str(self.courseNum)+","+self.courseName
#
#     def printStudents(self):
#         for student in self.studetsList:
#             print("Students in the course:",student)
#
#     def addStudent(self,student):
#         for s in self.studetsList:
#             if student.id==s.id:
#                 return 'Student already in course!'
#         self.studetsList.append(student)
#         student.addCourse(self)
#
#
#
# s1 = Student('israel israeli','123456789',[])
# s2 = Student('ploni almoni','987654321',[])
#
# c1 = Course(1111,'Java',[])
# c2 = Course(2222,'Cpp',[])
#
# c1.addStudent(s1)
# s2.addCourse(c1)






############################ Training 11/08/2024 #############################################











class Book:
    def __init__(self, title, author, price, quantity, owners):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
        self.owners = owners

    def update_quantity(self, amount):
        self.quantity = amount

    def apply_discount(self, percent):
        x = (percent / 100) * self.price
        self.price -= x
        return self.price

    def is_in_stock(self):
        if self.quantity > 0:
            return True
        return False

    def add_owner(self, name):
        self.owners.append(name)

    def list_owners(self):
        return self.owners


class Customer:
    def __init__(self, name, purchased_books):
        self.name = name
        self.purchased_books = purchased_books

    def purchase_book(self, book, quantity):
        if book.quantity < quantity:
            print("No stock!")
        else:
            self.purchased_books.append(book)



class Bookstore:
    def __init__(self, name, inventory, customers):
        self.name = name
        self.inventory = inventory
        self.customers = customers






