from assets.Stack import Stack
from assets.Queue import Queue

from classes.Customer import Customer
from classes.Employee import Employee
from classes.WorkDay import WorkDay

from classes.Airport import Airport
from classes.Flight import Flight
from classes.Suitcase import Suitcase

import time

# Customers
customer1 = Customer(name="Alice", age=25, id="1", is_vip=True)
customer2 = Customer(name="Bob", age=40, id="2", is_vip=False)
customer3 = Customer(name="Charlie", age=30, id="3", is_vip=True)
customer4 = Customer(name="David", age=22, id="4", is_vip=False)
customer5 = Customer(name="Eva", age=35, id="5", is_vip=True)

# Employees
employee1 = Employee(name="Emily", id="E1001", age=35, hour_rate=20)
employee2 = Employee(name="Daniel", id="E1002", age=45, hour_rate=25)
employee3 = Employee(name="Sophia", id="E1003", age=28, hour_rate=22)
employee4 = Employee(name="James", id="E1004", age=50, hour_rate=30)
employee5 = Employee(name="Liam", id="E1005", age=40, hour_rate=24)

# Work Days
workday1 = WorkDay(day=15, month=12, work_hours=8)
workday2 = WorkDay(day=16, month=12, work_hours=7)

# Flights
flight1 = Flight(flight_number="F1001", destination="New York", day=15, month=12, hour=10,
                 max_passengers=200, price=350, queue=Queue(), suitcases_stack=Stack())

flight2 = Flight(flight_number="F1002", destination="Paris", day=16, month=12, hour=15,
                 max_passengers=140, price=500, queue=Queue(), suitcases_stack=Stack())

flight3 = Flight(flight_number="F1003", destination="London", day=17, month=12, hour=12,
                 max_passengers=150, price=400, queue=Queue(), suitcases_stack=Stack())

flight4 = Flight(flight_number="F1004", destination="Tokyo", day=18, month=12, hour=9,
                 max_passengers=220, price=700, queue=Queue(), suitcases_stack=Stack())

flight5 = Flight(flight_number="F1005", destination="Sydney", day=19, month=12, hour=14,
                 max_passengers=170, price=600, queue=Queue(), suitcases_stack=Stack())

# Suit Cases
suitcase1 = Suitcase(owner=customer1, weight=15)
suitcase2 = Suitcase(owner=customer2, weight=20)
suitcase3 = Suitcase(owner=customer3, weight=18)
suitcase4 = Suitcase(owner=customer4, weight=22)
suitcase5 = Suitcase(owner=customer5, weight=17)

# Airport
airport1 = Airport(code="JFK",
                   flights=[flight1, flight2, flight3, flight4, flight5],
                   customers=[customer1, customer2, customer3, customer4, customer5],
                   employees=[employee1, employee2, employee4, employee5])


def ChooseFlight(customer_id, budget):

    customer_found = False
    for cust in airport1.customers:
        if cust.id == customer_id:
            customer_found = True

            available_flights = [flight for flight in airport1.flights
                                 if flight.price <= budget
                                 and flight.queue.size() < flight.max_passengers]
            if available_flights:
                print(f"Available flights for {cust.name} within your budget of {budget}:")
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
                            if cust.is_vip:
                                temp = Stack()
                                while not flight.suitcases_stack.isEmpty() and flight.suitcases_stack.top().is_vip:
                                    temp.push(flight.suitcases_stack.pop())
                                temp.push(suitcase)
                                flight.overall_weight += suitcase_weight
                                while not flight.suitcases_stack.isEmpty():
                                    temp.push(flight.suitcases_stack.pop())
                                flight.suitcases_stack = temp
                            else:
                                if (flight.max_passengers * 23) > (flight.overall_weight + suitcase_weight):
                                    flight.suitcases_stack.push(suitcase)
                                    flight.overall_weight += suitcase_weight
                                    print(f"Your suitcase (weight: {suitcase_weight} kg) has been added to the flight.")
                                else:
                                    print(f"Your suitcase weight is beyond the limit.")
                            print(f"Checking in, Please wait...")
                            flight.queue.enqueue(cust)
                            flight.price *= 1.02
                            time.sleep(2)
                            print("Checked in successfully, Returning to main menu..")
                            time.sleep(2)
                        elif has_suitcase == "no":
                            print(f"Checking in, Please wait...")
                            flight.queue.enqueue(cust)
                            flight.price *= 1.02
                            time.sleep(2)
                            print("Checked in successfully, Returning to main menu..")
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


def AddWorkDay(employee_id):
    emp_found = False
    for emp in airport1.employees:
        if emp.id == employee_id:
            emp_found = True
            workday_day = int(input("Put the day: "))
            workday_month = int(input("Put the month: "))
            workday_hours = int(input("Hours: "))
            workday = WorkDay(workday_day, workday_month, workday_hours)
            emp.workday.append(workday)
            print("Adding Work Day, Please wait...")
            time.sleep(2)
            print(f"Successfully Added {workday_day}/{workday_month} with {workday_hours} Hours"
                  f"To {emp.name}")
            print("Returning to the main menu...")
            time.sleep(2)

    if emp_found == False:
        print("Employee Not Found")
        time.sleep(2)
        print("Returning to the main menu....")
        time.sleep(2)

def EmployeeSalary(employee_id):
    emp_found = False
    for emp in airport1.employees:
        if emp.id == employee_id:
            emp_found = True
            month = int(input("Month: "))
            sum = 0
            for workday in emp.workday:
                if workday.month == month:
                    sum += (workday.work_hours * emp.hour_rate)
            print(sum)
    if not emp_found:
        print("Employee Not Found")
        time.sleep(2)
        print("Returning to the main menu....")
        time.sleep(2)


def FlightEnded(flight_id):
    flight_found = False
    for flight in airport1.flights:
        if flight.id == flight_id:
            flight_found = True
            while not flight.suitcases_stack.isEmpty():
                flight.suitcases_stack.pop()
                time.sleep(2)
    if not flight_found:
        print("Flight Not Found")
        time.sleep(2)
        print("Returning to the main menu....")
        time.sleep(2)


def Main():
    while True:
        print(f"\n        Welcome to {airport1.code} Airport")
        print("=" * 40)
        print(f"      Please Choose an Operation:\n")

        print("[1] - Add Flight")
        print("[2] - Add Customer")
        print("[3] - Add Employee")
        print("[4] - Offer Flight")
        print("[5] - Update Employee Work Hours")
        print("[6] - View Employee Salary")
        print("[7] - View Employees List")
        print("[8] - Report Flight Landed")
        print("[9] - Exit")

        x = input("\nEnter the number of your choice (1-9): ")

        if x == "1":
            print("\nYou chose to Add a Flight.")

            flight_number = input("Enter Flight Number: ")
            destination = input("Enter Flight Destination: ")
            day = int(input("Enter the day of the flight (1-31): "))
            month = int(input("Enter the month of the flight (1-12): "))
            hour = int(input("Enter the hour of departure (0-23): "))
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

            print("Adding Flight, Please wait...")
            time.sleep(2)
            print("Checking Flight Information...")
            time.sleep(3)
            flight_exists = False
            for f in airport1.flights:
                if f.flight_number == flight.flight_number:
                    flight_exists = True
                    print(f"\nFlight {flight_number} already exists")
                    print("Returning to main menu...")
                    time.sleep(2)
            if not flight_exists:
                airport1.AddFlight(flight)
                print(f"\nFlight {flight_number} Added Successfully to {airport1.code}\n")
                print(flight)
                time.sleep(3)


        elif x == "2":
            print("\nYou chose to Add Customer.")
            name = input("Enter Customer Name: ")
            age = int(input("Enter Customer Age: "))
            customer_id = input("Enter Customer ID: ")
            is_vip = input("Is the customer a VIP? (Yes/No): ").strip().lower()
            is_vip = True if is_vip == "yes" else False
            customer = Customer(
                name=name,
                age=age,
                id=customer_id,
                is_vip=is_vip
            )
            print("\nAdding Customer, Please wait...")
            time.sleep(2)
            print(f"Checking Customer Information...")
            time.sleep(2)
            airport1.AddCustomer(customer)
            print(f"\nCustomer {customer_id} Added Successfully to {airport1.code}")
            print(customer)
            time.sleep(1)
            print("\nReturning to the main menu...")
            time.sleep(2)


        elif x == "3":
            print("\nYou chose to Add Employee.")
            name = input("Enter Employee Name: ")
            employee_id = input("Enter Employee ID: ")
            age = int(input("Enter Employee Age: "))
            hour_rate = float(input("Enter Employee Hourly Rate: "))
            employee = Employee(
                name=name,
                id=employee_id,
                age=age,
                hour_rate=hour_rate,
            )
            print("\nAdding Employee, Please wait...")
            time.sleep(2)
            print(f"Checking Employee Information...")
            time.sleep(2)
            airport1.AddEmployee(employee)
            print(f"\nEmployee {employee_id} Added Successfully to {airport1.code}")
            print(employee)
            time.sleep(1)
            print("\nReturning to the main menu...")
            time.sleep(2)


        elif x == "4":

            print("\nYou chose to Offer Flight.")

            customer_id = input("Enter the Customer ID: ")
            budget = float(input("Enter the Customer's Budget: "))

            ChooseFlight(customer_id, budget)
            time.sleep(3)

        elif x == "5":
            print("You chose to Update Employee Work Hours.")
            id = str(input("Put Employee ID: "))
            AddWorkDay(id)

        elif x == "6":
            print("You chose to View Employee Salary.")
            id = str(input("Put Employee ID: "))
            EmployeeSalary(id)

        elif x == "7":
            print("You chose To View Employees List:")

        elif x == "8":
            print("You chose IDK. Let's figure it out together!")

        elif x == "9":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid option. Please choose a valid number between 1 and 9.")

Main()




























# def Menu():
#     print(f"Welcome to {airport1.code} Airport"
#           f"\nPlease Choose Operation:"
#           f"\n - Add Flight"
#           f"\n - Add Customer"
#           f"\n - Offer Flight"
#           f"\n - Update Flight"
#           f"\n - Add Employee"
#           f"\n - Update Employee Work Hours"
#           f"\n - View Workers List"
#           f"\n - IDK"
#           f"\n - Exit")
#
# Menu()



