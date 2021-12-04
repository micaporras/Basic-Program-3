# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

def get_numbers(): 
    random_one = random.randint(0,9)
    random_two = random.randint(0,9)
    random_three = random.randint(0,9)
    randoms = [random_one, random_two, random_three]
    try_again = 'yes'
    while try_again[0] == 'y':
        first_num = int(input('First number: '))
        second_num = int(input('Second number: '))
        third_num = int(input('Third number: '))
        if first_num in randoms and second_num in randoms and third_num in randoms:
            print(f'The winning numbers are {randoms}')
            print('Winner')
            break 
        else:
            print('You loss')
            try_again = input('Try again? (y or n): ')
    if try_again[0] == 'n':
        print(f'The winning numbers are {randoms}')

print('Give three numbers from 0 to 9')
get_numbers()
