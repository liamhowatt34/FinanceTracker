# database.py
import sqlite3
from transaction import Transaction

CONN = sqlite3.connect("finances.db")
CURSOR = CONN.cursor()


class Database:
    def __init__(self) -> None:
        self.transactions = []

    @classmethod
    def create_database(cls) -> None:
        CURSOR.execute(""" CREATE TABLE IF NOT EXISTS finances (
                        transaction_desc TEXT,
                        transaction_amount REAL,
                        transaction_date TEXT
                        ) """)

        CONN.commit()

    @classmethod
    def display_transactions(cls) -> None:
        CURSOR.execute("SELECT * FROM finances")
        transactions = [
            f"{row[0]}, {row[1]}, {row[2]}" for row in CURSOR.fetchall()]
        CONN.commit()

        for transaction in transactions:
            print(transaction)

    @classmethod
    def insert_transaction(cls) -> None:
        transaction = Transaction.get_transaction()

        CURSOR.execute("INSERT INTO finances (transaction_desc, transaction_amount, transaction_date) VALUES (?, ?, ?)",
                       (transaction.description, transaction.amount, transaction.date))
        CONN.commit()

    @classmethod
    def delete_transaction(cls) -> None:
        description_to_delete = input(
            "Enter the transaction description to delete: ")

        CURSOR.execute(
            "DELETE FROM finances WHERE transaction_desc = ?", (description_to_delete,))
        CONN.commit()

    @classmethod
    def close_connection(cls) -> None:
        CONN.close()
