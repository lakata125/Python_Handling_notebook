# Random module
#Exo1

"""

import random

num = random.randint(1, 2)

print("Welcome to the Coin Flipping Game!")
choice = input("Enter your side (heads = 1 or tails = 2): ")[0]

if num == 1 :
    if choice == "1" or choice == "h":
        print("Good Job! You won. The coin flipped head")
    else:
        print("Aw... You lost. The coin flipped tails")
else:
    if choice == "2" or choice == "t":
        print("Good Job! You won. The coin flipped tails")
    else:
        print("Aw... You lost. The coin flipped heads")
        
print("\nThanks for playing. Goodbye")

#print("num: ", num)
#print("choice: ", choice)

"""

#Exo2

"""
import random
dice = random.randint(1, 6)
choice = 0

print("Welcome to the dice game")
choice = int(input("Choose a number you want between 1 to 6 ? ")[0])

if choice == dice:
    print("Congratulation, you won the game with the number:", choice)
else:
    print("Aw... You lost the dice game with the number:", choice)
print("\nThanks to have played at this simple dice game")

"""

#OS MODULE

import os

def directories(name):
    os.system("clear")
    cwd = os.getcwd()
    print("Current Working Directory:", cwd)
    path = os.path.join(cwd, name)

    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory '%s' created" %path)
    else:
        print("Directory '%s' already exist" %path)

    os.chdir(path)
    print("Print Working Directory: ", os.getcwd())
    
    i = 0       
    while i != 2:
        i += 1
        folder = name + str(i)
        sub_dir = os.path.join(path ,folder)
        
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
            print("sub_dir '%s' created: " %sub_dir)
        else:
            print("sub_dir '%s' already exist" %sub_dir)
        
    os.chdir(cwd)
    print("Current Working Directory: ", os.getcwd())
    print("Directories in: '", path, "' :")
    print(os.listdir(path))


directories("TOTO")