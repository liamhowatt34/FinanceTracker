# transaction.py
NOT_AN_INT = -1


def get_num(prompt):
    try:
        user_input = int(input(prompt))
        return user_input
    except ValueError:
        return NOT_AN_INT


class Transaction:
    def __init__(self, description, amount, date) -> None:
        self.description = description
        self.amount = amount
        self.date = date

    def get_transaction(self, description, amount, date) -> None:
        pass
