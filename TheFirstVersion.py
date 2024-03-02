import random
def checking():
    flag = 0
    while flag == 0:
        PlayerInput = input("Enter a number from 1 to 3: ")
        if PlayerInput == '1' or PlayerInput == '2' or PlayerInput == '3':
            flag = 1
    return PlayerInput
def opportunities(inp):
    if inp == 1:
        s = 'the rock'
    elif inp == 2:
        s = 'the scissors'
    else:
        s = 'the paper'
    return s
def game(player_1, player_2):
    if player_1 == 1 and player_2 == 3:
        print("The computer won!")
    elif player_1 == 2 and player_2 == 1:
        print("The computer won!")
    elif player_1 == 3 and player_2 == 2:
        print("The computer won!")
    elif player_1 == player_2:
        print("Draw")
    else:
        print("You won!")
PlayerInput = int(checking())
PcInput = random.randint(1, 3)
print("You chose", opportunities(PcInput))
print("The computer has chosen", opportunities(PlayerInput))
game(PlayerInput, PcInput)