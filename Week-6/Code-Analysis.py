# 1
# De eerste lus print de tekens die in beide sets voorkomen. Omdat sets
# ongeordend zijn, ligt de exacte volgorde niet vast. De gedeelde tekens zijn:
# o, i en h.
print("Stap 1:")
sfind = set("orihme")
schar = set("ichgo")
for character in sfind:
    if character in schar:
        print(character)

# update() voegt alle tekens uit sfind toe aan schar. De tweede lus print
# daarom elk teken uit de unie van beide sets, ook in willekeurige volgorde.
print("Stap 2:")
schar.update(sfind)
for character in schar:
    print(character)

# 2
# rdic begint leeg. Elk geheel getal van 0 tot en met 9 wordt als sleutel
# gebruikt en krijgt een willekeurig getal van 0 tot en met 100 als waarde.
# De laatste lus print de tien waarden. Deze verschillen telkens door de
# willekeurige getallen.
import random

rdic = {}
for i in range(0, 10):
    rdic[i] = random.randint(0, 100)
for item in rdic.values():
    print(item)

# 3
# De eerste lambda telt 15 op bij 10 en print daarom 25. De variabele r wordt
# daarna vervangen door een tweede lambda, die 12 en 4 vermenigvuldigt en 48 print.
r = lambda a: a + 15
print(r(10))
r = lambda x, y: x * y
print(r(12, 4))
