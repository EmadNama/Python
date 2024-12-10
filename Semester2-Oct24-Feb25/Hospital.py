import time
import random


class Stack:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def top(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)


class PriorityQueue:
    def __init__(self):
        self.stack1 = []

    def enqueue(self, item):
        inserted = False
        for i in range(len(self.stack1)):
            if self.stack1[i].priority < item.priority:
                self.stack1.insert(i, item)
                inserted = True
                break
        if not inserted:
            self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1) != 0:
            return self.stack1.pop(0)
        else:
            return "Queue is Empty"

    def isEmpty(self):
        return len(self.stack1) == 0

    def peek(self):
        if not self.isEmpty():
            return self.stack1[0]

    def __repr__(self):
        return str(self.stack1)


class Person:

    def __init__(self, name, id, priority):
        self.name = name
        self.id = id
        self.priority = priority

    def __repr__(self):
        return self.name


class Hospital:

    def __init__(self):
        self.queue = PriorityQueue()
        self.history = Stack()

    def __repr__(self):
        return f"Queue: {self.queue}\nHistory: {self.history}"

    def addPatient(self, item):
        self.queue.enqueue(item)


patient1 = Person("Ebrahim", "9655", 999)
patient2 = Person("John", "5678", 1)
patient3 = Person("Emily", "9101", 2)
patient4 = Person("Michael", "1122", 3)
patient5 = Person("Sarah", "3344", 1)
patient6 = Person("David", "5566", 1)
patient7 = Person("Jessica", "7788", 999)
patient8 = Person("Daniel", "9900", 3)
patient9 = Person("Sophia", "2233", 1)
patient10 = Person("William", "4455", 2)
patient11 = Person("Olivia", "6677", 3)
patient12 = Person("Alice", "1111", 999)
patient13 = Person("Bob", "2222", 2)
patient14 = Person("Charlie", "3333", 3)
patient15 = Person("Diana", "4444", 1)
patient16 = Person("Eva", "5555", 2)
patient17 = Person("Frank", "6666", 999)
patient18 = Person("Grace", "7777", 2)
patient19 = Person("Hannah", "8888", 2)
patient20 = Person("Iris", "9999", 3)

hospital1 = Hospital()


patients = [patient1, patient2, patient3, patient4, patient5, patient6, patient7,
            patient8, patient9, patient10, patient11, patient12, patient13,
            patient14, patient15, patient16, patient17, patient18, patient19,
            patient20]

def main():

    while True:
        patient_to_add = random.choice(patients)
        patients.remove(patient_to_add)
        print(f"Adding {patient_to_add.name} to the queue with priority {patient_to_add.priority}")
        hospital1.addPatient(patient_to_add)
        print(hospital1)
        time.sleep(5)
        print("")

main()
