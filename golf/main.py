"""
Design and implement a program to process golf scores.
The scores of four golfers are stored in a file called golf.txt
Each line represents one hole, and the file contains 18 lines.
Each line contains five values: par for the hole followed by the number of strokes each golfer used on that hole.
Store the total for par in the variable par.
Store the totals for the players in a list called players.
Determine the winner and produce a table showing how well each golfer did.
"""
with open("golf.txt") as golf_scores:
    # Variable List
    # par adds up the first column
    # players is a list that adds up each players score
    par = 0
    players = [0, 0, 0, 0]
    winner = ""
    # Read in each line from text file as a string
    for line in golf_scores.readlines():
        # Split the string by whitespace
        scores = line.split()
        par += int(scores[0])
        players[0] += int(scores[1])
        players[1] += int(scores[2])
        players[2] += int(scores[3])
        players[3] += int(scores[4])
    if players[0] == min(players):
        winner = "Player 1"
    elif players[1] == min(players):
        winner = "Player 2"
    elif players[2] == min(players):
        winner = "Player 3"
    else:
        winner = "Player 4"
    print("Par for the course: %d" % par)
    print("Player 1: %d" % players[0])
    print("Player 2: %d" % players[1])
    print("Player 3: %d" % players[2])
    print("Player 4: %d" % players[3])
    print("The winner is %s!" % winner)
