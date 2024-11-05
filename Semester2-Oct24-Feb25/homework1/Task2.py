# 05/11/2024, Semester B Homework 1 Task 2



class Employee:
    def __init__(self, id, name, monthly_hours, hour_rate):
        self.id = id
        self.name = name
        self.monthly_hours = monthly_hours
        self.hour_rate = hour_rate
        self.monthly_rate = self.monthly_hours*self.hour_rate

    def __repr__(self):
        return f"Employee Information:\nName: {self.name}\nMonthly Hours: {self.monthly_hours}\nHour Rate: {self.hour_rate}\nMonthly Rate: {self.monthly_rate}"

    def GetSalary(self):
        self.monthly_rate = self.monthly_hours*self.hour_rate
        return f"{self.name}'s Salary is {self.monthly_rate}"


class Manager(Employee):
    def __init__(self, id, name, monthly_hours, hour_rate, bonus, managing_level):
        super().__init__(id, name, monthly_hours, hour_rate)
        self.bonus = bonus
        self.managing_level = managing_level
        self.monthly_rate = (self.monthly_hours*self.hour_rate + self.bonus) * self.managing_level


    def __repr__(self):
        return f"Manager Information:\nName: {self.name}\nMonthly Hours: {self.monthly_hours}\nHour Rate: {self.hour_rate}\nBonus: {self.bonus}\nMonthly Rate: {self.monthly_rate}\nManager Level: {self.managing_level}"

    def GetSalary(self):
        return f"{self.name}'s Salary is {self.monthly_rate}"


class Factory:
    def __init__(self, name):
        self.name = name
        self.workers_list = []

    def __repr__(self):
        return f"Factory Name: {self.name}\nWorkers List: {[i.name for i in self.workers_list]}"


    def AddWorker(self, worker):
        self.workers_list.append(worker)

    def GetBestWorker(self):
        x = 0
        employee = None
        for worker in self.workers_list:
            if worker.monthly_hours > x:
                x = worker.monthly_hours
                employee = worker
        if isinstance(employee, Manager):
            return f"The Best Worker In {self.name} is the Manager {employee.name}\nWith a total of {employee.monthly_hours} Monthly Hours"
        return f"The Best Worker In {self.name} is {employee.name}\nWith a total of {employee.monthly_hours} Monthly Hours"

    def Promote(self):
        list = []
        for employee in self.workers_list:
            if employee.monthly_hours > 160:
                if isinstance(employee, Manager):
                    employee.hour_rate *= 1.10
                    employee.monthly_rate = (employee.monthly_hours*employee.hour_rate + employee.bonus) * employee.managing_level
                    list.append((employee.name, employee.monthly_rate))
                else:
                    employee.hour_rate *= 1.10
                    employee.monthly_rate = employee.hour_rate * employee.monthly_hours
                    list.append((employee.name, employee.monthly_rate))
        if list == []:
            return "No Wrokers Found With 160+ Hours This Month"
        return f"Promoted: {list}"

    def BestManagers(self):
        list = []
        for employee in self.workers_list:
            if isinstance(employee, Manager) and employee.managing_level >= 2 and employee.monthly_hours >= 120:
                list.append(employee.name)
        if list == []:
            return "No Managers Found!"
        return f"Best Managers: {list}"


employee1 = Employee("111", "David", 90, 40)
employee2 = Employee("222", "John", 180, 40)
employee3 = Employee("333", "Tommy", 50, 40)

manager1 = Manager("666", "Edgar", 60, 40, 200, 1)
manager2 = Manager("777", "Roni", 170, 40, 200, 2)

factory1 = Factory("Metin")

factory1.AddWorker(employee1)
factory1.AddWorker(employee2)
factory1.AddWorker(employee3)

factory1.AddWorker(manager1)
factory1.AddWorker(manager2)

print("")
print(employee2)
print("")
print(manager2)
print("")
print(factory1)
print("")
print(factory1.GetBestWorker())
print("")
print(factory1.Promote())
print("")
print(factory1.BestManagers())