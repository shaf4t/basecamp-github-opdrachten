numstr = input("Voer een 4 cijferig getal in: ")
sum = 0
text = ""
for i in range(len(numstr)):
   sum += int(numstr[i])
   text = text + numstr[i]
print(text)