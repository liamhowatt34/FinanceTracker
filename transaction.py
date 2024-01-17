# transaction.py
import datetime
from console import Console


class Transaction:
    def __init__(self, description, amount, date) -> None:
        self.description = description
        self.amount = amount
        self.date = date

    @classmethod
    def get_transaction(cls) -> 'Transaction':
        description = input("Enter the transaction description: ")
        amount = Console.get_num("Enter the transaction amount: ")
        current_datetime = datetime.datetime.now()
        formatted_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        return cls(description, amount, formatted_string)
