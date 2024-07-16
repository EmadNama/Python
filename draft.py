# def AverageCheck(): #Checks an average for user numbers
#     CountOfNumbers = 0 #Count of input numbers
#     SumOfNumbers = 0 #Sum of all input numbers
#     while True:
#         number = input("Put a number: ")
#         if number == "q": #q is the stop key that gives the result
#             break
#         elif number.isdigit(): #checks if the input has only digits
#             number = int(number)
#             SumOfNumbers+=number
#             CountOfNumbers+=1
#         else: #output gets to here only if the input wasn't a digit
#             print("Please enter a valid number or q to quit.")
#
#     if CountOfNumbers>0: #the result to only when the count of input numbers is bigger than zero
#         Average = SumOfNumbers / CountOfNumbers
#         return Average
#     else: #only if the first input wasn't a digit so that prevents a division by zero
#         print("You did not enter any valid numbers")
#         return None
#
# result = AverageCheck()
# if result is not None: #is not None refers to line 23
#     print(f"The average is {result}") #final result


# def ListAverageCheck(x): #checks an average in a list with all types of classes
#     SumOfNumbers = 0
#     CountOfNumbers = 0
#     NonNumericItems = []
#     for i in x:
#         if isinstance(i, (int, float)):
#             SumOfNumbers+=i
#             CountOfNumbers+=1
#         elif isinstance(i, str) and i.isdigit():
#             SumOfNumbers+=int(i)
#             CountOfNumbers+=1
#         else:
#             NonNumericItems.append(i)
#     if NonNumericItems:
#          print(f"Ignored items: {NonNumericItems}")
#     if CountOfNumbers > 0:
#         average = SumOfNumbers / CountOfNumbers
#         return average
#     else:
#         return 0
#
# list1 = ["30", 10, 20, 40, "50", 60, 70, "Emad", "E17"]
# print(f"List one: {ListAverageCheck(list1)}")



# import random #sum of two dice throwing with count of throws
# def roll_dice():
#     CountOfThrows=0
#     TotalSum=0
#     while CountOfThrows<10:
#         TotalSum += random.randint(1,7) + random.randint(1,7)
#         CountOfThrows+=1
#     return TotalSum
#
# dice_result = roll_dice()
# print(dice_result)

# import random
# def roll_dice():
#     return random.randint(1,7) + random.randint(1,7)
#
# playeronechips = 20
# computerchips = 20
#
# while True:
#     t = input("Type anything to throw: ")
#     resultplayer = roll_dice()
#     computerchips -= resultplayer
#     playeronechips += resultplayer
#     print(f"You've thrown the dice and got {resultplayer}")
#     print(f"Results: Computer {computerchips}, you {playeronechips}")
#     resultcomputer = roll_dice()
#     computerchips += resultcomputer
#     playeronechips -= resultcomputer
#     print(f"Computer have thrown the dice and got {resultcomputer}")
#     print(f"Results: Computer {computerchips}, you {playeronechips}")


# import random
#
#
# def roll_dice():
#     return random.randint(1, 6) + random.randint(1, 6)  # Simulates rolling two six-sided dice
#
#
# player_chips = 20
# computer_chips = 20
#
# while True:
#     input("Press Enter to roll the dice: ")
#
#     # Player's turn
#     player_result = roll_dice()
#     player_chips += player_result
#     computer_chips -= player_result
#     print(f"You rolled the dice and got: {player_result}")
#     print(f"Chips: Computer {computer_chips}, Player {player_chips}\n")
#
#     # Check if player has lost all chips
#     if player_chips <= 0:
#         print("You have no more chips. Game over!")
#         break
#
#     # Computer's turn
#     computer_result = roll_dice()
#     computer_chips += computer_result
#     player_chips -= computer_result
#     print(f"Computer rolled the dice and got: {computer_result}")
#     print(f"Chips: Computer {computer_chips}, Player {player_chips}\n")
#
#     # Check if computer has lost all chips
#     if computer_chips <= 0:
#         print("Computer has no more chips. You win!")
#         break

import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("")

        # Entry widget to display and input numbers
        self.entry = tk.Entry(root, width=20, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for numbers and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, text):
        current = self.entry.get()

        if text == '=':
            try:
                result = eval(current)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", f"Invalid Input: {str(e)}")
        else:
            self.entry.insert(tk.END, text)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
