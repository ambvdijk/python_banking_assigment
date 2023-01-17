from ..account import Account
from ..exceptions.insufficient_funds_exception import InsufficientFundsException

def withdraw(account: Account) -> None:
    amount = abs(int(input("What amount would you like to withdraw? ")))

    if amount > account["balance"]:
        raise InsufficientFundsException

    account["balance"] = account["balance"] - amount
