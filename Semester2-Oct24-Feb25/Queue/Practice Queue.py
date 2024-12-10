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
        return self.stack1[0]

    def __repr__(self):
        return str(self.stack1)

queue1 = Queue()
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.enqueue(5)

def multNumbers(queue):
    t = Queue()
    if queue.isEmpty():
        return "Queue is Empty"
    while not queue.isEmpty():
        t.enqueue(queue.dequeue()  * 2)
    return str(t.stack1)

# print(multNumbers(queue1))

def sortEvenOdd(queue):
    t = Queue()
    t2 = Queue()
    if queue.isEmpty():
        return "Queue is Empty"
    while not queue.isEmpty():
        if queue.peek() % 2 == 0:
            t.enqueue(queue.dequeue())
        else:
            t2.enqueue(queue.dequeue())
    while not t2.isEmpty():
        t.enqueue(t2.dequeue())
    return t.stack1

# print(sortEvenOdd(queue1))

queue2 = Queue()
queue2.enqueue(2)
queue2.enqueue(3)


def combineQueues(queue1, queue2):
    t = Queue()
    while not queue1.isEmpty() or not queue2.isEmpty():
        if not queue1.isEmpty():
            t.enqueue(queue1.dequeue())
        if not queue2.isEmpty():
            t.enqueue(queue2.dequeue())
    return t

# print(combineQueues(queue1, queue2))