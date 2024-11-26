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
    def __repr__(self):
        return str(self.items)

'''reverse string'''

def reverseString(str):
    temp = stack()
    retString = ""
    for char in str:
        temp.push(char)
    while not temp.isEmpty():
        retString+=temp.pop()
    return retString

    #
    # b1 = "("
    # b1x = ")"
    # b2 = "{"
    # b2x = "}"
    # b3 = "["
    # b3x = "]"
    # b_list = ["(", ")", "{", "}", "[", "]"]
    # b_closers = [")", "}", "]"]
    # b_openers = ["(", "{", "["]
# print(reverseString("hello"))

# def isBalanced(str):
#     brackets = {"(": ")", "[": "]", "{": "}"}
#     temp = stack()
#     for char in str:
#         if char in brackets:
#             temp.push(char)
#         elif char in brackets.values():
#             if temp.isEmpty() or brackets[temp.pop()] != char:
#                 return False
#     return temp.isEmpty()


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