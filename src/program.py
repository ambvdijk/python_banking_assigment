from .authentication_menu import AuthenticationMenu
from .account_service import AccountService

# TODO: Add (file,database) store to actually store the accounts
class Program:
    def run(self) -> None:
        AuthenticationMenu(AccountService([])).run()
