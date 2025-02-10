# Random module
#Exo1

"""

import random

num = random.randint(1, 2)

print("Welcome to the Coin Flipping Game!")
choice = int(input("Enter your side (heads = 1 or tails = 2): ")[0])

if choice == num:
    print("Good Job! You won.")
else:
    print("Aw... You lost.")
   
print("\nThanks for playing. Goodbye")



"""

#Exo2

"""

import random
dice = random.randint(1, 6)
choice = 0

print("Welcome to the dice game")
choice = int(input("\nChoose a number you want between 1 to 6 ? ")[0])

if choice == dice:
    print(f"\nCongratulation, you won the game with the number: {dice}")
else:
    print("\nAw... You lost the dice game, the dice number was:", dice)

"""


#OS MODULE

import os

def directories(name):
    os.system("clear")
    cwd = os.getcwd()
    #print("Current Working Directory:", cwd)
    path = os.path.join(cwd, name)

    if not os.path.exists(path):
        os.mkdir(path)
        print("\nDirectory created:", path)
    else:
        print("\nDirectory already existing:", path)

    os.chdir(path)
    #print("Print Working Directory: ", os.getcwd())
    hyphen = '-'
    
    i = 0       
    while i != 2:
        i += 1
        folder = name + hyphen + str(i)
        sub_dir = os.path.join(path ,folder)
        
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
            print("\nDirectory created:", sub_dir)
        else:
            print("\nDirectory already existing:", sub_dir)
        
    os.chdir(cwd)
    #print("Current Working Directory: ", os.getcwd())
    print("\nDirectories in: '", path, "' :")
    print(os.listdir(path))

directories("TOTO")

# Exo2

def remove_dir():
    answer = str(input("\nWrite the absolute path directory to remove it:\n"))
    if not os.path.exists(answer):
        print("\nDirectory not existing:", answer)
    else:
        list_dir = os.listdir(answer)
        for dir in list_dir:
            sub_dir = os.path.join(answer, dir)
            print("\nSub directory removed:", sub_dir)
            os.rmdir(sub_dir)
        print("\nParent directory removed:", answer)
        os.rmdir(answer)
        

remove_dir()