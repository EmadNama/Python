class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name, self.age}"

class Dog(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type
    def __repr__(self):
        return f"{self.name, self.age, self.type}"

class DogShelter:

    def __init__(self, owner):
        self.owner = owner
        self.dog_list = []
    def __repr__(self):
        return f"{self.owner, self.dog_list}"

    def add_dog(self, dog):
        if dog in self.dog_list:
            return "Dog Already Exists"
        else:
            self.dog_list.append(dog)
    def remove_dog(self, dog):
        if dog not in self.dog_list:
            return "Dog Doesn't Exists"
        else:
            self.dog_list.remove(dog)

    def search_by_type(self, type):
        if type != str(type):
            return "Wrong Input!"
        dogs_by_type = []
        for dog in self.dog_list:
            if dog.type == type:
                dogs_by_type.append(f"{dog.name}, {dog.age}")
        if dogs_by_type == []:
            return "No Dogs Found"
        return dogs_by_type

    def avg_age(self):
        sum = 0
        for dog in self.dog_list:
            sum += dog.age
        return sum//len(self.dog_list)

dog1 = Dog("Michael", 3, "Zeev")
dog2 = Dog("Alaxender", 3, "Doberman")
dog3 = Dog("Tommy", 2, "Pitbull")
dog4 = Dog("Bella", 5, "Zeev")
dog5 = Dog("Tote", 4, "Zeev")
dog6 = Dog("Moak", 1, "Pitbull")
dog7= Dog("Syndrome", 6, "Doberman")

shelter1 = DogShelter("Emad")

shelter1.add_dog(dog1)
shelter1.add_dog(dog2)
shelter1.add_dog(dog3)
shelter1.add_dog(dog4)
shelter1.add_dog(dog5)
shelter1.add_dog(dog6)
shelter1.add_dog(dog7)

print(shelter1.avg_age())