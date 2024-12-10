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

def removeDuplicates(stack):
    temp = Stack()
    temp2 = Stack()
    while not stack.isEmpty():
        t = stack.pop()
        if temp.top() != t:
            temp.push(t)
    while not temp.isEmpty():
        temp2.push(temp.pop())
    return temp2

def findUnmatch(str):
    brackets = {"(": ")", "[": "]", "{": "}"}
    temp = Stack()
    for char in str:
        if char in brackets:
            temp.push(char)
        elif char in brackets.values() and brackets[temp.pop()] == char:
            continue
        elif char in brackets.values() and temp.size() <= 1:
            return char
        elif char in brackets and temp.size()==1:
            return char
    return None

print(findUnmatch("{}{}"))




