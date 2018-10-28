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
	sorted_team = sorted(team.items(), key=lambda kv: kv[1])
	for player, jersey in sorted_team:
		print("Player Name: %s, Jersey Number: %d" % (player, jersey))


# Prompts the user for player name and number to add to a team
def add_player(team):
	player_name = input("Name of player you would like to add: ")
	player_number = int(input("Enter jersey number for %s: " % player_name))
	team[player_name] = player_number
	return team


# Removes player from a team
def remove_player(team):
	player_name = input("Name of player you would like to remove: ")
	del team[player_name]
	return team


# Prints the number of players on a team
def number_on_team(team):
	return len(team)
