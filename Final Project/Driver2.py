import time
from assets.Stack import Stack
from assets.Queue import Queue
from classes.Customer import Customer
from classes.Employee import Employee
from classes.WorkDay import WorkDay
from classes.Flight import Flight
from classes.Suitcase import Suitcase

class Airport:
    def __init__(self, code, flights, customers, employees):
        self.code = code
        self.flights = flights
        self.customers = customers
        self.employees = employees

    def __repr__(self):
        return (f"Airport Information:\n"
                f"Airport Code: {self.code}\n"
                f"Flights: {self.flights}\n"
                f"Employees: {self.employees}\n"
                f"Customers: {self.customers}")

    def AddCustomer(self):
        name = input("Enter Customer Name: ")
        customer_id = input("Enter Customer ID: ")
        age = input("Enter Customer Age: ")
        is_vip = input("Is the customer a VIP? (Yes/No): ").strip().lower()
        is_vip = True if is_vip == "yes" else False
        customer = Customer(
            name=name,
            age=age,
            id=customer_id,
            is_vip=is_vip
        )
        print("\nAdding Customer, Please wait...")
        time.sleep(1)
        print(f"Checking Customer Information...")
        time.sleep(1)
        for c in self.customers:
            if c.id == customer.id:
                print(f"\nCustomer {customer_id} already exists\n")
                time.sleep(1)
                print("Returning to main menu...")
                time.sleep(2)
            return
        self.customers.append(customer)
        print(f"\nCustomer {customer_id} Added Successfully to {self.code}")
        time.sleep(1)
        print("\nReturning to main menu...")
        time.sleep(2)

    def AddFlight(self):
        flight_number = input("Enter Flight Number: ")
        destination = input("Enter Flight Destination: ")
        day = int(input("Enter the day of the flight (1-31): "))
        while not 1<=day<=31:
            print("Wrong Day, Only between 1 - 31")
            day = int(input("Enter the day of the flight (1-31): "))

        month = int(input("Enter the month of the flight (1-12): "))
        while not 1<=month<=12:
            print("Wrong Month, Only between 1 - 12")
            month = int(input("Enter the month of the flight (1-12): "))

        hour = int(input("Enter the hour of departure (1-24): "))
        while not 1<=hour<=24:
            print("Wrong Hour, Only between 1 - 24")
            hour = int(input("Enter the hour of departure (1-24): "))
        max_passengers = int(input("Enter the maximum number of passengers: "))
        price = float(input("Enter the flight price: "))

        flight = Flight(
            flight_number=flight_number,
            destination=destination,
            day=day,
            month=month,
            hour=hour,
            max_passengers=max_passengers,
            price=price,
            queue=Queue(),
            suitcases_stack=Stack()
        )

        print("\nAdding Flight, Please wait...")
        time.sleep(1)
        print("Checking Flight Information...")
        time.sleep(1)
        for f in self.flights:
            if f.flight_number == flight.flight_number:
                print(f"\nFlight {flight_number} already exists")
                time.sleep(1)
                print("\nReturning to main menu...")
                time.sleep(2)
                return
        self.flights.append(flight)
        print(f"\nFlight {flight_number} Added Successfully to {airport.code}")
        time.sleep(1)
        print("\nReturning to main menu...")
        time.sleep(2)

    def AddEmployee(self):

        name = input("Enter Employee Name: ")
        employee_id = input("Enter Employee ID: ")
        age = input("Enter Employee Age: ")
        hour_rate = float(input("Enter Employee Hourly Rate: "))

        employee = Employee(
            name=name,
            id=employee_id,
            age=age,
            hour_rate=hour_rate,
        )

        print("\nAdding Employee, Please wait...")
        time.sleep(1)
        print(f"Checking Employee Information...")
        time.sleep(1)
        for c in self.employees:
            if c.id == employee.id:
                print(f"\nEmployee {employee_id} already exists")
                time.sleep(1)
                print("\nReturning to main menu...")
                time.sleep(2)
            return
        self.employees.append(employee)
        print(f"\nEmployee {employee_id} Added Successfully to {self.code}")
        time.sleep(1)
        print("\nReturning to main menu...")
        time.sleep(2)

    def ChooseFlight(self):
        customer_id = input("Enter the Customer ID: ")
        budget = float(input("Enter the Customer's Budget: "))
        customer_found = False
        for cust in self.customers:
            if cust.id == customer_id:
                customer_found = True
                available_flights = [flight for flight in self.flights
                                     if flight.price <= budget
                                     and flight.queue.size() < flight.max_passengers]
                if available_flights:
                    print(f"\nAvailable flights for {cust.name} within the budget of {budget}:\n")
                    for flight in available_flights:
                        print(f"{flight.flight_number}: {flight.destination} - ${flight.price}"
                              f"\n {flight.max_passengers - flight.queue.size()} Seats out of {flight.max_passengers} Available")

                    x = input("\nEnter the flight of your choice: ")
                    flight_found = False
                    for flight in available_flights:
                        if flight.flight_number == x:
                            flight_found = True

                            has_suitcase = input("Do you have a suitcase? (Yes/No): ").strip().lower()
                            if has_suitcase == "yes":
                                suitcase_weight = float(input("Enter the weight of your suitcase (in kg): "))
                                suitcase = Suitcase(owner=cust, weight=suitcase_weight)
                                temp = Stack()
                                if cust.is_vip:
                                    while not flight.suitcases_stack.isEmpty() and flight.suitcases_stack.top().owner.is_vip:
                                        temp.push(flight.suitcases_stack.pop())
                                    temp.push(suitcase)
                                    while not temp.isEmpty():
                                        flight.suitcases_stack.push(temp.pop())
                                    flight.overall_weight += suitcase_weight
                                else:
                                    if (flight.max_passengers * 23) > (flight.overall_weight + suitcase_weight):
                                        while not flight.suitcases_stack.isEmpty():
                                            temp.push(flight.suitcases_stack.pop())
                                        flight.suitcases_stack.push(suitcase)
                                        while not temp.isEmpty():
                                            flight.suitcases_stack.push(temp.pop())
                                        flight.overall_weight += suitcase_weight
                                    else:
                                        print(f"\nYour suitcase weight is beyond the limit.")
                                print(f"\nChecking in, Please wait...")
                                flight.queue.enqueue(cust)
                                flight.price *= 1.02
                                time.sleep(2)
                                print("\nChecked in successfully, Returning to main menu..")
                                time.sleep(2)
                            elif has_suitcase == "no":
                                print(f"\nChecking in, Please wait...")
                                flight.queue.enqueue(cust)
                                flight.price *= 1.02
                                time.sleep(2)
                                print("\nChecked in successfully, Returning to main menu..")
                                time.sleep(2)
                    if not flight_found:
                        print("Flight not found, Returning to the main menu...")
                        time.sleep(2)
                else:
                    print(f"No flights available within your budget of {budget}.")
                    print("Returning to the main menu...")
                    time.sleep(2)
                break
        if not customer_found:
            print(f"Customer with ID {customer_id} not found, Returning to the main menu... ")
            time.sleep(2)

    def AddWorkDay(self, employee_id):

        for emp in self.employees:
            if emp.id == employee_id:
                workday_day = input("Which Day? : ")
                workday_month = input("Which Month?: ")
                workday_hours = int(input("How Many Hours?: "))
                workday = WorkDay(workday_day, workday_month, workday_hours)
                emp.workdays.append(workday)
                print("\nAdding Work Day, Please wait...")
                time.sleep(1)
                print(f"\nSuccessfully Added {workday_day}/{workday_month} with {workday_hours} Hours "
                      f"To {emp.name}")
                time.sleep(1)
                print("\nReturning to the main menu...")
                time.sleep(2)
                return
        print("\nEmployee Not Found")
        time.sleep(1)
        print("\nReturning to the main menu....")
        time.sleep(2)

    def EmployeeSalary(self, employee_id, month):
        employee = None
        for emp in self.employees:
            if emp.id == employee_id:
                employee = emp
        if employee:
            sum = 0
            for workday in employee.workdays:
                    if workday.month == month:
                        sum += (workday.work_hours * employee.hour_rate)
                        print(f"\n{employee.name} has earned a total of {sum} in that month")
                        time.sleep(1)
                        print("\nReturning to the main menu....")
                        time.sleep(2)
        else:
            print("\nEmployee Not Found")
            time.sleep(1)
            print("\nReturning to the main menu....")
            time.sleep(2)

    def EmployeeSalary2(self, employee, month):
            sum = 0
            for workday in employee.workdays:
                    if workday.month == month:
                        sum += (workday.work_hours * employee.hour_rate)
            return sum

    def ViewEmployees(self):
        month = input("For which month?: ")
        temp = []
        for emp in self.employees:
            temp.append((emp.name, self.EmployeeSalary2(emp, month)))
        self.BubbleSort(temp)
        print(f"{self.code}'s Employees Salaries for month {month}: ")
        while not len(temp) == 0:
            highest = temp.pop(0)
            print(f"{highest[0]}, {highest[1]}")

    def BubbleSort(self, lst):
        n = len(lst)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if lst[j][1] < lst[j + 1][1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst

    def FlightEnded(self):
        flight_id = input("Flight Number: ")
        flight_found = False
        for flight in self.flights:
            if flight.flight_number == flight_id:
                flight_found = True
                print(f"\nFlight Landed Successfully, Unloading Baggage...\n")
                while not flight.suitcases_stack.isEmpty():
                    print(flight.suitcases_stack.pop())
                    time.sleep(2)
        if not flight_found:
            print("Flight Not Found")
            time.sleep(2)
            print("Returning to the main menu....")
            time.sleep(2)

    def Main(self):
        while True:
            print(f"\n        Welcome to {self.code} Airport")
            print("=" * 40)
            print(f"      Please Choose an Operation:\n")

            print("[1] - Add Flight")
            print("[2] - Add Customer")
            print("[3] - Add Employee")
            print("[4] - Offer Flight")
            print("[5] - Add A Work Day For Employee")
            print("[6] - View Employee Salary")
            print("[7] - View Employees List")
            print("[8] - Report Flight Landed")
            print("[9] - Exit")

            x = input("\nEnter the number of your choice (1-9): ")

            if x == "1":
                print("\nYou chose to add a flight.\n")
                self.AddFlight()

            elif x == "2":
                print("\nYou chose to add Customer.\n")
                self.AddCustomer()

            elif x == "3":
                print("\nYou chose to add employee.\n")
                self.AddEmployee()

            elif x == "4":
                print("\nYou chose to offer flight.\n")
                self.ChooseFlight()

            elif x == "5":
                print("\nYou chose to add a work day for an employee.\n")
                id = str(input("Put Employee ID: "))
                self.AddWorkDay(id)

            elif x == "6":
                print("\nYou chose to view employee salary.\n")
                id = input("Put Employee ID: ")
                month = input("For which month?: ")
                self.EmployeeSalary(id, month)

            elif x == "7":
                print("\nYou chose to view employees list:\n")
                self.ViewEmployees()

            elif x == "8":
                print("\nYou chose to report flight landed\n")
                self.FlightEnded()

            elif x == "9":
                print("\nExiting. Have a great day!")
                break
            else:
                print("Invalid option. Please choose a valid number between 1 and 9.")

airport = Airport(code="JFK",
                   flights=[],
                   customers=[],
                   employees=[])
airport.Main()