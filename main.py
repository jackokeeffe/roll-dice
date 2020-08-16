import random
import time

def roll_dice():
    global dice_1
    print('Rolling dice...')
    time.sleep(1)
    dice_1 = random.choice(range(1,6))
    output()

def output():
    print('Your dice rolled ' + str(dice_1) + '!')
    play_again()

def play_again():
    again = input('Play again? (y/n): ')
    if again == 'y':
        roll_dice()
    elif again == 'n':
        exit()
    else:
        print('Please provide a valid input! y = Yes, n = No.')
        play_again()

roll_dice()
