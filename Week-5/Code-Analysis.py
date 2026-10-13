# 4.1
a_tuple = ("Never", "gonna", "give", "you", "up")
counter = 0
for x in a_tuple:
	if x[0] == "g":
		counter = counter + 1
	else:
		counter = counter + 2
print(counter)

# 4.2
def do_something(x):
	rtuple = x,
	for i in range(2, 11):
		rtuple = rtuple + ((x * i),)
	return rtuple


print(do_something(6))

# 4.3
def print_matching_values(*args, **kwargs):
	for item in args:
		for key, value in kwargs.items():
			if item == key:
				print(value)


print_matching_values("a", "z", "d", "b", a=1, b=2, c=3, d=4)

# 4.4
def process_strings(strings):
	processed_strings = []
	for string in strings:
		processed_string = ""
		for char in reversed(string):
			processed_string += char
		processed_strings.append(processed_string)
	return processed_strings


names = ["Alice", "Bob", "Charlie", "Dave"]
for name in process_strings(names):
	print(name)
