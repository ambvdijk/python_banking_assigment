

class InsufficientFundsException(Exception):
    def __init__(self):
        super().__init__("You have insufficient funds to perform this operation")