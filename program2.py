# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

def guess_number():
    random_num = random.randint(0,100)
    user_num = 0
    while user_num != random_num:
        user_num = int(input('Number: '))
        number = user_num
        if number > random_num:
            print("Your number is greater than the random number")
        if number < random_num:
            print("Your number is less than the random number")
    else:
        print("Correct!")

print('Guess the random number from 0 - 100')
guess_number()