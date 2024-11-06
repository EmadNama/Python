# 04/11/2024, Semester B Homework 1 Task 1


class Product:

    def __init__(self, id, name, department, price):
        self.id = id
        self.name = name
        self.department = department
        self.price = price
    def __repr__(self):
        return f"{self.id} {self.name} {self.department} {self.price}"

    def GetPrice(self):
        return f"{self.name}'s Price is {self.price}"


class DiscountProduct(Product):

    def __init__(self, id, name, department, price, percentage):
        super().__init__(id, name, department, price)
        self.percentage = percentage
        self.discounted_price = self.price - (self.price*self.percentage/100)
    def __repr__(self):
        return f"{self.id} {self.name} {self.department} {self.price}"

    def GetPrice(self):
        return f"{self.name}'s Original Price is {self.price}\n   - And now has {self.percentage}% Off!\n   - Price after discount: {(self.price) - self.price*self.percentage/100}"


class Store:

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.products = []
    def __repr__(self):
        return f"Store name: {self.name}\nStore Owner: {self.owner}\nStore Products: {[(i[0].name, i[1]) for i in self.products]}"

    def AddProduct(self, product, count):
        for i in self.products:
            if i[0].name == product.name:
                temp = (i[0], i[1] + count)
                self.products.remove(i)
                self.products.append(temp)
                return f"Action: Adding MORE {count} {product.name} to {self.name}'s Stock\nUpdated Stock: {self.products}\n"
        self.products.append((product, count))
        return f"Action: Adding NEW {count} {product.name} to {self.name}'s Stock\nUpdated Stock: {self.products}\n"

    def TotalValue(self):
        sum = 0
        for product, count in self.products:
            sum += product.price * count
        return f"{self.name} has products worth {sum}₪\n"

    def GetDiscountProduct(self):
        list = []
        for product, count in self.products:
            if isinstance(product, DiscountProduct):
                list.append(product)
        return f"List of {self.name}'s Discounted Products:\n{tuple(list)}"

    def GetCheapestByDepartment(self, department):
        list = []
        for product, count in self.products:
            if product.department == department:
                list.append(product)
        if list == []:
            return "No Department Found!"
        cheapest_product = list[0]
        for product in list:
            if product.price < cheapest_product.price:
                cheapest_product = product
        return f"The cheapest product in {department} is {cheapest_product.name}"

    def Buy(self, id, howmany, money):
        for product in self.products:
            if product[0].id == id:
                if howmany <= product[1]:
                    if money >= (howmany * product[0].price):
                        updated_product = (product[0], product[1]-howmany)
                        if updated_product[1] == 0:
                            self.products.remove(product)
                        else:
                            self.products.remove(product)
                            self.products.append(updated_product)
                        if isinstance(product[0], DiscountProduct):
                            return f"Purchase Successfully\nOriginal Price: {product[0].price}\nPrice After {product[0].percentage}% Discount: {product[0].discounted_price}\nYou've bought {howmany} {product[0].name} for {howmany * product[0].discounted_price}\nPaid: {money}\nChange is: {money - howmany * product[0].discounted_price}"
                        return f"Purchase Successfully\nYou've Bought {howmany} {product[0].name} for {howmany*product[0].price}\nPaid: {money}\nChange is: {money-howmany*product[0].price}"
                    else: return f"Purchase Failed - Not Enough Money\nYou're Buying {howmany} {product[0].name} for {howmany*product[0].price}\nYou Only Have: {money}"
                else: return f"Purchase Failed - We don't Have {howmany} {product[0].name}\nWe Only Have: {product[1]}"
        return f"Purchase Failed - No Products Found\nWe don't have any product with the id of {id}"



product1 = Product("1111", "Corona", "Alcohol", 14)
product2 = Product("2222", "Vodka", "Alcohol", 80)
product3 = Product("3333", "Whiskey", "Alcohol", 120)

product4 = Product("4444", "Marlboro Gold", "Tobacco", 38)
product5 = Product("5555", "Time", "Tobacco", 32)
product6 = Product("6666", "Winston", "Tobacco", 34)

discountedproduct1 = DiscountProduct("7777", "Chair", "Home", 600, 20)
discountedproduct2 = DiscountProduct("8888", "Table", "Home", 1000, 50)
discountedproduct3 = DiscountProduct("9999", "Locker", "Home", 900, 30)


store1 = Store("DanaMarket", "David")


store1.AddProduct(product1, 20)
store1.AddProduct(product1, 20) #הןספת כמות למוצר

store1.AddProduct(product2, 20)
store1.AddProduct(product3, 20)
store1.AddProduct(product4, 20)
store1.AddProduct(product5, 20)
store1.AddProduct(product6, 20)

store1.AddProduct(discountedproduct1, 20)
store1.AddProduct(discountedproduct2, 20)
store1.AddProduct(discountedproduct3, 20)

print("")
print(product1.GetPrice())
print(product2.GetPrice())
print("")
print(discountedproduct1.GetPrice())
print(discountedproduct2.GetPrice())
print(discountedproduct3.GetPrice())
print("")
print(store1)
print("")
print(store1.TotalValue())
print(store1.GetDiscountProduct())
print("")
print(store1.GetCheapestByDepartment("Tobacco"))
print(store1.GetCheapestByDepartment("Home"))
print(store1.GetCheapestByDepartment("Alcohol"))
print("")
print(store1.Buy("1111", 1, 20)) #מקרה של קנייה רגילה
print("")
print(store1.Buy("7777", 1, 1000)) #מקרה של קניית מוצר בהנחה
print("")
print(store1.Buy("3333", 3, 200)) #מקרה של אי ספיקת כסף
print("")
print(store1.Buy("9999", 60, 200)) #מקרה של אי ספיקת כמות
print("")
print(store1.Buy("0000", 10, 30)) #מקרה של מוצר חסר
print("")
print(store1) #מלאי מעודכן בסוף
