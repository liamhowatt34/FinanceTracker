# console.py
ADD_TRANSACTION = 1
DISPLAY_TRANSACTION_LIST = 2
DELETE_TRANSACTION = 3
EXIT = 4
MENU_SIZE = 4
NOT_AN_INT = -1


class Console:
    def __init__(self) -> None:
        pass

    @staticmethod
    def display_menu():
        options = {
            ADD_TRANSACTION: "Enter a new transaction(s).",
            DISPLAY_TRANSACTION_LIST: "Display transaction list.",
            DELETE_TRANSACTION: "Delete a transaction from the transaction list.",
            EXIT: "Exit app.",
        }
        for key, value in options.items():
            print(f"{key}. {value}")

    @staticmethod
    def get_num(prompt):
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            return NOT_AN_INT
