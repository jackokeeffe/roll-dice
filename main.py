import random
import time

one_dice = 0
two_dice = 0

def choose_dice():
    choice = input('Would you like to roll one dice (1) or two dice (2)? ')
    if choice == '1':
        roll_dice()
    elif choice == '2':
        roll_2dice()
    else:
        print('Please enter a valid input (1 = roll 1 dice, 2 = roll 2 dice): ')
        choose_dice()

def roll_dice():
    global one_dice, dice_1
    print('Rolling dice...')
    time.sleep(1)
    dice_1 = random.choice(range(1,6))
    one_dice +=1
    output()

def roll_2dice():
    global two_dice, dice_2, dice_3, dice_total
    print('Rolling dice...')
    two_dice += 1
    time.sleep(1)
    dice_2 = random.choice(range(1,6))
    dice_3 = random.choice(range(1,6))
    dice_total = (dice_2 + dice_3)
    output()

def output():
    if one_dice == 1:
        print('Your dice rolled ' + str(dice_1) + '!')
        roll_again()
    elif two_dice == 1:
        print('Your dice rolled ' + str(dice_2) + ' and ' + str(dice_3) + ' for a total of ' + str(dice_total) + '!')
        roll_again()

def roll_again():
    global one_dice, two_dice
    again = input('Roll again? (y/n): ')
    if again == 'y':
        if one_dice == 1:
            one_dice = 0
            roll_dice()
        elif two_dice == 1:
            two_dice = 0
            roll_2dice()
    elif again == 'n':
        exit()
    else:
        print('Please provide a valid input! y = Yes, n = No.')
        roll_again()

choose_dice()
