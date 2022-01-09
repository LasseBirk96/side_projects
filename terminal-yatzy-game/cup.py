import random


amount_of_dice_available = 6
picked_dice = []

def roll_dice(dice_amount):
    roll = []
    while len(roll) < dice_amount:
        roll.append(random.randint(1,6))
    print(roll)
    return roll

def get_user_input():
    user_input = input('Enter the indices of dice you want to keep, seperated by spaces\n')
    return user_input

def make_user_input_int(user_input):
    user_input_as_int = []
    for element in user_input:
        user_input_as_int.append(int(element))
    return user_input_as_int

def pick_dice_from_roll(roll):
    try: 
        user_input = get_user_input().split()
        picks = make_user_input_int(user_input) 
        for element in picks:
            picked_dice.append(roll[element])
        return picked_dice
    except IndexError:
        return print("You picked a number out of range")
        
def adjust_amount_of_dice(amount_of_dice_available, picked_dice):
    amount_of_dice_available = amount_of_dice_available - len(picked_dice)
    return amount_of_dice_available


