class ID:
    def __init__(self, id):
        self.id = id

    def IdWithLastDigit(self):
        if len(self.id) > 8:
            return("8 Digits only!")
        elif len(self.id) < 8:
            while len(self.id) < 8:
                self.id = "0" + self.id
        sum = 0
        for digit in (self.id[1::2]):
            digit = int(digit)
            digit = digit * 2
            if digit >= 10:
                digit = (digit%10) + (digit//10)
                sum += digit
            else:
                sum += (digit)
        for digit in (self.id[0::2]):
            sum+=int(digit)
        lastdigit = (10 - sum%10)
        return self.id + str(lastdigit)




newid = ID("32306989")
print(newid.IdWithLastDigit())


