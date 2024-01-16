# database.py
import sqlite3

CONN = sqlite3.connect("finances.db")
CURSOR = CONN.cursor()


class Database:
    def __init__(self) -> None:
        pass

    def create_database() -> None:
        CURSOR.execute(""" CREATE TABLE IF NOT EXIST finances (
                        transaction_desc TEXT,
                        transaction_amount REAL,
                        transaction_date TEXT
                        ) """)

        CONN.commit()
