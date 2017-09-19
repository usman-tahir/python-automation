
birthdays = {
	'Alice': 'Apr 1',
	'Bob': 'Dec 12',
	'Carol': 'Mar 4'
}

while True:
	print('Enter a name (blank to quit):')
	name = raw_input()

	if name == '':
		print('Goodbye!')
		break

	if name in birthdays:
		print(birthdays[name] + ' is ' + name + '\'s birthday')
	else:
		print('I do not have birthday information for ' + name + '.')
		print('What is their birthday?')
		birthday = raw_input()

		birthdays[name] = birthday
		print('Birthday database updated.')