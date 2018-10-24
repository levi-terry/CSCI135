def get_num_of_non_WS_characters(some_string):
	character_count = 0
	for i in some_string:
		if i.isspace():
			pass
		else:
			character_count += 1
	return character_count


def get_num_of_words(some_string):
	word_count = some_string.split()
	return len(word_count)


print(get_num_of_non_WS_characters('My name is Trish Duce.'))
print(get_num_of_words('Hey buddy what do you know'))
