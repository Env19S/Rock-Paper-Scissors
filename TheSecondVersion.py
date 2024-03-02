import random
def game(player_1, player_2):
    if (player_1 == 1 and player_2 == 3):
        print("The computer won!")
    elif (player_1 == 2 and player_2 == 1):
        print("The computer won!")
    elif (player_1 == 3 and player_2 == 2):
        print("The computer won!")
    elif (player_1 == player_2):
        print("Draw!")
    else: print("You won!")
def cheсking(k):
    flag = 0
    if k == 1:
        while (flag == 0):
            PlayerInput = input("Enter a number from 1 to 3: ")
            if (PlayerInput == '1' or PlayerInput == '2' or PlayerInput == '3'):
                flag = 1
    else:
        while (flag == 0):
            PlayerInput = input("Enter 1 to continue, 0 to exit: ")
            if (PlayerInput == '1' or PlayerInput == '0'):
                flag = 1
    return PlayerInput
def opportunities(inp):
    if inp == 1: s = 'the rock'
    elif inp == 2: s = 'the scissors'
    else: s = 'the paper'
    return s
flag = 1
while (flag == 1):
    PlayerInput = int(cheсking(1))
    PcInput = random.randint(1, 3)
    print("The computer has chosen", opportunities(PcInput))
    game(PlayerInput, PcInput)
    flag = int(cheсking(2))
