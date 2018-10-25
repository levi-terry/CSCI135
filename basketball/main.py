import basketball

print('Create Griz roster:')
griz = basketball.create_roster()
print('\nGriz Basketball Roster:')
basketball.print_roster(griz)

print('\nCreate Bobcat roster:')
bobcats = basketball.create_roster()
print('\nBobcat Basketball Roster: ')
basketball.print_roster(bobcats)

print("\nAdd player to Griz roster:")
basketball.add_player(griz)
basketball.add_player(griz)

print("\nAdd player to Bobcat roster:")
basketball.add_player(bobcats)
basketball.add_player(bobcats)

print('\nGriz Basketball Roster:')
basketball.print_roster(griz)
print('\nBobcat Basketball Roster: ')
basketball.print_roster(bobcats)

print("\nRemove player from Griz roster:")
basketball.remove_player(griz)

print("\nRemove player from Bobcat roster:")
basketball.remove_player(bobcats)

print('\nGriz Basketball Roster:')
basketball.print_roster(griz)
print('\nBobcat Basketball Roster: ')
basketball.print_roster(bobcats)

print('\nNumber of players on the Griz Roster:')
print(basketball.number_on_team(griz))
print('\nNumber of players on the Bobcat Roster: ')
print(basketball.number_on_team(bobcats))