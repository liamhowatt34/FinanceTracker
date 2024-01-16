# console.py
ADD_TRANSACTION = 1
DISPLAY_TRANSACTION_LIST = 2
DELETE_TRANSACTION = 3
EXIT = 4
MENU_SIZE = 4
NUMBER_TOO_BIG = -1
NOT_AN_INT = -2


class Console:
    def __init__(self) -> None:
        pass

    def display_menu():
        options = {
            ADD_TRANSACTION: "Enter a new transaction(s).",
            DISPLAY_TRANSACTION_LIST: "Display transaction list.",
            DELETE_TRANSACTION: "Delete a transaction from the transaction list.",
            EXIT: "Exit app.",
        }
        for key, value in options.items():
            print(f"{key}. {value}")

    def get_num(prompt):
        try:
            user_input = int(input(prompt))
            if user_input > MENU_SIZE:
                return NUMBER_TOO_BIG
            return user_input
        except ValueError:
            return NOT_AN_INT