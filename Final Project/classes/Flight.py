from assets.Stack import Stack
from assets.Queue import Queue

class Flight:
    def __init__(self, flight_number, destination, day, month, hour, max_passengers, price, queue=None, suitcases_stack=None):
        self.flight_number = flight_number
        self.destination = destination
        self.day = day
        self.month = month
        self.hour = hour
        self.max_passengers = max_passengers
        self.price = price
        self.queue = queue
        self.suitcases_stack = suitcases_stack

    def __repr__(self):
        return (f"Flight Information:\n"
                f"Flight Number: {self.flight_number}\n"
                f"Date: {self.day}/{self.month}\n"
                f"Destination: {self.destination}\n"
                f"Time: {self.hour}:00\n"
                f"Max Passengers: {self.max_passengers}\n"
                f"Price: ${self.price}")