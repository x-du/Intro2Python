import random
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

my_face = random.choice(faces)
my_suit = random.choice(suits)

print("You have the ", my_face, "of", my_suit)
