def while_exercises():
	#2.1
	number = 1
	while number <= 42:
		print(number, end=" ")
		number += 1
	print()

	#2.2
	number = 1
	while number <= 100:
		if number % 2 == 1:
			print(number, end=" ")
		number += 1
	print()

	#2.3
	number = 10
	while number >= -10:
		print(number, end=" ")
		number -= 1
	print()

	#2.4
	text = input("Enter a text: ")
	index = 0
	while index < len(text):
		print(text[index])
		index += 1

	#2.5
	index = 0
	while index < len(text):
		if text[index] in "ea":
			print(text[index])
		index += 1

	#2.6
	# Uitvoer van het eerste voorbeeld: 39, 79.
	# Uitvoer van het tweede voorbeeld: -16, -24, -32, -40, -48, -56, -64, -72.
	# Uitvoer van het derde voorbeeld: -8, -16, -24, -32, -40, -48, -56, -64.
	# Als de laatste twee regels worden verwisseld, verandert de uitvoer omdat de waarde wordt geprint voordat deze wordt verlaagd in plaats van erna.


while_exercises()
