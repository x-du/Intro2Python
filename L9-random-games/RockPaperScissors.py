import random

choices = ["rock", "paper", "scissors"]
player = input("Do you want to be rock, paper, or scissors (or quit)?")
computer = random.choice(choices)

while player!="quit":
    player = player.lower()
    print("Your choice is", player)
    print("Computer's choice is", computer)
    if player == computer:
        print("It is a tie!")
    else:
        if player == "rock":
            if computer == "paper":
                print("Computer wins!")
            else:
                print("You win!")
        elif player == "paper":
            if computer == "scissors":
                print("Computer wins!")
            else:
                print("You win!")
        elif player == "scissors":
            if computer == "rock":
                print("Computer wins!")
            else:
                print("You win!")
        else:
            print("Wrong input! Try again! ")
    player = input("Do you want to be rock, paper, or scissors (or quit)?")
    computer = random.choice(choices)
