from .menus.menu_option import MenuOption
from .menus.menu import Menu
from .types.account import Account
from .actions.withdraw_action import withdraw
from .actions.deposit_action import deposit
from .exceptions.insufficient_funds_exception import InsufficientFundsException

class AccountMenu:
    def __init__(self, account: Account):
        self.account = account
        self.menu = Menu(
            options=[
                MenuOption(char="B", text="Balance", action=self.show_balance),
                MenuOption(char="W", text="Withdraw", action=self.withdraw),
                MenuOption(char="D", text="Deposit", action=self.deposit),
                MenuOption(char="X", text="Exit"),
            ]
        )

    def show_balance(self):
        print(f'Your current balance is: {self.account["balance"]}')

    def deposit(self):
        try:
            deposit(self.account)
            print(f'Your new balance is: {self.account["balance"]}')
        except ValueError:
            print('The amount entered is not a valid number')


    def withdraw(self):
        try:
            withdraw(self.account)
            print(f'Your new balance is: {self.account["balance"]}')
        except ValueError:
            print('The amount entered is not a valid number')
        except InsufficientFundsException:
            print("You have insufficient funds to perform this operation")

    def run(self):
        while True:
            option = self.menu.run()
            if option.action is None:
                break
            option.action()
