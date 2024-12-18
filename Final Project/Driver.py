from assets.Stack import Stack
from assets.Queue import Queue

from classes.Customer import Customer
from classes.Employee import Employee
from classes.WorkDay import WorkDay

from classes.Airport import Airport
from classes.Flight import Flight
from classes.Suitcase import Suitcase


# Customers
customer1 = Customer(name="Alice", age=25, id="C1001", is_vip=True)
customer2 = Customer(name="Bob", age=40, id="C1002", is_vip=False)
customer3 = Customer(name="Charlie", age=30, id="C1003", is_vip=True)
customer4 = Customer(name="David", age=22, id="C1004", is_vip=False)
customer5 = Customer(name="Eva", age=35, id="C1005", is_vip=True)
customer6 = Customer(name="Frank", age=28, id="C1006", is_vip=False)
customer7 = Customer(name="Grace", age=45, id="C1007", is_vip=True)
customer8 = Customer(name="Hank", age=50, id="C1008", is_vip=False)
customer9 = Customer(name="Ivy", age=27, id="C1009", is_vip=True)
customer10 = Customer(name="Jack", age=38, id="C1010", is_vip=False)
customer11 = Customer(name="Kara", age=33, id="C1011", is_vip=True)
customer12 = Customer(name="Leo", age=29, id="C1012", is_vip=False)
customer13 = Customer(name="Mia", age=26, id="C1013", is_vip=True)
customer14 = Customer(name="Nina", age=32, id="C1014", is_vip=False)
customer15 = Customer(name="Oscar", age=36, id="C1015", is_vip=True)
customer16 = Customer(name="Paul", age=41, id="C1016", is_vip=False)
customer17 = Customer(name="Quinn", age=34, id="C1017", is_vip=True)
customer18 = Customer(name="Rita", age=37, id="C1018", is_vip=False)
customer19 = Customer(name="Sam", age=23, id="C1019", is_vip=True)
customer20 = Customer(name="Tina", age=31, id="C1020", is_vip=False)


# Employees
employee1 = Employee(name="Emily", id="E1001", age=35, hour_rate=20, workday=None)
employee2 = Employee(name="Daniel", id="E1002", age=45, hour_rate=25, workday=None)
employee3 = Employee(name="Sophia", id="E1003", age=28, hour_rate=22, workday=None)
employee4 = Employee(name="James", id="E1004", age=50, hour_rate=30, workday=None)
employee5 = Employee(name="Liam", id="E1005", age=40, hour_rate=24, workday=None)
employee6 = Employee(name="Olivia", id="E1006", age=33, hour_rate=23, workday=None)
employee7 = Employee(name="Noah", id="E1007", age=38, hour_rate=27, workday=None)
employee8 = Employee(name="Emma", id="E1008", age=29, hour_rate=21, workday=None)
employee9 = Employee(name="Lucas", id="E1009", age=42, hour_rate=26, workday=None)
employee10 = Employee(name="Mia", id="E1010", age=30, hour_rate=20, workday=None)


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

flight6 = Flight(flight_number="F1006", destination="Berlin", day=20, month=12, hour=16,
                 max_passengers=160, price=450, queue=Queue(), suitcases_stack=Stack())

flight7 = Flight(flight_number="F1007", destination="Rome", day=21, month=12, hour=11,
                 max_passengers=180, price=350, queue=Queue(), suitcases_stack=Stack())

flight8 = Flight(flight_number="F1008", destination="Dubai", day=22, month=12, hour=8,
                 max_passengers=200, price=550, queue=Queue(), suitcases_stack=Stack())

flight9 = Flight(flight_number="F1009", destination="Los Angeles", day=23, month=12, hour=10,
                 max_passengers=210, price=400, queue=Queue(), suitcases_stack=Stack())

flight10 = Flight(flight_number="F1010", destination="Cape Town", day=24, month=12, hour=13,
                  max_passengers=190, price=650, queue=Queue(), suitcases_stack=Stack())


# Suit Cases
suitcase1 = Suitcase(owner=customer1, weight=15)
suitcase2 = Suitcase(owner=customer2, weight=20)
suitcase3 = Suitcase(owner=customer3, weight=18)
suitcase4 = Suitcase(owner=customer4, weight=22)
suitcase5 = Suitcase(owner=customer5, weight=17)
suitcase6 = Suitcase(owner=customer6, weight=19)
suitcase7 = Suitcase(owner=customer7, weight=25)
suitcase8 = Suitcase(owner=customer8, weight=23)
suitcase9 = Suitcase(owner=customer9, weight=16)
suitcase10 = Suitcase(owner=customer10, weight=21)


# Airport
airport1 = Airport(code="JFK", flights=[flight1, flight2, flight3, flight4], customers=[customer1], employees=[])


class Driver:
    def __init__(self, name):
        self.name = name

    def ChooseFlight(self, customer_id, budget):
        for cust in airport1.customers:
            if cust.id == customer_id:
                available_flights = [flight for flight in airport1.flights
                                     if flight.price <= budget
                                     and flight.queue.size() < flight.max_passengers]
                if available_flights:
                    print(f"Available flights for {cust.name} within your budget of {budget}:")
                    for flight in available_flights:
                        print(f"{flight.flight_number}: {flight.destination} - ${flight.price}"
                              f"\n {flight.max_passengers - flight.queue.size()}"
                              f" Seats out of {flight.max_passengers} Available")
                else:
                    print(f"No flights available within your budget of {budget}.")
                break
        else:
            print(f"Customer with ID {customer_id} not found.")


driver1 = Driver("Emad")
driver1.ChooseFlight("C1001", 500)

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



