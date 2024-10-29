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









# class Song:
#     def __init__(self, name, artist, length):
#         self.name = name
#         self.artist = artist
#         self.length = length
#     def __repr__(self):
#         return f"Song Name: {self.name}, Artist: {self.artist}, Length: {self.length}"
#
# class Playlist:
#     def __init__(self, name):
#         self.name = name
#         self.songs = []
#     def __repr__(self):
#         songnames = []
#         for song in self.songs:
#             songnames.append(song.name)
#         return f"Playlist Name: {self.name}, Songs: {songnames}"
#
#     def add_song(self, song):
#         if song in self.songs:
#             return f"{song.name} is already in {self.name}"
#         else:
#             self.songs.append(song)
#     def remove_song(self, song):
#         if song not in self.songs:
#             return f"{song.name} Doesn't exist in {self.name}"
#         else:
#             self.songs.remove(song)
#
#     def check_playlist_time(self):
#         minutes = 0
#         for song in self.songs:
#             minutes += song.length
#         return f"Playlist's length is {minutes}"
#
#     def check_artist_songs(self, artist):
#         artistsongs = []
#         for song in self.songs:
#             if song.artist != artist:
#                 continue
#             else:
#                 artistsongs.append(song.name)
#         if artistsongs == []:
#             return f"{artist} has no songs in {self.name}"
#         else:
#             return artistsongs
#
#     def check_artist_time(self, artist, minutes):
#         return minutes < sum(song.length for song in self.songs if song.artist == artist)








# class Product:
#     def __init__(self, id, name, price):
#         self.id = id
#         self.name = name
#         self.price = price
#     def __repr__(self):
#         return f"{self.id} {self.name} {self.price}"
#
#
# class Warehouse:
#     def __init__(self, owner):
#         self.owner = owner
#         self.stock = {}
#     def __repr__(self):
#         return f"{self.owner}'s\nStock: {self.stock}"
#
#     def add_product(self, product, count):
#         if product in self.stock:
#             self.stock[product] += count
#         else:
#             self.stock[product] = count
#
#     def check_availability(self, product_id):
#         for product, count in self.stock.items():
#             if product.id == product_id:
#                 return count
#         return f"Product Doesn't Exists in {self.owner}'s Warehouse"
#
#     def buy_product(self, id, howmany, money):
#         for product, count in self.stock.items():
#             if product.id == id:
#                 if howmany > count:
#                     return "We don't have this amount"
#                 elif money < (product.price * howmany):
#                     return "You don't have enough money"
#                 else:
#                     self.stock[product] -= howmany
#                     return f"Purchase success!, Odef: {money -(product.price * howmany)}"
#
#
# product1 = Product("0001", "Motor", 20)
# product2 = Product("0002", "Kola", 9000)
# product3 = Product("0003", "Sababa", 5644)
# product4 = Product("0004", "Phone", 315)
# product5 = Product("0005", "Bag", 100)
# product6 = Product("0006", "Arch", 50)
#
# warehouse1 = Warehouse("Jobaara")
#
# warehouse1.add_product(product1, 10)
# warehouse1.add_product(product2, 2)
# warehouse1.add_product(product3, 15)
# warehouse1.add_product(product4, 1)
# warehouse1.add_product(product5, 9)
# warehouse1.add_product(product6, 6)
#
#
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))
# print(warehouse1.buy_product("0005", 1, 100))









# class Order:
#     def __init__(self, id, name, amount, single_price, status):
#         self.id = id
#         self.name = name
#         self.amount = amount
#         self.single_price = single_price
#         self.status = status
#         self.final_price = single_price * amount
#
#     def __repr__(self):
#         return f"{self.id} {self.name} {self.amount} {self.single_price} {self.status}"
#
# class Resturant:
#     def __init__(self, name):
#         self.name = name
#         self.list_orders = []
#     def __repr__(self):
#         return f"{self.name} {self.list_orders}"
#
#     def new_order(self,order):
#         if order in self.list_orders:
#             return "Order already exists"
#         else:
#             self.list_orders.append(order)
#
#     def update_order_status(self, order_id, new_status):
#         for order in self.list_orders:
#             if order.id == order_id:
#                 order.status = new_status
#         else:
#             return "Order doesn't Exist"
#
#     def check_orders_with_status(self, status):
#         list_orders = []
#         for order in self.list_orders:
#             if order.status == status:
#                 list_orders.append(order.id)
#         return list_orders
#
#     def discount(self, name, discount):
#         for order in self.list_orders:
#             if order.name == name:
#                 discount_amount = order.single_price * discount/100
#                 order.single_price -= discount_amount
#
#     def profit(self):
#         sum = 0
#         for order in self.list_orders:
#             sum += order.final_price
#         return sum
#
# order1 = Order("0001", "Fish", 2, 50, "Not Ready")
# order2 = Order("0002", "Meat", 1, 100, "Not Ready")
# order3 = Order("0003", "Salad", 3, 20, "Not Ready")
# order4 = Order("0004", "Water", 3, 10, "Not Ready")
#
# resturant1 = Resturant("Mamamia")
#
# resturant1.new_order(order1)
# resturant1.new_order(order2)
# resturant1.new_order(order3)
# resturant1.new_order(order4)
#
# print(resturant1)
#
# resturant1.update_order_status("0003", "Ready")
# resturant1.update_order_status("0001", "Ready")
#
# print(resturant1)
#
# print(resturant1.check_orders_with_status("Ready"))
#
# resturant1.discount("Meat", 20)
#
# print(resturant1)
#
# print(resturant1.profit())
