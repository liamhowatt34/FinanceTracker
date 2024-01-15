NOT_AN_INT = 1


class Utils:
    def __init__(self) -> None:
        pass

        def get_num(prompt):
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                return NOT_AN_INT
