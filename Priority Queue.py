# priority 999 - VIP
# priority 3 - Comes after vip and comes after the already waiting with priority 3
# priority 2 - Comes after 3 and comes after the already waiting with priority 2
# priority 1 - always the last

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