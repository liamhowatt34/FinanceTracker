# console.py
ADD_TRANSACTION = 1
DISPLAY_TRANSACTION_LIST = 2
DELETE_TRANSACTION = 3
EXIT = 4
NOT_A_NUM = -1


class Console:

    @staticmethod
    def display_menu() -> None:
        options = {
            ADD_TRANSACTION: "Enter a new transaction.",
            DISPLAY_TRANSACTION_LIST: "Display transaction list.",
            DELETE_TRANSACTION: "Delete a transaction from the transaction list.",
            EXIT: "Exit app.",
        }

        for key, value in options.items():
            print(f"{key}. {value}")

    @staticmethod
    def get_num(prompt) -> float:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Error: Please enter a valid number.")
            return NOT_A_NUM
