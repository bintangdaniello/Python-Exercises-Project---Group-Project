# DICE ROLLING SIMULATOR

import random

# Function to generate a random dice number
def random_numbers():
    generated_numbers = random.randint(1, 6)
    return generated_numbers

# Main function to run the dice simulator
def main():
    # Print the first dice roll
    print("The result of the dice roll is:", random_numbers())

    # Ask the user if they want to roll again
    user_input = input("Do you want to roll the dice again? (Y/N): ")

    # Keep rolling as long as the user does not enter 'N'
    while user_input.upper() != "N":
        print("The result of the dice roll is:", random_numbers())
        user_input = input("Do you want to roll the dice again? (Y/N): ")

    # Keep rolling as long as the user does not enter 'N'
    print("Thanks for playing!")
main()