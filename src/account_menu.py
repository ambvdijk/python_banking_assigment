from typing import Callable, Optional, TypedDict, Tuple
from .menus.menu_option import MenuOption
from .menus.menu import Menu
from .types.account import Account

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
