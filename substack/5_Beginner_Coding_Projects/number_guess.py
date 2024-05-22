import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.")

guess_game()
