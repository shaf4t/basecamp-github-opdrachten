#Code 01:
words = []
num_str = input("How many words would you like to enter?")
num = int(num_str)
for _ in range(0, num):
	word = input("Next word: ")
words.append(word)
print("This is your list of words:", words)