import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number = random.randint(1, 50)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {number}.")
            print(f"You guessed it in {attempts} attempts.")
            break

number_guessing_game()
