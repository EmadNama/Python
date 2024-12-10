# class Queue:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def enqueue(self,item):
#         self.stack1.append(item)
#         print(self.stack1)
#
#     def dequeue(self):
#         if len(self.stack2) == 0:
#             while len(self.stack1) != 0:
#                 self.stack2.append(self.stack1[-1])
#                 self.stack1.pop()
#             dequeued = self.stack2.pop()
#             print(f"{dequeued} Dequeued Successfully")
#         else:
#             dequeued = self.stack2.pop()
#             print(f"{dequeued} Dequeued Successfully")
#
# shop = Queue()
#
# shop.enqueue(1)



class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
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

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)
        print(self.stack1)

    def dequeue(self):
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        if not self.stack2.isEmpty():
            dequeued = self.stack2.pop()
            print(f"{dequeued} Dequeued Successfully")
        else:
            print("Queue is empty!")

shop = Queue()
shop.enqueue(1)
shop.enqueue(2)
shop.enqueue(3)
shop.enqueue(4)
shop.enqueue(5)
shop.enqueue(6)
shop.dequeue()
shop.enqueue(7)





