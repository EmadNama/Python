class University:

    def __init__(self, name):
        self.name = name
        self.faculties = []

    def __repr__(self):
        return f"University Name: {self.name}\nUniversity Faculties: {self.faculties}"

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def remove_faculty(self, faculty_name):
        for faculty in self.faculties:
            if faculty.name == faculty_name:
                self.faculties.remove(faculty)
            else:
                print("Faculty not found!")

    def find_faculty(self, faculty_name):
        for faculty in self.faculties:
            if faculty.name == faculty_name:
                print(faculty)
            else:
                print("Faculty not found!")

    def display_faculties(self):
        print(f"{self.name} Faculties: {self.faculties}")


class Faculty:

    def __init__(self, name):
        self.name = name
        self.departments = []

    def __repr__(self):
        return f"Faculty Name: {self.name}, Departments: {self.departments}"

    def add_department(self, department):
        self.departments.append(department)

    def remove_department(self, department_name):
        for department in self.departments:
            if department.name == department_name:
                self.departments.remove(department)
            else:
                print("Department not found!")

    def find_department(self, department_name):
        for department in self.departments:
            if department.name == department_name:
                print(department)
            else:
                print("Department not found!")

    def display_departments(self):
        print(f"{self.name} Departments: {self.departments}")



class Department:

    def __init__(self, name):
        self.name = name
        self.courses = []

    def __repr__(self):
        return f"Department Name: {self.name}, Courses: {self.courses}"

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course_name):
        for course in self.courses:
            if course.name == course_name:
                self.courses.remove(course)
            else:
                print("Course not found!")

    def find_course(self, course_name):
        for course in self.courses:
            if course.name == course_name:
                print(course)
            else:
                print("Course not found!")

    def display_courses(self):
        print(f"{self.name} Courses: {self.courses}")

class Course:

    def __init__(self, name):
        self.name = name
        self.max_students = 20
        self.students = []

    def __repr__(self):
        return f"Course Name: {self.name}, Max Students: {self.max_students}, Grades: {self.grades}"



class Student:

    def __init__(self, name, id_number, start_year):
        self.name = name
        self.id_number = id_number
        self.start_year = start_year




#Testing University:

university1 = University("Sami Shamoon") #Create University
faculty1 = Faculty("Faculty of Engineering") #Create Faculty

university1.add_faculty(faculty1) #Adding a faculty to university
university1.display_faculties() #Displaying university faculties after adding

university1.find_faculty("Faculty of Engineering") #Sending a faculty name to return it as an object

university1.remove_faculty("Faculty of Engineering") #Removing a faculty from university
university1.display_faculties() #Displaying university faculties after removal


#Testing Faculty:

department1 = Department("Department of Mathematics") #Create Department

faculty1.add_department(department1) #Adding a department
faculty1.display_departments() #Display after Add

faculty1.find_department("Department of Mathematics") #Find object by name

faculty1.remove_department("Department of Mathematics") #Remove object by name
faculty1.display_departments() #Display after remove


#Testing Department:

course1 = Course("Calculus")

department1.add_course(course1) #Adding a course
department1.display_courses() #Display after add

department1.find_course("Calculus") #Find Object by name

department1.remove_course("Calculus") #Remove object by name
department1.display_courses() #Display after removal
