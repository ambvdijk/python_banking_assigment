import random
from hashlib import sha256
from typing import Callable, Optional, TypedDict, Tuple


class Account(TypedDict):
    number: str
    pin: str
    balance: int


class MenuOption:
    def __init__(
        self, char: str, text: str, action: Optional[Callable[[], None]] = None
    ) -> None:
        super().__init__()
        self.char = char
        self.text = text
        self.action = action


class Menu:
    def __init__(self, options: list[MenuOption]) -> None:
        super().__init__()
        self.options = options

    def run(self) -> None:
        option: MenuOption = None
        while option is None:

            for opt in self.options:
                print(f"[{opt.char}]: {opt.text}")

            choice = input("Enter your choice: ")
            option = next(
                (option for option in self.options if option.char == choice), None
            )
            if option is None:
                print(f"Unknown option [{choice}]. Please try again...")
        return option


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


class AuthenticationMenu:
    def __init__(self, account_service: AccountService) -> None:
        self.account_service = account_service
        self.menu = Menu(
            options=[
                MenuOption(char="C", text="Create account", action=self.create_account),
                MenuOption(char="L", text="Login", action=self.login),
                MenuOption(char="X", text="Exit"),
            ]
        )

    def create_account(self) -> None:
        (account, pin) = self.account_service.create()
        print(f'Created account [{account["number"]}] with pin [{pin}]')

    def login(self) -> None:
        account = self.account_service.login()
        if account is None:
            return
        AccountMenu(account).run()

    def run(self):
        while True:
            option = self.menu.run()
            if option.action is None:
                break
            option.action()


class AccountMenu:
    def __init__(self, account: Account):
        self.account = account
        self.menu = Menu(
            options=[
                MenuOption(char="W", text="Withdraw", action=self.withdraw),
                MenuOption(char="D", text="Deposit", action=self.deposit),
                MenuOption(char="X", text="Exit"),
            ]
        )

    def deposit(self):
        while True:
            try:
                amount = abs(int(input("What amount would you like to deposit? ")))
                self.account["balance"] = self.account["balance"] + amount
                print(f'Your new balance is: {self.account["balance"]}')
                break
            except:
                continue

    def withdraw(self):
        while True:
            try:
                amount = abs(int(input("What amount would you like to withdraw? ")))
                if amount > self.account["balance"]:
                    print(
                        f'The maximum amount you can withdraw is {self.account["balance"]}'
                    )
                    continue
                self.account["balance"] = self.account["balance"] - amount
                print(f'Your new balance is: {self.account["balance"]}')
                break
            except:
                continue

    def run(self):
        while True:
            option = self.menu.run()
            if option.action is None:
                break
            option.action()


class Program:
    def run(self) -> None:
        AuthenticationMenu(AccountService([])).run()


if __name__ == "__main__":
    Program().run()
