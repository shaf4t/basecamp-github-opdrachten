def strings_exercises():
	#1.1
	text = input("Enter a text: ")
	print("Length:", len(text))

	#1.2
	print("First character replaced:", "k" + text[1:] if text else "")

	#1.3
	print("Spaces removed:", "this is a text".replace(" ", ""))

	#1.4
	print("Capitalized:", text.upper())

	#1.5
	print("Without e:", text.replace("e", ""))

	#1.6
	print("Number of i characters:", text.count("i"))

	#1.7
	first = input("Enter the first text: ")
	second = input("Enter the second text: ")
	print(f"Together: {first} {second}")


strings_exercises()
