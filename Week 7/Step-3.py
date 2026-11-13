"""Week 7 - Stap 3: een kleine objectgeoriënteerde bibliotheek."""


# 3.1 Definieer een class voor een boek.
class Book:
    # 3.2 Initialiseer de gegevens van een boek.
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    # 3.3 Geef een leesbare tekstrepresentatie van een boek.
    def __repr__(self) -> str:
        return f"Titel: {self.title}, Auteur: {self.author}"


# 3.4 Definieer een class die boeken beheert.
class Library:
    # 3.5 Initialiseer een lege boekenlijst.
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    # 3.6 Voeg één boek toe aan de bibliotheek.
    def add_book(self, book: Book) -> None:
        self.books.append(book)

    # 3.7 Verwijder een boek op basis van de titel.
    def remove_book(self, title: str) -> bool:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    # 3.8 Toon alle boeken in de bibliotheek.
    def display_books(self) -> None:
        print(f"Boeken in bibliotheek {self.name}:")
        if not self.books:
            print("Geen boeken beschikbaar.")
            return
        for book in self.books:
            print(book)


def main() -> None:
    # 3.9 Maak twee bibliotheek-objects.
    university_library = Library("University")
    city_library = Library("City")

    # 3.10 Maak vier boek-objects.
    book1 = Book("Introducing Python", "Bill Lubanovic")
    book2 = Book("The Python Workbook", "Ben Stephenson")
    book3 = Book("Learn Python Programming", "Fabrizio Romano")
    book4 = Book("Fluent Python", "Luciano Ramalho")

    # 3.11 Voeg de boeken toe aan de juiste bibliotheek.
    university_library.add_book(book1)
    university_library.add_book(book2)
    city_library.add_book(book3)
    city_library.add_book(book4)

    # 3.12 Toon de inhoud van beide bibliotheken.
    university_library.display_books()
    city_library.display_books()


if __name__ == "__main__":
    main()
