# #class Address and Person:
#
#
# class Address:
#
#     def __init__(self, city, street, house):
#         self.city = city
#         self.street = street
#         self.house = house
#
#     def __repr__(self):
#         return(f"Address1\nCity: {self.city}, Street: {self.street}, House: {self.house}")
#
#
# class Person:
#
#     def __init__(self, name, birth_year, address):
#         self.name = name
#         self.birth_year = birth_year
#         self.address = address
#
#     def __repr__(self):
#         return(f"Name: {self.name}, Birth Year: {self.birth_year}, Address: {self.address}")
#
#     def update_address(self, new_address):
#         self.address = new_address
#
#     def age_calc(self):
#         return 2024 - self.birth_year
#
#     def check_neighbor(self, person1):
#         if (self.address.city == person1.address.city) and (self.address.street == person1.address.street):
#             return True
#         return False
#
# address1 = Address("Beer Sheva", "Moriyah", 3)
# address2 = Address("Beer Sheva", "Moriyah", 3)
#
# person1 = Person("Emad", 2001, address1)



#class Account and Customer:

class Account:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance
        self.history = {}
    def __repr__(self):
        return(f"Account Number: {self.number}, Account Balance: {self.balance}")
    def deposit(self, amount):
        self.balance += amount
        self.history["deposit"] = amount
        return f"Deposit Success\nYour balance now holds {self.balance}"
    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            return "You don't have this amount!!"
        else:
            self.balance -= amount
            self.history["withdraw"] = amount
            return f"Withdraw Success\nYour balance now holds {self.balance}"
    def account_history(self):
        return self.history

class Customer:
    def __init__(self, name, id, account):
        self.name = name
        self.id = id
        self.account = account
    def __repr__(self):
        return(f"Name: {self.name}, ID: {self.id}, Account: {self.account.number}")

    def transfer(self, recipient, amount):
        if (self.account.balance - amount) <= 0:
            return "Not Enough!"
        else:
            self.account.balance -= amount
            recipient.account.balance += amount
            self.account.history["Transfer"] = f"-{amount}"
            recipient.account.history["Transfer"] = f"+{amount}"
            return "Transferred Successfully!"


account1 = Account("000001", 1000)
account2 = Account("000002", 1000)
customer1 = Customer("Emad", "123123123", account1)
customer2 = Customer("Ray", "456456456", account2)




# #class Movie and Library:
#
# class Movie:
#     def __init__(self, name, director, year, rate):
#         self.name = name
#         self.director = director
#         self.year = year
#         self.rate = rate
#     def __repr__(self):
#         return (f"Movie Name: {self.name}, Director: {self.director}, Year: {self.year}, Rate: {self.rate}")
#
#     def update_rate(self, rate):
#         if 0<=rate<=10:
#             self.rate = rate
#         else:
#             return "Wrong rate!"
#
#
# class Library:
#     def __init__(self, owner_name):
#         self.owner_name = owner_name
#         self.movies = []
#     def __repr__(self):
#         return (f"Library Information\n- Owner Name: {self.owner_name}\n- Movies: {self.movies}")
#
#     def add_movie(self, movie):
#         self.movies.append(movie)
#     def remove_movie(self, movie):
#         self.movies.remove(movie)
#
#     def highest_rate(self):
#         x = 0
#         y = ""
#         for movie in self.movies:
#             if movie.rate > x :
#                 x = movie.rate
#                 y = movie.name
#         return y, x
#
#     def director_movies(self, director_name):
#         list_movies = []
#         for movie in self.movies:
#             if movie.director == director_name:
#                 list_movies.append(movie.name)
#         return list_movies
#
#
# movie1 = Movie("Marinaka", "Jack Smith", 2014, 4)
# movie2 = Movie("Jokara", "Alba Saka", 2019, 6)
# movie3 = Movie("The Sum", "Dorin Akko", 2012, 8)
# movie4 = Movie("The Minus", "Dorin Akko", 2001, 7)
# movie5 = Movie("The Mult", "Dorin Akko", 2009, 8)
# movie6 = Movie("Engineers", "Jordan Morlo", 2003, 7)