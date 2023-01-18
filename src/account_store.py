import json
import os

from .account import Account

FILE_NAME = "accounts.json"


class AccountStore:
    def __init__(self, path: str) -> None:
        self.path = path

    def read_or_create(self) -> list[Account]:
        file_path = os.path.join(self.path, FILE_NAME)
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r", encoding="UTF-8") as file_object:
            return json.load(file_object)

    def store(self, accounts: list[Account]):
        file_path = os.path.join(self.path, FILE_NAME)
        print(f"Storing account in {file_path}")
        with open(file_path, "w", encoding="UTF-8") as file_object:
            json.dump(accounts, file_object)
