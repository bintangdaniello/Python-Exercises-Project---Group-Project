import random

def hangman():
    words = ["python", "tiger", "apple", "house", "puzzle"]
    secret_word = random.choice(words)
    guessed = ["_"] * len(secret_word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

        print(" ".join(guessed))

    if "_" not in guessed:
        print("Congratulations! You guessed the word!")
    else:
        print(f"Out of attempts! The word was '{secret_word}'.")

hangman()