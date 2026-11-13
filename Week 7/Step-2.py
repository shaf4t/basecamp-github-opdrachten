"""Week 7 - Stap 2: initialisatie, statuswijzigingen en object scope."""


# 2.1 Definieer een class met een class attribute.
class BankAccount:
    """Een bankrekening met gegevens per afzonderlijk object."""

    bank_name = "Learning Bank"

    # 2.2 Initialiseer de attributes van ieder account-object.
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    # 2.3 Voeg geld toe met een instance method.
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("De storting moet groter zijn dan nul.")
        self.balance += amount

    # 2.4 Neem geld op zonder onder nul uit te komen.
    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    # 2.5 Geef de huidige status van het object terug.
    def summary(self) -> str:
        return f"{self.owner}: EUR {self.balance:.2f}"


def main() -> None:
    # 2.6 Maak een object en wijzig de objectstatus.
    account = BankAccount("Noor", 100.0)
    account.deposit(25.0)
    account.withdraw(40.0)

    print(account.summary())
    print(f"Class-attribuut: {BankAccount.bank_name}")
    print(f"Namespace van het object: {account.__dict__}")


if __name__ == "__main__":
    main()
