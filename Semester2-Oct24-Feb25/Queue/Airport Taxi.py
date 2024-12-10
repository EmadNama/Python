import time
import random

class Queue:
    def __init__(self):
        self.stack1 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1) != 0:
            return self.stack1.pop(0)
        else:
            return "Queue is Empty"

    def isEmpty(self):
        return len(self.stack1) == 0

    def peek(self):
        return self.stack1[0]

    def __repr__(self):
        return str([f"{person.firstName}" for person in self.stack1])


class Residence:
    def __init__(self, region):
        self.region = region

class North(Residence):
    def __init__(self, region="North"):
        super().__init__(region)

class South(Residence):
    def __init__(self, region="South"):
        super().__init__(region)

class Center(Residence):
    def __init__(self, region="Center"):
        super().__init__(region)


class Person:
    def __init__(self, firstName, lastName, id, residence, is_vip=False):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.residence = residence
        self.is_vip = is_vip

    def __repr__(self):
        return f"{self.firstName} {self.lastName} (ID: {self.id})"


person1 = Person("John", "Doe", "A12345", North(), is_vip=True)
person2 = Person("Jane", "Smith", "B23456", South())
person3 = Person("Michael", "Johnson", "C34567", Center())
person4 = Person("Emily", "Davis", "D45678", North())
person5 = Person("David", "Martinez", "E56789", South())
person6 = Person("Sophia", "Garcia", "F67890", Center())
person7 = Person("James", "Rodriguez", "G78901", North())
person8 = Person("Olivia", "Wilson", "H89012", South(), is_vip=True)
person9 = Person("William", "Anderson", "I90123", Center())
person10 = Person("Ava", "Thomas", "J01234", North())
person11 = Person("Alexander", "Jackson", "K12345", South())
person12 = Person("Isabella", "White", "L23456", Center())
person13 = Person("Daniel", "Harris", "M34567", North())
person14 = Person("Mia", "Clark", "N45678", South())
person15 = Person("Jacob", "Lewis", "O56789", Center(), is_vip=True)
person16 = Person("Amelia", "Roberts", "P67890", North())
person17 = Person("Ethan", "Walker", "Q78901", South())
person18 = Person("Charlotte", "Young", "R89012", Center())
person19 = Person("Liam", "Allen", "S90123", North())
person20 = Person("Lucas", "Scott", "T01234", South())
person21 = Person("Henry", "Martinez", "U12345", North(), is_vip=True)
person22 = Person("Anna", "Taylor", "V23456", South())
person23 = Person("Mason", "Lopez", "W34567", Center(), is_vip=True)
person24 = Person("Evelyn", "White", "X45678", North())
person25 = Person("Lucas", "Harris", "Y56789", South())
person26 = Person("Zoe", "Evans", "Z67890", Center())
person27 = Person("Chloe", "Miller", "AA78901", North())
person28 = Person("Jackson", "Wilson", "BB89012", South(), is_vip=True)
person29 = Person("Isabella", "Taylor", "CC90123", Center())
person30 = Person("Michael", "Scott", "DD01234", North())
person31 = Person("Liam", "Roberts", "EE12345", South())
person32 = Person("Amelia", "Harris", "FF23456", Center())
person33 = Person("Sophia", "Young", "GG34567", North(), is_vip=True)
person34 = Person("Benjamin", "Miller", "HH45678", South())
person35 = Person("Emma", "Clark", "II56789", Center())
person36 = Person("Noah", "Rodriguez", "JJ67890", North())
person37 = Person("Avery", "Walker", "KK78901", South())
person38 = Person("Ella", "Thomas", "LL89012", Center())
person39 = Person("Matthew", "Lewis", "MM90123", North())
person40 = Person("Aria", "Evans", "NN01234", South(), is_vip=True)


class TaxiBGU:
    def __init__(self):
        self.northqueue = Queue()
        self.southqueue = Queue()
        self.centerqueue = Queue()

    def enqueue(self, person):
        if person.residence.region == "North":
            if person.is_vip:
                temp_queue = Queue()
                temp_queue.enqueue(person)
                while not self.northqueue.isEmpty():
                    temp_queue.enqueue(self.northqueue.dequeue())
                self.northqueue = temp_queue
            else:
                self.northqueue.enqueue(person)
        elif person.residence.region == "South":
            if person.is_vip:
                temp_queue = Queue()
                temp_queue.enqueue(person)
                while not self.southqueue.isEmpty():
                    temp_queue.enqueue(self.southqueue.dequeue())
                self.southqueue = temp_queue
            else:
                self.southqueue.enqueue(person)
        elif person.residence.region == "Center":
            if person.is_vip:
                temp_queue = Queue()
                temp_queue.enqueue(person)
                while not self.centerqueue.isEmpty():
                    temp_queue.enqueue(self.centerqueue.dequeue())
                self.centerqueue = temp_queue
            else:
                self.centerqueue.enqueue(person)

    def display_queues(self):
        print("North Queue:", self.northqueue)
        print("South Queue:", self.southqueue)
        print("Center Queue:", self.centerqueue)


taxi1 = TaxiBGU()

people = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10,
    person11, person12, person13, person14, person15, person16, person17, person18, person19, person20,
    person21, person22, person23, person24, person25, person26, person27, person28, person29, person30,
    person31, person32, person33, person34, person35, person36, person37, person38, person39, person40]

while True:
    person_to_enqueue = random.choice(people)
    print(f"Enqueuing: {person_to_enqueue.firstName}, Heading to {person_to_enqueue.residence.region}, VIP: {person_to_enqueue.is_vip})")
    people.remove(person_to_enqueue)
    taxi1.enqueue(person_to_enqueue)
    taxi1.display_queues()
    time.sleep(4)
    print("")
