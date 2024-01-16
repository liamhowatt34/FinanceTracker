# transaction.py
from console import Console


class Transaction:
    def __init__(self, description, amount, date) -> None:
        self.description = description
        self.amount = amount
        self.date = date

    def get_transaction(self, description, amount, date) -> None:
        number_of_transactions = Console.get_num(
            "Enter number of transactions to log: ")
