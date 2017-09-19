
all_guests = {
	'Alice': {'apples': 5, 'pretzels': 12},
	'Bob': {'ham sandwiches': 3, 'oranges': 2, 'apples': 1},
	'Carol': {'cups': 3, 'apple pies': 1}
}

items = ['apples', 'pretzels', 'ham sandwiches', 'oranges', 'cups', 'apple pies']

def total_brought(guests, item):
	num_brought = 0

	for k, v in guests.items():
		num_brought = num_brought + v.get(item, 0)
	return num_brought

print('Items brought:')
for item in items:
	print(' - ' + item.lower() + ': ' + str(total_brought(all_guests, item)))