"""Week 9 - Code-analyse: voorspel, voer uit en leg het programma uit.

Het oorspronkelijke voorbeeld gebruikte ``add_books`` om de volledige lijst
iedere keer te vervangen. De verbeterde versie hieronder gebruikt ``add_book``
om één boek toe te voegen zonder eerder opgeslagen boeken kwijt te raken.
"""


# 4.1 Definieer de class Book.
class Book:
    # 4.2 Initialiseer de titel en auteur van een boek.
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    # 4.3 Maak een tekstrepresentatie van een boek.
    def __repr__(self) -> str:
        return f"Titel: {self.title}, Auteur: {self.author}"


# 4.4 Definieer de class Library.
class Library:
    # 4.5 Initialiseer een bibliotheek met een lege boekenlijst.
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    # 4.6 Voeg één boek toe zonder de bestaande lijst te vervangen.
    def add_book(self, book: Book) -> None:
        self.books.append(book)

    # 4.7 Toon de boeken die in de bibliotheek zijn opgeslagen.
    def display_books(self) -> None:
        print(f"Boeken in bibliotheek {self.name}:")
        for book in self.books:
            print(book)


def main() -> None:
    # 4.8 Maak vier Book-objects.
    book1 = Book("Introducing Python", "Bill Lubanovic")
    book2 = Book("The Python Workbook", "Ben Stephenson")
    book3 = Book("Learn Python Programming", "Fabrizio Romano")
    book4 = Book("Fluent Python", "Luciano Ramalho")

    # 4.9 Maak twee Library-objects.
    university_library = Library("University")
    city_library = Library("City")

    # 4.10 Voeg boeken toe zonder eerdere toevoegingen te overschrijven.
    university_library.add_book(book1)
    university_library.add_book(book4)
    city_library.add_book(book1)
    city_library.add_book(book3)
    university_library.add_book(book2)
    city_library.add_book(book4)

    # 4.11 Toon de uiteindelijke inhoud van beide bibliotheken.
    university_library.display_books()
    city_library.display_books()


if __name__ == "__main__":
    main()
