class stack:
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

def reverseString(str):
    temp = stack()
    retString = ""
    for char in str:
        temp.push(char)
    while not temp.isEmpty():
        retString+=temp.pop()
    return retString

def isBalanced(str):
    brackets = {"(": ")", "[": "]", "{": "}"}
    temp = stack()
    for char in str:
        if char in brackets:
            temp.push(char)
        elif char in brackets.values():
            if brackets[temp.pop()] != char:
                return False
    return temp.isEmpty()

str = ("({})")
print(isBalanced(str))