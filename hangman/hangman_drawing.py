# Created this file to make the main code cleaner since this mostly consists of the display of the hangman

display = ['''
     ______
     |    |
          |
          |
          |
          |
     _____|''',
           '''
     ______
     |    |
     0    |
          |
          |
          |
     _____|
           ''',
           '''
     ______
     |    |
     0    |
     |    |
          |
          |
     _____|
           ''',
           '''
     ______
     |    |
     0    |
     |    |
    /     |
          |
     _____|
           ''',
           '''
     ______
     |    |
     0    |
     |    |
    / \   |
          |
     _____|
           ''',
           '''
     ______
     |    |
     0    |
    /|    |
    / \   |
          |
     _____|
           ''',
           '''
     ______
     |    |
     0    |
    /|\   |
    / \   |
          |
     _____|
           ''']


def draw_display(player_guesses, display_word, missed_letters):
    print(display[player_guesses])
    print("Word: ", end='')
    for letter in display_word:
        print(letter, end='')
    print("\nMissed Letters: ")
    for letter in missed_letters:
        print(letter, end=' ')
    print()


def replace_letter(word, display_word, player_guess):
    for position, char_a in enumerate(word):
        if player_guess == char_a:
            display_word[position] = char_a
    return display_word
