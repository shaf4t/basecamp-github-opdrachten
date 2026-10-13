import random


# 1.1
# Een dictionary slaat waarden op met unieke sleutels. Een tuple is een
# geordende, onveranderlijke verzameling waarden.

# 1.2
person = {"FirstName": "Larry", "LastName": "Page"}
print(person["LastName"])

# 1.3
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print("Waarden:", car.values())
print("Sleutels:", car.keys())
print("Lengte:", len(car))

car["color"] = "Red"
del car["year"]
print("Sleutels na wijzigingen:", car.keys())
print("Waarden na wijzigingen:", car.values())

# 1.4
random_car = {
    key: (random.randint(1, 100), random.randint(1, 100))
    for key in car
}
print("Dictionary met willekeurige tuples:", random_car)

# 1.5a - Tel hoe vaak elk woord voorkomt.
words = ["python", "set", "python", "dictionary", "set", "python"]
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print("Woordaantallen:", word_counts)

# 1.5b - Laat iteratie, get(), pop() en clear() zien.
scores = {"Alice": 8, "Bob": 7, "Charlie": 9}
for name, score in scores.items():
    print(name, "heeft", score, "punten")
print("Score van Bob:", scores.get("Bob"))
removed_score = scores.pop("Bob")
print("Verwijderde score:", removed_score)
scores.clear()
print("Na clear:", scores)
