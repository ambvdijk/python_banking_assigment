import random

from hashlib import sha256
from typing import Optional, Tuple
from .types.account import Account

class AccountService:
    def __init__(self, accounts: list[Account]) -> None:
        self.accounts = accounts

    def create_account_number(self) -> str:
        return f"{random.randrange(0, 1000000):06}"

    def create_pin_number(self) -> str:
        return f"{random.randrange(0, 10000):04}"

    def hash(self, text: str) -> str:
        return sha256(text.encode()).hexdigest()

    def create(self) -> Tuple[Account, str]:

        account_number = self.create_account_number()
        pin = self.create_pin_number()

        account: Account = {
            "number": account_number,
            "pin": self.hash(pin),
            "balance": 0,
        }

        self.accounts.append(account)

        return (account, pin)

    def login(self) -> Optional[Account]:
        account_number = input("Please enter your 6 digit account number: ")

        account = next(
            (
                account
                for account in self.accounts
                if account["number"] == account_number
            ),
            None,
        )

        if account is None:
            print(f"Account with number [{account_number}] does not exist")
            return None

        pin = input("Please enter your 4 digit pin: ")

        hashed_pin = self.hash(pin)

        if account["pin"] == hashed_pin:
            return account

        return None
