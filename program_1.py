# Author: Joseph Kracht
# Last Modified: 10/3/2025
# Title: Random Dice

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.

import  random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    # Sum 2 numbers
    dice_sum = die_1 + die_2

    # return sum to calling function
    return dice_sum

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
sum_of_dice_rolls = 0
for i in range(100):
    sum_of_dice_rolls += randDice()

# Average rolls
average_roll = sum_of_dice_rolls / 100

print("The average dice roll is", format(average_roll, '.2f'))
