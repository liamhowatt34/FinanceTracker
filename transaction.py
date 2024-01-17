# transaction.py
import datetime
from console import Console
NOT_AN_INT = -1


class Transaction:
    def __init__(self, description, amount, date) -> None:
        self.description = description
        self.amount = amount
        self.date = date

    def get_transaction(self) -> None:
        number_of_transactions = Console.get_num(
            "Enter number of transactions to log: ")
        if number_of_transactions == NOT_AN_INT:
            return NOT_AN_INT

        current_datetime = datetime.datetime.now()
        formatted_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        for _ in range(0, number_of_transactions):
            self.description = input("Enter the transaction description: ")
            self.amount = Console.get_num("Enter the transaction amount: ")
            self.date = formatted_string

        return 0
