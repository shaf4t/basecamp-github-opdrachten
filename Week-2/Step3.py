#exercise 3.1
#Parameters zijn de plaatshouders die in de definitie van een functie staan
#(bijv. bij "def add(x, y):" zijn x en y de parameters).

#Arguments zijn de daadwerkelijke waarden die je meegeeft wanneer je de functie aanroept
#(bijv. bij "add(3, 5)" zijn 3 en 5 de arguments).


#exercise 3.2
def say_hello():
    print("hello")

say_hello()
#De functie wordt hierboven gedefinieerd in het def-blok.
#De functie wordt hierboven aangeroepen op de regel say_hello().


#exercise 3.3
def print_text(text):
    print(text)

print_text("Hallo, dit is een test!")


#exercise 3.4
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 7)
print(result)


#exercise 3.5
def multiply_by_2(number):
    return number * 2

def multiply_by_10(number):
    return number * 10

total = multiply_by_2(4) + multiply_by_10(4)
print(total)


#exercise 3.6
def say_hello():
    print("hello")

def say_bye():
    print("bye")

number = int(input("Enter a number: "))
if number > 10:
    say_hello()
else:
    say_bye()


#exercise 3.7
def say_bye():
    print("bye")

def say_hello():
    print("hello")
    say_bye()

say_hello()


#exercise 3.8

#eigen oefening 1: schrijf een functie die controleert of een getal even of oneven is
#de functie neemt een getal als argument en print "even" of "oneven"

def check_even_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("oneven")

check_even_odd(7)
check_even_odd(10)

#eigen oefening 2: schrijf een functie die de oppervlakte van een rechthoek berekent
#de functie neemt lengte en breedte als arguments en retourneert de oppervlakte
#roep de functie aan en print het resultaat

def calculate_area(length, width):
    return length * width

area = calculate_area(5, 3)
print(area)