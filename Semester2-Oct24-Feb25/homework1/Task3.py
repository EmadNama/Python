import random


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
            character.hp -= (character.defense * -1)
            if character.hp < 0:
                character.hp = 0
            character.defense = 0


class Warrior(Character):
    def __init__(self, name, hp, defense, attack):
        super().__init__(name, hp, defense, attack)
    def __repr__(self):
        return (f"Warrior Information:"
                f"\n Name: {self.name}"
                f"\n HP: {self.hp}"
                f"\n Defense: {self.defense}"
                f"\n Attack: {self.attack}")

    def SpecialMove(self, character):
        if self.hp <= 10:
             return False
        else:
            self.defense -= 10
            if self.defense < 0:
                self.hp -= (self.defense * -1)
                self.defense = 0
            self.Attack(character)
            self.Attack(character)


class Mage(Character):
    def __init__(self, name, hp, defense, attack):
        super().__init__(name, hp, defense, attack)
    def __repr__(self):
        return (f"Mage Information:"
                f"\n Name: {self.name}"
                f"\n HP: {self.hp}"
                f"\n Defense: {self.defense}"
                f"\n Attack: {self.attack}")

    def SpecialMove(self, character):
        self.hp += 10
        if self.hp > 100:
            self.defense += self.hp - 100
            self.hp = 100
            if self.defense > 100:
                self.defense = 100
        sCharacter = Character("temp", 0, 0, 5)
        sCharacter.Attack(character)



class Game:
    def __init__(self, name):
        self.name = name
        self.list_players = []

    def AddPlayer(self, player):
        if player not in self.list_players:
            self.list_players.append(player)
        else:
            return ("Player Already Exists!")

    def RemovePlayer(self, player):
        if player not in self.list_players:
            return ("Player Doesn't Exist!")
        else:
            self.list_players.remove(player)
            return f"{player.name} Successfully removed from {self.name}"

    def Battle(self, player1, player2):
        if player1 not in self.list_players or player2 not in self.list_players:
            return "Players Missing"
        else:

            print(f"\nWelcome to the Battle Field!\n"
                  f"Player 1: {player1.name}\n"
                  f"- Attack Power: {player1.attack}\n"
                  f"Player 2: {player2.name}"
                  f"\n- Attack Power: {player2.attack}\n")

            while True:
                if player1.hp <= 0:
                    print(f"Player 1 {player1.name} Died")
                    break
                if player2.hp <= 0:
                    print(f"Player 2 {player2.name} Died")
                    break
                turn = random.randint(0,3)
                if turn == 0:
                    player1.Attack(player2)
                    print(f"{player1.name} Attacked {player2.name}\n{player1.name} ({player1.hp}/{player1.defense})\n{player2.name} ({player2.hp}/{player2.defense})")
                    print("")
                if turn == 1:
                    player2.Attack(player1)
                    print(f"{player2.name} Attacked {player1.name}\n{player1.name} ({player1.hp}/{player1.defense})\n{player2.name} ({player2.hp}/{player2.defense})")
                    print("")
                if turn == 2:
                    if isinstance(player1, Warrior):
                        if player1.SpecialMove(player2) == False:
                            print(f"{player1.name} Special Move Failed - {player1.name} would die!")
                            print("")
                        else:
                            print(f"{player1.name} Performed A Special Move on {player2.name}\n{player1.name} ({player1.hp}/{player1.defense})\n{player2.name} ({player2.hp}/{player2.defense})")
                            print("")
                if turn == 3:
                    player2.SpecialMove(player1)
                    print(f"{player2.name} Performed A Special Move on {player1.name}\n{player1.name} ({player1.hp}/{player1.defense})\n{player2.name} ({player2.hp}/{player2.defense})")
                    print("")





warrior1 = Warrior("Warrior", 100, 100, 10)
mage1 = Mage("Mage", 100, 100, 10)

game1 = Game("Game")

game1.AddPlayer(warrior1)
game1.AddPlayer(mage1)

game1.Battle(warrior1,mage1)

print("Hello World! That's A new text from vs 2022")