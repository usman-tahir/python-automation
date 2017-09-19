
import pprint

print('Please enter a text string:')
message = raw_input()

character_count = {}

for character in message:
	character_count.setdefault(character, 0)
	character_count[character] = character_count[character] + 1

# print(character_count)
pprint.pprint(character_count)