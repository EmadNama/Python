'''string=input("Put a string: ")
reversed=""
for i in string:
    reversed=i+reversed
print(reversed)'''
import random

'''l=[]
s='a'
while s<='z':
    l.append([s, 0])
    s=chr(ord(s)+1)
string=input("Put a string: ")
for char in string:
    for histo in l:
        if char==histo[0]:
            histo[1]+=1
print(l)'''

'''import random

result=[["You", 0], ["Computer", 0]]
options=["rock", "paper", "scissors"]
computer = random.choice(options)

rounds=int(input("How many rounds do you want to play?: "))
option=input(f"Choose {options}: ")
print(f"I choose {computer}")
if option=="rock" and computer=="scissors":
    print("You won")
    result[0][1]+=1
if option=="rock" and computer=="paper":
    print("You lost")
    result[1][1]+=1
if option=="rock" and computer=="rock":
    print("tie")
    result[0][1] += 1
    result[1][1] += 1

if option=="paper" and computer=="scissors":
    print("You lost")
    result[1][1]+=1
if option=="paper" and computer=="rock":
    print("You won")
    result[0][1]+=1
if option=="paper" and computer=="paper":
    print("tie")
    result[0][1] += 1
    result[1][1] += 1

if option=="scissors" and computer=="rock":
    print("You lost")
    result[1][1]+=1
if option=="scissors" and computer=="paper":
    print("You won")
    result[0][1]+=1
if option=="scissors" and computer=="scissors":
    print("tie")
    result[0][1] += 1
    result[1][1] += 1

print(result)'''

'''import  random
choices = ["rock","paper","scissors"]

rounds = int(input("Welcome, how many rounds on the game?"))
computerS=0
playerS=0

for i in range(rounds):
    while True:
        playerChoice=input("Please enter your choise - rock, paper, scissors only: ")
        if playerChoice in choices:
            break
        else:
            print("Error, please choose only what i've asked!")
    computerChoise = random.choices(choices)[0]

    if playerChoice==computerChoise:
        computerS+=1
        playerS+=1
        print("computer choose {0} so it is a tie!".format(computerChoise))
    elif (playerChoice=='rock' and computerChoise=='scissors') or (playerChoice=='paper' and computerChoise=='rock') or (playerChoice=='scissors' and computerChoise=='paper'):
        playerS+=1
        print("Great, computer choose {0} so you win for now".format(computerChoise))
    else:
        computerS+=1
        print("Sorry, you lose this round because computer choose {0}".format(computerChoise))

if computerS>playerS:
    print('You lose, the computer have {0} and you have {1} score'.format(computerS,playerS))
elif computerS<playerS:
    print('You win, the computer have {0} and you have {1} score'.format(computerS, playerS))
else:
    print("It's a tie!")'''





'''sticks = 21
while True:
    userinput=int(input("Choose between 1-3: "))
    if userinput<1 or userinput>3:
        print("Error, Wrong option")
    else:
        sticks-=userinput
        print(f"Sticks = {sticks}")
        if sticks==1:
            print("You Won!")
            break
        if sticks>7:
            computerinput=random.choice([1,2,3])
            sticks-=computerinput
            print(f"Computer chose {computerinput}, Sticks = {sticks}")
        elif sticks==6:
            computerinput=1
            sticks-=computerinput
            print(f"Computer chose {computerinput}, Sticks = {sticks}")
        elif sticks==5:
            computerinput=random.choice([1,2,3])
            sticks-=computerinput
            print(f"Computer chose {computerinput}, Sticks = {sticks}")
        elif sticks==4:
            computerinput=3
            sticks-=computerinput
            print(f"Computer chose {computerinput}, Sticks = {sticks}")
            print("You lost!")
        elif sticks==3:
            computerinput=2
            sticks-=computerinput
            print(f"Computer chose {computerinput}, Sticks = {sticks}")
        elif sticks==2:
            computerinput=1
            sticks-=computerinput
            print(f"Computer chose {computerinput}, Sticks = {sticks}")'''



'''import random
print("*** Welcome to the game 21 sticks!!!***")

sticks = 21

while True:
    print("There are {0} sticks left for now".format(sticks))
    while True:
        c = int(input("Please enter how much sticks to pick up from 1 to 3: "))
        if 1<=c<=3:
            break
        else:
            print("Please pick up only from 1 to 3 sticks!!!")
    sticks-=c
    if sticks<=0:
        print("You lose!")
        break
    comC = random.randint(1,3)
    comC = min(comC,sticks)
    print("Computer choose {0} sticks to pick up".format(comC))
    sticks-=comC
    if sticks <= 0:
        print("You win!")
        break'''























