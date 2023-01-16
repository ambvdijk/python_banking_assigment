from typing import Callable, Optional, TypedDict


class Account(TypedDict):
    owner: str
    password_hash: str
    balance: int


class MenuOption:
    def __init__(self, char: str, text: str, action: Optional[Callable[[], None]] = None) -> None:
        super().__init__()
        self.char = char
        self.text = text
        self.action = action


class Menu:
    def __init__(self, options: list[MenuOption]) -> None:
        super().__init__()
        self.options = options

    def display(self) -> None:
        for option in self.options:
            print(f"[{option.char}]: {option.text}")

    def navigate(self) -> None:
        choice = input("Enter your choice: ")

class AccountService:

    def create(self) -> Optional[Account]:
        pass

    def login(self)-> Optional[Account]:
        pass

class AuthenticationMenu:
    def __init__(self):
        self.account_service = AccountService()
        self.menu = Menu(
            options=[
                MenuOption(char="C", text="Create account"),
                MenuOption(char="L", text="Login"),
                MenuOption(char="X", text="Exit"),
            ]
        )

    def create_account(self):
        account = self.account_service.create()
        pass

    def run(self):
        self.menu.display()
        self.menu.navigate()


class Program:
    def run(self) -> None:
        account = AuthenticationMenu().run()


if __name__ == "__main__":
    Program().run()
