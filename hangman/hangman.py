import random
from hangman_drawing import display

player_continue = "y"
word_list = ["longing", "rusted", "furnace", "daybreak", "seventeen", "benign", "nine", "homecoming", "one",
             "freight car"]
player_guesses = 0
print(display[0])

while player_continue != "n":
    word = random.choice(word_list)
    print(word)
    player_guesses = len(word)
    display_word = "*" * len(word)
    missed_letters = []
    print(display_word)

    while player_guesses > 0:
        player_choice = input("Please guess a letter: ")
        for letter in word:
            if player_choice in word:
                print(letter)
                break
            else:
                missed_letters.append(player_choice)
                print("Missed Letters:\n", missed_letters)
                player_guesses -= 1

    player_continue = input("Play again? (n to stop)\n")
