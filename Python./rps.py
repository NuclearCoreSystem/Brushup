import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Pick either rock, paper, or scissors.")

if player == computer:
    print("Tied.")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print("Oh wow. You won.")
else:
    print("You lose, dumbass.")