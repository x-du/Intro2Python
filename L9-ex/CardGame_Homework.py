import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
faces = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#start points for players
player1_point = 0
player2_point = 0

#play 5 rounds
for i in range(5):
    print("Round ", i+1, "...")
    #player 1 picks a card
    face = random.choice(faces)
    face_value = faces.index(face) +1
    suit = random.choice(suits)

    print("Player", 1, "has the", face, "of", suit)
    if suit=="Diamonds" or suit == "Hearts":
        player1_point += 1
    else:
        if face_value > 9:
            player2_point+= 1
        else:
            player1_point += face_value

    print("Player 1's point:", player1_point)
    print("Player 2's point:", player2_point)

    input("[Enter] to Continue?")
    #player 2 picks a card
    face = random.choice(faces)
    face_value = faces.index(face) +1
    suit = random.choice(suits)

    print("Player", 2, "has the", face, "of", suit)
    if suit=="Diamonds" or suit == "Hearts":
        player2_point += 1
    else:
        if face_value > 9:
            player1_point+= 1
        else:
            player2_point += face_value

    print("Player 1's point:", player1_point)
    print("Player 2's point:", player2_point)

    input("[Enter] to Continue?")

#after 5 rounds, decide who wins.
if player1_point > player2_point:
    print("Player 1 wins!")
elif player1_point == player2_point:
    print("It's a tie!")
else:
    print("Player 2 wins!")
