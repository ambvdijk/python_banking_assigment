from ..account import Account

def deposit(account: Account) -> None:
    amount = abs(int(input("What amount would you like to deposit? ")))
    account["balance"] = account["balance"] + amount