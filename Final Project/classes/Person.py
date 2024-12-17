class Person:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def __repr__(self):
        return f"Person Infromation:\nName: {self.name}\nAge: {self.age}\nID: {self.id})"
