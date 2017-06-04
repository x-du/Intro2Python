import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
faces = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

keep_going = True
players = [0, 0]

for i in range(10):
    print("Round ", i+1, "...")
    face = random.choice(faces)
    face_value = faces.index(face) +1
    suit = random.choice(suits)
    player = i % 2
    print("Player", player+1, "has the", face, "of", suit)
    if suit=="Diamonds" or suit == "Hearts":
        players[player] += 1
    else:
        if face_value > 9:
            players[1-player]+= 1
        else:
            players[player] += face_value

    print("Player 1's point:", players[0])
    print("Player 2's point:", players[1])

    input("[Enter] to Continue?")

if players[0] > players[1]:
    print("Player 1 wins!")
elif players[0] == players[1]:
    print("It's a tie!")
else:
    print("Player 2 wins!")
