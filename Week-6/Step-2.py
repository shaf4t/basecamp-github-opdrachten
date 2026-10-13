# 2.1
# Een set bevat unieke, ongeordende waarden en kan worden gewijzigd.
# Een tuple is geordend en onveranderlijk, en kan daarom dubbele waarden bevatten.

# 2.2
# Een set bevat geen dubbele waarden en heeft geen indexen.
# Een list is geordend, kan dubbele waarden bevatten en ondersteunt indexering.

# 2.3
planets = {"Mercury", "Venus", "Earth", "Mars"}
print("Aantal planeten:", len(planets))
print("Een willekeurige laatste waarde:", next(iter(planets)))

planets.add("Jupiter")
planets.discard("Mars")
print("Planeten:", planets)

# 2.4
def values_to_set(dictionary):
    return set(dictionary.values())


temperatures = {"morning": 12, "afternoon": 20, "evening": 12}
temperature_set = values_to_set(temperatures)
print("Unieke temperaturen:", temperature_set)
for temperature in temperature_set:
    print(temperature)

# 2.5
letters = {"x", "y", "q", "z", "u"}
letter = input("Voer een van de letters x, y, q, z of u in: ")
if letter in letters:
    print("ja")
else:
    print("nee")

# 2.6a - Zoek gedeelde en unieke onderwerpen.
python_topics = {"functions", "dictionaries", "sets"}
web_topics = {"functions", "HTML", "CSS"}
print("Doorsnede:", python_topics & web_topics)
print("Unie:", python_topics | web_topics)
print("Alleen Python-onderwerpen:", python_topics - web_topics)
print("Python-onderwerpen zijn een deelverzameling:", python_topics <= web_topics)

# 2.6b - Verwijder dubbele namen met behulp van een set.
names = ["Ada", "Grace", "Ada", "Linus", "Grace"]
unique_names = set(names)
print("Unieke namen:", unique_names)
