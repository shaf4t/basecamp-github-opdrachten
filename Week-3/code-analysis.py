def code_analysis():
	print("Code 1:")
	i = 7
	for number in range(1, i + i):
		print(number)

	print("Code 2:")
	i = 1
	j = 10
	for number in range(i, j):
		if number > 5:
			print(number)
		else:
			print("Hello")

	print("Code 3:")
	sentence = "I just came to say hello!"
	count = 0
	for letter in sentence:
		if letter == " ":
			count += 1
		elif letter == "a":
			count -= 1
	print(count)

	print("Code 4:")
	for index in range(len(sentence)):
		print(sentence[index])

	print("Code 5:")
	for character in sentence:
		print(character)


if __name__ == "__main__":
	code_analysis()
