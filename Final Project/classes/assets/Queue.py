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