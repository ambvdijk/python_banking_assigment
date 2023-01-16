from .account_service import AccountService
from .account_menu import AccountMenu
from .menus.menu_option import MenuOption
from .menus.menu import Menu

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
