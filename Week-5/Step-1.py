# 1.1
mixed_tuple = ("Alice", 21, True, 1.75)
print(mixed_tuple[0], "is", mixed_tuple[1], "years old.")

# 1.2
numbers = (12, 24, 36)
first, second, last = numbers
print(last)

# 1.3
numbers = (1, 2)
texts = ("hello", "world")
combined = numbers + texts
print(combined)

# 1.4
numbers = (3, 7, 10)
for number in numbers:
	print(number * 2)

# 1.5
def get_words():
	return ("learn", "practice", "improve")


first, second, third = get_words()
print(first)
print(second)
print(third)

# 1.6a
def rectangle_dimensions():
	return (8, 5)


width, height = rectangle_dimensions()
print("Area:", width * height)

# 1.6b
colors = ("red", "green", "blue")
print("blue" in colors)
