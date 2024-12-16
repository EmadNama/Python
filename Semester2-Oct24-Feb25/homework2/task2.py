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
    temp = stack()
    temp2 = stack()
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
        elif char in brackets.values():
            if temp.isEmpty():
                return char
            else:
                x = temp.pop()
                if brackets[x] != char:
                    return char
    if not temp.isEmpty():
        return temp.pop()
    return None


# print(findUnmatch("(())"))


def equalStacks(stack1, stack2):
    dict1 = {}
    dict2 = {}
    while not stack2.isEmpty():
        value = stack2.pop()
        if value not in dict2:
            dict2[value] = 1
        else:
            dict2[value] += 1
    while not stack1.isEmpty():
        value = stack1.pop()
        if value not in dict1:
            dict1[value] = 1
        else:
            dict1[value] += 1
    return dict1 == dict2


# stack1 = Stack()
# stack2 = Stack()
# stack1.push(1)
# stack1.push("e")
# stack1.push(2)
#
# stack2.push("e")
# stack2.push(1)
# stack2.push(2)
#
# print(equalStacks(stack1, stack2))


def compressStr(str):
    stack = Stack()
    stack.push((str[0], 1))
    for char in str[1:]:
        last_char, count = stack.pop()
        if char == last_char:
            stack.push((last_char, count + 1))
        else:
            stack.push((last_char, count))
            stack.push((char, 1))
    compressed_str = ""
    while not stack.isEmpty():
        char, count = stack.pop()
        compressed_str = f"{char}{count}" + compressed_str
    return compressed_str

# print(compressStr("aabbbcc"))


def reverseSentence(sentence):
    words = sentence.split()
    reversed_words = []

    for word in words:
        stack = Stack()
        for char in word:
            stack.push(char)
        reversed_word = ""
        while not stack.isEmpty():
            reversed_word += stack.pop()
        reversed_words.append(reversed_word)
    return " ".join(reversed_words)

# sentence = "hello world!"
# print(reverseSentence(sentence))