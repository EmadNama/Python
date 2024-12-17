class Airport:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.customers = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_customer(self, customer):
        self.customers.append(customer)

    def __repr__(self):
        return f"Airport Information:\nName: {self.name}\nEmployees: {len(self.employees)}\nCustomers: {len(self.customers)}"
