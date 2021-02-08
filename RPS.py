import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
meScore = 0
youScore = 0
while(1 < 2):
    print("\n")
    print("Rock, Paper, Scissors - Start")
    meInput = input("Please choose [R]ock, [P]aper, [S]cissors : ")
    if not re.match("[SsRrPp]", meInput):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue

    #GENERATE RANDOM CHOICE
    print("I choose: " + meInput)
    meChoices = ['R' , 'P', 'S']
    youChoices = random.choice(meChoices)
    print("You choose: " + youChoices)

    #LOGIC
    if youChoices == str.upper(meInput):
        print("Tie")
    elif youChoices == 'R' and meInput.upper() == 'S':
        print("You Win")
        youScore = youScore + 1
    elif youChoices == 'R' and meInput.upper() == 'P':
        print("I Win")
        meScore = meScore + 1
    elif youChoices == 'S' and meInput.upper() == 'R':
        print("I Win")
        meScore = meScore + 1
    elif youChoices == 'S' and meInput.upper() == 'P':
        print("You Win")
        youScore = youScore + 1
    elif youChoices == 'P' and meInput.upper() == 'R':
        print("You Win")
        youScore = youScore + 1
    elif youChoices == 'P' and meInput.upper() == 'S':
        print("I Win")
        meScore = meScore + 1
    print("Score : " + str(meScore) + " - " + str(youScore))
