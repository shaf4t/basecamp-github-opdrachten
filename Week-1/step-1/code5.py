#Code 05
my_str = input("Enter a string: ")
words = [word.lower() for word in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
	print(word)

    #de syntaxes die ik begrijp zijn: input(), list comprehension, split(), lower(), sort(), for loop, print().
    #ik begrijp elke statment in de lijst
    #Ik denk dat de uitkomst van de code is dat het de gebruiker vraagt om een string in te voeren, splitst deze in woorden, zet ze allemaal in kleine letters, sorteert ze alfabetisch en print ze vervolgens één voor één.
    