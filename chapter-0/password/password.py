
password_file = open('./password.txt')
secret_password = password_file.read()

print('Enter your password:')
typed_password = raw_input()

if typed_password == secret_password:
	print('Access granted.')
else:
	print('Access denied.')