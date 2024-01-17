# main.py
from console import Console
from database import Database
from transaction import Transaction


ADD_TRANSACTION = 1
DISPLAY_TRANSACTION_LIST = 2
DELETE_TRANSACTION = 3
EXIT = 4


def main() -> None:
    Database.create_database()
    taking_input = True
    print("FINANCE TRACKING APP")
    print("-----------------------\n")

    while taking_input:
        Console.display_menu()
        print("\n")
        user_choice = Console.get_num("Select an option: ")

        if user_choice == ADD_TRANSACTION:
            Transaction.get_transaction()

        if user_choice == DISPLAY_TRANSACTION_LIST:
            Database.display_transactions()

        if user_choice == DELETE_TRANSACTION:
            # handle this
            pass

        if user_choice == EXIT:
            print("Exiting the app.")
            taking_input = False
            break


if __name__ == "__main__":
    main()
