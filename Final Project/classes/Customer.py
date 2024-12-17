from .Person import Person

class Customer(Person):
    def __init__(self, name, age, id, is_vip=False):
        super().__init__(name, id, age)
        self.is_vip = is_vip

    def __repr__(self):
        return f"Customer Information:\nName: {self.name}\nID: {self.id}\nVIP: {self.is_vip}"
