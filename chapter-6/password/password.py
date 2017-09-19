
def is_valid_password(password):
	return len(password) >= 8 and password.isalnum()

while True:
	print('Select a new password (minimum of 8 characters; letters and numbers only)')
	password = raw_input()

	if (is_valid_password(password)):
		break
	print('Passwords must be at least 8 characters, and must consist of only letters and numbers.')

print('Your password has been set.')