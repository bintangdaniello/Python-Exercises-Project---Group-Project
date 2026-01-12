# Generate random number and have user guess the number
from random import randint

def random():
    number = randint(1, 26) #make the random integer (1-26)

    guess = int(input("Enter guess (1-26): ")) #get the guess from the user

    while guess != number: #while the number is not the guess
        if guess >= 27:
            print("Number is too high, the range is (1-26)")
        if guess <= 0:
            print("Number is too low, the range is (1-26)")
        elif guess > number and guess <= 26: #if its greater than and less than or equal to 27
            print("Incorrect guess.") #print incorrect
            print("Guess is too high") #print too high
        elif guess < number:
            print("Incorrect guess.") #print incorrect
            print("Guess is too low") #print too low

        guess = int(input("Enter guess (1-26): ")) #reprompt for the guess

    print("Correct guess!") #once they get the answer print correct

def main():
    random()

main()