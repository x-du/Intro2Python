import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

player1 = input("Player 1's name? ")
player2 = input("Player 2's name? ")
keep_going = True
while keep_going:
    player1_face = random.choice(faces)
    player1_suit = random.choice(suits)
    player2_face = random.choice(faces)
    player2_suit = random.choice(suits)

    print(player1, "has the", player1_face, "of", player1_suit)
    print(player2, "has the", player2_face, "of", player2_suit)

    if faces.index(player1_face) > faces.index(player2_face):
        print(player1, "wins!")
    elif faces.index(player2_face) > faces.index(player1_face):
        print(player2, "wins!")
    else:
        print("It is a tie!")
    answer = input("Hit [Enter] to keep going, any key to exit:")
    keep_going = answer == ""
