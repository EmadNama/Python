class Character:
    def __init__(self, name, hp, defense, attack):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.attack = attack
    def __repr__(self):
        return f"{self.name} {self.hp} {self.defense} {self.attack}"

    def IsAlive(self):
        return True if self.hp > 0 else False

    def Attack(self, character):
        character.defense -= self.attack
        if character.defense < 0:
            character.hp -= (character.defense*-1)
            character.defense = 0


class Warrior(Character):
    def __init__(self, name, hp, defense, attack, sheild):
        super().__init__(name, hp, defense, attack)
        self.sheild = sheild
    def __repr__(self):
        return (f"Warrior Information:"
                f"\n Name: {self.name}"
                f"\n HP: {self.hp}"
                f"\n Defense: {self.defense}"
                f"\n Attack: {self.attack}"
                f"\n Sheild: {self.sheild}")

class Mage(Character):
    def __init__(self, name, hp, defense, attack, magic_power):
        super().__init__(name, hp, defense, attack)
        self.magic_power = magic_power
    def __repr__(self):
        return (f"Warrior Information:"
                f"\n Name: {self.name}"
                f"\n HP: {self.hp}"
                f"\n Defense: {self.defense}"
                f"\n Attack: {self.attack}"
                f"\n Magic Power: {self.magic_power}")
class Game:
    def __init__(self, name, list_characters):
        self.name = name
        self.list_characters = list_characters


warrior1 = Warrior("Emad", 100, 100, 10, 100)
mage1 = Mage("David", 100, 100, 10, 100)

print(warrior1)
print("")
print(mage1)
print("")
warrior1.Attack(mage1)
print(warrior1)
print("")
print(mage1)
print("")

