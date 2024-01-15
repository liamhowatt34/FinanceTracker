import sqlite3
from utils import Input

NEGATIVE_NUMBER_OF_TRANSACTIONS = 1

conn = sqlite3.connect("finances.db")
cursor = conn.cursor()


class Database:
    def __init__(self) -> None:
        pass

    def create_database(self) -> None:
        cursor.execute(""" CREATE TABLE IF NOT EXIST finances (
                       transaction_desc TEXT,
                       transaction_amount REAL
                       transaction_date TEXT
                       ) """)

        conn.commit()

    def add_transaction(self) -> None:
        number_of_transactions = Input.get_num(
            "Enter the number of expenses you want to add: ")
        if number_of_transactions <= 0:
            return NEGATIVE_NUMBER_OF_TRANSACTIONS
        for i in range(0, number_of_tasks):


    def remove_transaction(self) -> None:
        pass
