class Airport:
    def __init__(self, code, flights, customers, employees):
        self.code = code
        self.flights = flights
        self.customers = customers
        self.employees = employees

    def AddCustomer(self, customer):
        self.customers.append(customer)

    def AddFlight(self, flight):
        self.flights.append(flight)

    def AddEmployee(self, employee):
        self.employees.append(employee)

    def __repr__(self):
        return (f"Airport Information:\n"
                f"Airport Code: {self.code}\n"
                f"Flights: {self.flights}\n"
                f"Employees: {self.employees}\n"
                f"Customers: {self.customers}")