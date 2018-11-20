import random

player_continue = "y"
word_list = ["longing", "rusted", "furnace", "daybreak", "seventeen", "benign", "nine", "homecoming", "one",
             "freight car"]
player_guesses = 0

while player_continue != "n":
    word = random.choice(word_list)
    player_guesses = len(word)
    player_choice = input("Please guess a letter")
