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


def draw_display(player_guesses, missed_letters, correct_letters):
    print(display[player_guesses])
    print("Missed Letters: ")
    for letter in missed_letters:
        print(letter, end=' ')
    print("\nGuesses Left: %d" % player_guesses)
