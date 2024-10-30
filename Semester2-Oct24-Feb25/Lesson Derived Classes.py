class Employee:

    raise_mult = 10
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __repr__(self):
        return f"Employee Information\nFull Name: {self.firstname} {self.lastname}\nSalary: {self.salary}"

    def full_name(self):
        return f"Full Name: {self.firstname} {self.lastname}"

    def apply_raise(self):
        self.salary *= Employee.raise_mult

class Developer(Employee):
    raise_mult = 100

    def __init__(self, firstname, lastname, salary, language):
        super().__init__(firstname, lastname, salary)
        self.language = language

class Manager(Employee):

    def __init__(self, firstname, lastname, salary, list_employees):
        super().__init__(firstname, lastname, salary)
        self.list_employees = list_employees

    def add_employee(self, employee):
        self.list_employees.append(employee)

    def remove_employee(self, name):
        for employee in self.list_employees:
            if employee.firstname == name:
                self.list_employees.remove(employee)

    def print_employees(self):
        return [employee.firstname for employee in self.list_employees]


e1 = Employee("Eric", "Fox", 15000)
# print(e1.full_name())

d1 = Developer("Morris", "Alba", 30000, "Java")
# print(d1.full_name())
#
# manager1 = Manager("Emad", "Nama", 40000, [e1, d1])
# print(manager1.print_employees())
# manager1.remove_employee("Eric")
# print(manager1.print_employees())
print(d1)
d1.apply_raise()
print(d1)