def GetTuple(tuple):
    dictionary = {}
    for words in tuple:
        dictionary[words] = len(words)
    return dictionary

tuple = ("emad", "hello World!", "avishay", "h", "12", "lotem")
print(GetTuple(tuple))