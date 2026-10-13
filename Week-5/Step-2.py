import random


# 2.1
scores = [72, 88, 91, 64, 79]
print("Maximum:", max(scores))
print("Minimum:", min(scores))

# 2.2
sorted_scores = sorted(scores)
print("Two smallest:", sorted_scores[:2])
print("Two largest:", sorted_scores[-2:])

# 2.3
numbers = [int(number) for number in input("Enter integers separated by spaces: ").split()]
print("Number of items:", len(numbers))
print("Last item:", numbers[-1])
print("Reverse:", numbers[::-1])
print("Contains a 5:", "Yes" if 5 in numbers else "No")
print("Number of fives:", numbers.count(5))
middle = numbers[1:-1]
middle.sort()
print("Sorted middle:", middle)
print("Less than 5:", sum(number < 5 for number in numbers))

# 2.4
random_numbers = [random.randint(1, 100) for _ in range(20)]
sorted_numbers = sorted(random_numbers)
print("Numbers:", random_numbers)
print("Average:", sum(random_numbers) / len(random_numbers))
print("Largest:", max(random_numbers))
print("Smallest:", min(random_numbers))
print("Second largest:", sorted_numbers[-2])
print("Second smallest:", sorted_numbers[1])
print("Even numbers:", sum(number % 2 == 0 for number in random_numbers))

# 2.5
numbers = [8, 9, 10]
numbers[1] = 17
numbers.extend([4, 5, 6])
numbers.pop(0)
numbers.sort()
numbers *= 2
numbers.insert(3, 25)
print(numbers)

# 2.6
zero_to_forty_nine = []
squares = []
letters = []
for number in range(50):
	zero_to_forty_nine.append(number)
for number in range(1, 51):
	squares.append(number ** 2)
for number in range(1, 27):
	letters.append(chr(96 + number) * number)
print(zero_to_forty_nine)
print(squares)
print(letters)

# 2.7
def add_lists(first_list, second_list):
	return [first + second for first, second in zip(first_list, second_list)]


print(add_lists([3, 1, 4], [1, 5, 9]))

# 2.8a
def remove_duplicates(items):
	return list(dict.fromkeys(items))


print(remove_duplicates([3, 1, 3, 2, 1, 4]))

# 2.8b
temperatures = [18, 21, 19, 24]
print("Warm days:", sum(temperature >= 20 for temperature in temperatures))
