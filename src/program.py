from .authentication_menu import AuthenticationMenu
from .account_service import AccountService

class Program:
    def run(self) -> None:
        AuthenticationMenu(AccountService([])).run()