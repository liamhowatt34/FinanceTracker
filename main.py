# main.py
from console import Console
from database import Database

ADD_TRANSACTION = 1
DISPLAY_TRANSACTION_LIST = 2
DELETE_TRANSACTION = 3
EXIT = 4
MENU_SIZE = 4


def main() -> None:
    try:
        Database.create_database()
        taking_input = True
        print("FINANCE TRACKING APP")
        print("-----------------------\n")

        while taking_input:
            Database.initialize_total()
            print("\nTotal +/-: $", Database.TOTAL)

            print("\n")
            Console.display_menu()
            print("\n")

            user_choice = Console.get_num("Select an option: ")
            if user_choice > MENU_SIZE:
                print("Enter a valid menu option.")
                continue

            if user_choice == ADD_TRANSACTION:
                Database.insert_transaction()

            if user_choice == DISPLAY_TRANSACTION_LIST:
                Database.display_transactions()

            if user_choice == DELETE_TRANSACTION:
                Database.delete_transaction()

            if user_choice == EXIT:
                print("Exiting the app.")
                taking_input = False
                break

    finally:
        Database.close_connection()


if __name__ == "__main__":
    main()
