import random

number = random.randint(1,10000)
guess = None

while guess != number:
    guess = int(input("Guess between 1 and 10000."))

    if guess < number:
        print("No.")
    elif guess > number:
        print("Too high.")
    elif guess == number:
        print("Congratulations.")