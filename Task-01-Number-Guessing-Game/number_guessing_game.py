import random


def play_game():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 8

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")

    if attempts >= max_attempts and guess != secret_number:
        print(f"Game over! The correct number was {secret_number}.")


if __name__ == "__main__":
    play_game()
