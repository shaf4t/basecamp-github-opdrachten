#exercise 2.1 
boolean = True
print(boolean)
boolean = False
print(boolean)


#exercise 2.2
a = True
b = False
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)


#exercise 2.3
#dit if-statement vergelijkt a en b met alle vergelijkingsoperatoren
#en print "yes" als de vergelijking True is, anders "no"
a = True
b = False
if a == b:
    print("yes")
else:
    print("no")

if a != b:
    print("yes")
else:
    print("no")

if a < b:
    print("yes")
else:
    print("no")

if a > b:
    print("yes")
else:
    print("no")

if a <= b:
    print("yes")
else:
    print("no")

if a >= b:
    print("yes")
else:
    print("no")


#exercise 2.4
word = input("Enter a word: ")
if "e" in word:
    print("yes")
else:
    print("no")


#exercise 2.5
#nested if-statement: eerst checken of de gebruiker een leeftijd heeft ingevuld
#die uberhaupt geldig is, en pas daarna checken of diegene oud genoeg is
age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    if age >= 18:
        print("yes, you are an adult")
    else:
        print("no, you are a minor")
else:
    print("invalid input")