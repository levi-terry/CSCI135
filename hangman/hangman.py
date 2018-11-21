import random
from hangman_drawing import draw_display, replace_letter

player_continue = "y"
word_list = ["longing", "rusted", "furnace", "daybreak", "seventeen", "benign", "nine", "homecoming", "one",
             "freight car"]

while player_continue != "n":
    # Display welcome message to player, repeats with every new game
    print("*" * 23)
    print("* Welcome to Hangman! *")
    print("*" * 23)
    # Pick random word from list, save that string as a list
    word = list(random.choice(word_list))
    # display word, for testing // remove later
    print(word)
    # Initialize player guesses, display word, missed letters
    player_guesses = 0
    display_word = list("-" * len(word))
    missed_letters = []

    while player_guesses != 6:
        if display_word == word:
            break
        player_choice = input("Please guess a letter: ")
        # Loop to not allow repeat guesses of same letter
        while player_choice in missed_letters or player_choice in display_word:
            print("You have already guessed the letter '%c'." % player_choice)
            player_choice = input("Please guess another letter: ")
        for letter in word:
            if player_choice in word:
                display_word = replace_letter(word, display_word, player_choice)
                draw_display(player_guesses=player_guesses, missed_letters=missed_letters,
                             display_word=display_word)
                break
            else:
                missed_letters += player_choice
                player_guesses += 1
                draw_display(player_guesses=player_guesses, missed_letters=missed_letters,
                             display_word=display_word)
                break

    if display_word == word:
        print("You win!")
    if player_guesses == 6:
        print("You lose.")

    player_continue = input("Play again? (n to quit)\n")
