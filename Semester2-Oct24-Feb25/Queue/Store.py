import time
import random

class Queue:
    def __init__(self):
        self.stack1 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1)!=0:
            return self.stack1.pop(0)
        else:
            return "Queue is Empty"

    def isEmpty(self):
        return len(self.stack1) == 0

    def peek(self):
        if not self.isEmpty():
            return self.stack1[0]
        else:
            return None

    def __repr__(self):
        return str(self.stack1)

class Customer:

    def __init__(self, name, id, priority):
        self.name = name
        self.id = id
        self.priority = priority
    def __repr__(self):
        return f"Customer Information:\nName: {self.name}\nID: {self.id}\nPriority Level: {self.priority}"

class Store:

    def __init__(self, name):
        self.name = name
        self.queue = Queue()
    def __repr__(self):
        return f"Store Queue: {[customer.name for customer in self.queue.stack1]}"

    def addCustomer(self, customer):
        if customer.priority == 3:
            temp = Queue()
            while not self.queue.isEmpty() and self.queue.peek().priority == 3:
                temp.enqueue(self.queue.dequeue())
            temp.enqueue(customer)
            while not self.queue.isEmpty():
                temp.enqueue(self.queue.dequeue())
            self.queue = temp
        elif customer.priority == 2:
            temp = Queue()
            while not self.queue.isEmpty() and self.queue.peek().priority >= 2:
                temp.enqueue(self.queue.dequeue())
            # while not self.queue.isEmpty() and self.queue.peek().priority == 2:
            #     temp.enqueue(self.queue.dequeue())
            temp.enqueue(customer)
            while not self.queue.isEmpty():
                temp.enqueue(self.queue.dequeue())
            self.queue = temp
        else:
            self.queue.enqueue(customer)

    def serveCustomer(self):
        if self.queue.isEmpty():
            print("There are not customers to serve!")
        else:
            print(f"{self.queue.dequeue().name} Served Successfully\nUpdated Queue: {[customer.name for customer in self.queue.stack1]}")

    def findCustomer(self, id):
        temp = Queue()
        flag = False
        while not self.queue.isEmpty():
            t = self.queue.dequeue()
            if t.id == id:
                print(f"Customer Found!\nCustomer Name: {t.name}")
                flag = True
            temp.enqueue(t)
        self.queue = temp
        if not flag:
            print("Customer not found!")

    def promoteCustomer(self, id):
        temp = Store("temp")
        flag = False
        while not self.queue.isEmpty():
            t = self.queue.dequeue()
            if t.id == id and t.priority < 3:
                t.priority += 1
                flag = True
            temp.addCustomer(t)
        self.queue = temp.queue
        if not flag:
            print("Customer already has a priority level of 3")

store1 = Store("Store of Calculus")

customer1 = Customer("Ebrahim", "9655", 1)
customer2 = Customer("John", "5678", 1)
customer3 = Customer("Emily", "9101", 2)
customer4 = Customer("Michael", "1122", 3)
customer5 = Customer("Sarah", "3344", 1)
customer6 = Customer("David", "5566", 1)
customer7 = Customer("Jessica", "7788", 3)
customer8 = Customer("Daniel", "9900", 3)
customer9 = Customer("Sophia", "2233", 2)
customer10 = Customer("William", "4455", 2)
customer11 = Customer("Olivia", "6677", 3)
customer12 = Customer("Alice", "1111", 1)
customer13 = Customer("Bob", "2222", 2)
customer14 = Customer("Charlie", "3333", 3)
customer15 = Customer("Diana", "4444", 1)
customer16 = Customer("Eva", "5555", 2)
customer17 = Customer("Frank", "6666", 3)
customer18 = Customer("Grace", "7777", 2)
customer19 = Customer("Hannah", "8888", 2)
customer20 = Customer("Iris", "9999", 3)


list_customers = [customer1, customer2, customer3, customer4, customer5, customer6, customer7, customer8, customer9, customer10,
customer11, customer12, customer13, customer14, customer15, customer16, customer17, customer18, customer19, customer20]

def main():
    while True:
        x = random.randint(0,100)
        if x < 85:
            customer_to_add = random.choice(list_customers)
            list_customers.remove(customer_to_add)
            print(f"Adding {customer_to_add.name} to the queue with priority {customer_to_add.priority}")
            store1.addCustomer(customer_to_add)
            print(store1)
            time.sleep(3.5)
            print("")
        else:
            store1.serveCustomer()
            time.sleep(3.5)
            print("")
main()