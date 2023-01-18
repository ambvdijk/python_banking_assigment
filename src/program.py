import os

from .authentication_menu import AuthenticationMenu
from .account_service import AccountService
from .account_store import AccountStore
from .account import Account

# TODO: Add (file,database) store to actually store the accounts
class Program:

    def __init__(self, path: str) -> None:
        self.path = path

    def run(self) -> None:
        
        store = AccountStore(self.path)
        accounts: list[Account] = store.read_or_create()

        AuthenticationMenu(AccountService(accounts)).run()

        store.store(accounts)
