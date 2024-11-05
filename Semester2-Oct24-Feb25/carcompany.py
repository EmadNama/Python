class Car:
    def __init__(self, maxpass, carnum, cost):
        self.maxpass = maxpass
        self.carnum = carnum
        self.cost = cost

    def __repr__(self):
        return (f"Car Information:"
                f"\n Max Passengers: {self.maxpass}"
                f"\n Car Number: {self.carnum}"
                f"\n Rent Cost Per Day: {self.cost}")

class SportCar(Car):
    def __init__(self, maxpass, carnum, cost, sunroof, mode):
        super().__init__(maxpass, carnum, cost)
        self.sunroof = sunroof
        self.mode = mode

    def __repr__(self):
        return (f"Sport Car Information:"
                f"\n Max Passengers: {self.maxpass}"
                f"\n Car Number: {self.carnum}"
                f"\n Rent Cost Per Day: {self.cost}"
                f"\n Motor Status: {self.mode}")

    def Tuning(self, mode):
        self.mode = mode

car1 = Car(4, "1245", 500)


sportcar1 = SportCar(2, "1234", 2000, False, "Normal")
sportcar2 = SportCar(2, "1234", 2000, True, "Sport")
sportcar3 = SportCar(2, "1234", 2000, True, "Normal")
sportcar4 = SportCar(2, "1234", 2000, False, "Comfort")
sportcar5 = SportCar(2, "1234", 2000, True, "Comfort")
sportcar6 = SportCar(2, "1234", 2000, False, "Sport")

list_sport_cars = [sportcar1, sportcar2, sportcar2, sportcar3, sportcar4, sportcar5]
for car in list_sport_cars:
    car.Tuning("Sport")
list_car_modes = [i.mode for i in list_sport_cars]

print("")
print(sportcar1)
print("")
print(car1)
print("")
print(list_car_modes)