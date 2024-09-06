# database.py
import sqlite3
from transaction import Transaction

NOT_AN_INT = -1
CONN = sqlite3.connect("finances.db")
CURSOR = CONN.cursor()


class Database:
    TOTAL = 0

    @classmethod
    def create_database(cls) -> None:
        CURSOR.execute(""" CREATE TABLE IF NOT EXISTS finances (
                        transaction_desc TEXT,
                        transaction_amount REAL,
                        transaction_date TEXT
                        ) """)
        CONN.commit()

    @classmethod
    def initialize_total(cls) -> None:
        CURSOR.execute("SELECT SUM(transaction_amount) FROM finances")
        result = CURSOR.fetchone()
        if result and result[0] is not None:
            cls.TOTAL = result[0]
        else:
            cls.TOTAL = 0

    @classmethod
    def display_transactions(cls) -> None:
        CURSOR.execute("SELECT * FROM finances")
        transactions = [
            f"Transaction: {row[0]}, ${row[1]}, {row[2]}" for row in CURSOR.fetchall()]
        CONN.commit()

        for transaction in transactions:
            print(transaction)
        if (transactions):
            print("-" * 50)

    @classmethod
    def insert_transaction(cls) -> None:
        transaction = Transaction.get_transaction()
        if transaction.amount == NOT_AN_INT:
            return

        cls.TOTAL += transaction.amount
        CURSOR.execute("INSERT INTO finances (transaction_desc, transaction_amount, transaction_date) VALUES (?, ?, ?)",
                       (transaction.description, transaction.amount, transaction.date))
        CONN.commit()

    @classmethod
    def delete_transaction(cls) -> None:
        description_to_delete = input(
            "Enter the transaction description to delete: ")

        CURSOR.execute(
            "SELECT transaction_amount FROM finances WHERE transaction_desc = ?", (description_to_delete,))
        result = CURSOR.fetchone()
        if result:
            deleted_amount = result[0]
            cls.TOTAL -= deleted_amount

        CURSOR.execute(
            "DELETE FROM finances WHERE transaction_desc = ?", (description_to_delete,))
        CONN.commit()

    @classmethod
    def close_connection(cls) -> None:
        CONN.close()
