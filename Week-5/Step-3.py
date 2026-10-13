# 3.1
def describe_arguments(*args, **kwargs):
	print("Positional arguments:", args)
	print("Keyword arguments:", kwargs)


describe_arguments("Python", "Week 5", topic="functions", completed=True)

# 3.2
def add_numbers(*args):
	return sum(args)


print(add_numbers(4, 8, 15, 16, 23, 42))

# 3.3
def count_passes(**kwargs):
	count = 0
	for result in kwargs.values():
		if result == "Pass":
			count += 1
	return count


result = count_passes(math="Fail", science="Fail", history="Pass", english="Pass")
print(result)

# 3.4a
def calculate_discount(price, discount=0.10):
	"""Return the price after applying a discount percentage."""
	return price * (1 - discount)


print(calculate_discount(100))
print(calculate_discount(price=100, discount=0.25))

# 3.4b
names = ["Ada", "Grace", "Linus"]
for name in names:
	print(name)
