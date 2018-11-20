import random
import math
from hangman_drawing import draw_display

player_continue = "y"
word_list = ["longing", "rusted", "furnace", "daybreak", "seventeen", "benign", "nine", "homecoming", "one",
             "freight car"]
player_guesses = 0

while player_continue != "n":
    word = random.choice(word_list)
    print(word)
    player_guesses = math.ceil(len(word) / 2)
    display_word = "*" * len(word)
    missed_letters = ''
    correct_letters = ''
    print(display_word)

    while player_guesses != 6:
        player_choice = input("Please guess a letter: ")
        for letter in word:
            if player_choice in word:
                correct_letters += player_choice
                draw_display(player_guesses=player_guesses, missed_letters=missed_letters,
                             correct_letters=correct_letters)
                break
            else:
                missed_letters += player_choice
                player_guesses += 1
                draw_display(player_guesses=player_guesses, missed_letters=missed_letters,
                             correct_letters=correct_letters)
                break

    if player_guesses == 0:
        print("You lose.")

    player_continue = input("Play again? (n to quit)\n")
