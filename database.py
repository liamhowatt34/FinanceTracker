# database.py
import sqlite3

CONN = sqlite3.connect("finances.db")
CURSOR = CONN.cursor()


class Database:
    def __init__(self) -> None:
        self.transactions = []

    def create_database(self) -> None:
        CURSOR.execute(""" CREATE TABLE IF NOT EXISTS finances (
                        transaction_desc TEXT,
                        transaction_amount REAL,
                        transaction_date TEXT
                        ) """)

        CONN.commit()

    def display_transactions(self) -> None:
        CURSOR.execute("SELECT * FROM finances")
        self.transactions = [
            f"{row[0]}, {row[1]}, {row[2]}" for row in CURSOR.fetchall()]
        CONN.commit()

        for transaction in self.transactions:
            print(transaction)
