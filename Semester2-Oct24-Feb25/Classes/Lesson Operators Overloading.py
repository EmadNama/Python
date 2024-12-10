# #Lesson 29/10/2024
#
# class Shever:
#
#     def __init__(self, up=0, down=1):
#         self.up = up
#         self.down = down
#
#     def __repr__(self):
#         return str(self.up)+"\n--\n"+str(self.down)
#
#     def __add__(self, other):
#         return self.__class__((self.up*other.down)+(self.down*other.up), (self.down*other.down))
#
#     def __mul__(self, other):
#         return self.__class__(self.up*other.up, self.down*other.down)
#
#     def __truediv__(self, other):
#         return self.__class__(self.up*other.down, self.down*other.up)
#
#     def __sub__(self, other):
#         return self.__class__((self.up*other.down)-(self.down*other.up), (self.down*other.down))
#
#
#
# shever1 = Shever(2,3)
# shever2 = Shever(4,6)
#
# print(shever1)
# shever3 = shever1 - shever2
# print(shever3)



#day min 1 max 31
#month min 1 max 12
#hour min 00 max = 23

class DateTime:

    def __init__(self, day, month, year, hour, minutes):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minutes = minutes

    def __repr__(self):
        return f"{self.day}/{self.month}/{self.year} {self.hour}:{self.minutes}"

    def add_days(self, days):
        if self.day + days == 31:
            self.day = 31
        elif self.day + days < 31:
            self.day += days
        elif self.day + days > 31:
            if days == 365:
                self.year += 1
            elif days < 365:
                months = days//31
                self.month += months
                self.day += days%31
            elif days > 365: # inpupt = 1000
                self.year += days//365 #  = 2
                daysmonth = days%365 # = 271
                self.month += daysmonth//31 # = 8
                leftdays = days%31
                self.day += leftdays



datetime1 = DateTime(1,1,2000,17,52)
print(datetime1)
datetime1.add_days(1)
print(datetime1)
