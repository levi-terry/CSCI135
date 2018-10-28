# Prompts a user for player names and numbers, returns in a dictionary
def create_roster():
	team_roster = {}
	player_name = ""
	while player_name != "q":
		player_name = input("Enter player's name or 'q' to quit: ")
		if player_name == 'q':
			break
		player_number = int(input("Enter jersey number for %s: " % player_name))
		team_roster[player_name] = player_number
	return team_roster


# Prints the team ordered by jersey numbers low to high
def print_roster(team):
	sorted_team = team((jersey,player) for player,jersey in team.
	for player, jersey in sorted(team.items()):
		print("Player Name: %s, Jersey Number: %d" % (player, jersey))


# Prompts the user for player name and number to add to a team
def add_player(team):
    pass


# Removes player from a team
def remove_player(team):
    pass


# Prints the number of players on a team
def number_on_team(team):
    return len(team)
