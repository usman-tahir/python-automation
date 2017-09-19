
def print_picnic(picnic_items, left_width, right_width):
	print('Picnic items:'.center(left_width + right_width, '-'))
	for k, v in picnic_items.items():
		print(k.ljust(left_width, '.') + str(v).rjust(right_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)