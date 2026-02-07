import random
def number_guessing_game():
    number_to_guess = random.randint(1,10)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

number_guessing_game()
