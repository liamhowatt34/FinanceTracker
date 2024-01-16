# main.py
from database import Database
from transaction import Transaction


def main() -> None:
    Database.create_database()


if __name__ == "__main__":
    main()
