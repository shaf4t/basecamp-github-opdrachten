def for_exercises():
	#3.1
	for number in range(1, 43):
		print(number, end=" ")
	print()

	#3.2
	for number in range(1, 101, 2):
		print(number, end=" ")
	print()

	#3.3
	text = input("Enter a text: ")
	for character in text:
		print(character)

	# extra voorbeeld
	print("Characters at odd indices:")
	for index in range(1, len(text), 2):
		print(text[index])

	#3.4
	print("A loop repeats a block of code until its sequence ends or its condition becomes false.")

	#3.5
	print("A for loop iterates over a sequence. A while loop repeats while a condition remains true.")

	#3.6
	# Hoofdstuk 6, oefening 6.1
	for value in [3, 2, 1, 0]:
		print(value)

	# Hoofdstuk 7, oefening 7.1
	for value in [3, 2, 1, 0]:
		print(value)

	# Hoofdstuk 7, oefening 7.2
	guess_me = 7
	number = 1
	while True:
		if number < guess_me:
			print("too low")
		elif number == guess_me:
			print("found it!")
			break
		else:
			print("oops")
			break
		number += 1

	# Hoofdstuk 7, oefening 7.3
	guess_me = 5
	for number in range(10):
		if number < guess_me:
			print("too low")
		elif number == guess_me:
			print("found it!")
			break
		else:
			print("oops")
			break

for_exercises()
