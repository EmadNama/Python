from Person import Person

class Employee(Person):
    def __init__(self, name, id, age, hour_rate, workday=None):
        super().__init__(name, id, age)
        self.hour_rate = hour_rate
        self.workday = workday

    def __repr__(self):
        return f"Employee Information:\nName: {self.name}\nID: {self.id}\nHour Rate: {self.hour_rate}\nWorkday: {self.workday}"
