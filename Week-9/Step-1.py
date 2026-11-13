"""Week 9 - Stap 1: classes, objects, attributes en instance methods."""


# 1.1 Definieer een class voor een student.
class Student:
    """Een object waarin gegevens van één student worden opgeslagen."""

    # 1.2 Initialiseer het object met attributes.
    def __init__(self, name: str, student_number: str) -> None:
        self.name = name
        self.student_number = student_number

    # 1.3 Maak een instance method die een introductie teruggeeft.
    def introduce(self) -> str:
        return f"Mijn naam is {self.name} ({self.student_number})."


def main() -> None:
    # 1.4 Maak twee objects van de class Student.
    first_student = Student("Amina", "s1234567")
    second_student = Student("Bilal", "s7654321")

    # 1.5 Gebruik de method en lees de attributes uit.
    print(first_student.introduce())
    print(second_student.introduce())
    print(
        f"{first_student.name} heeft studentnummer "
        f"{first_student.student_number}."
    )


if __name__ == "__main__":
    main()