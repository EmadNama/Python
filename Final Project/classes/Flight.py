from assets.Queue import Queue
from assets.Stack import Stack


class Flight:
    def __init__(self, flight_number, month, day, hour, destination, max_passengers, time=None):
        self.flight_number = flight_number
        self.date = date
        self.destination = destination
        self.origin = origin
        self.time = time

    def __repr__(self):
        return f"Flight Information:\nFlight Number: {self.flight_number}\nDate: {self.date}\nDestination: {self.destination}\nOrigin: {self.origin}\nTime: {self.time}"
