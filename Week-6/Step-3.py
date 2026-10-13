# 3.1
even = lambda number: number % 2 == 0
print(even(4))
print(even(13))

# 3.2
numbers = list(range(1, 11))
is_even = lambda number: number % 2 == 0
even_numbers = list(filter(is_even, numbers))
odd_numbers = list(filter(lambda number: not is_even(number), numbers))
print("Even getallen:", even_numbers)
print("Oneven getallen:", odd_numbers)

# 3.3
def am_i_sorted(numberlist):
    is_in_order = lambda first, second: first <= second
    return all(
        is_in_order(first, second)
        for first, second in zip(numberlist, numberlist[1:])
    )


result = am_i_sorted([1, 2, 5, 6, 8, 17])
print(result)
result = am_i_sorted([1, 2, 99, 6, 8, 17])
print(result)

# 3.4
make_tuple = lambda first, second: (first, second)
print(make_tuple("Python", 6))

# 3.5a - Zet temperaturen om met map().
temperatures_celsius = [0, 10, 20, 30]
to_fahrenheit = lambda celsius: celsius * 9 / 5 + 32
temperatures_fahrenheit = list(map(to_fahrenheit, temperatures_celsius))
print("Temperaturen in Fahrenheit:", temperatures_fahrenheit)

# 3.5b - Sorteer studenten op hun score met een key-lambda.
students = [("Alice", 8), ("Bob", 6), ("Charlie", 9)]
students_by_score = sorted(students, key=lambda student: student[1])
print("Studenten op score:", students_by_score)
