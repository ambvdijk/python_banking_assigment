from typing import TypedDict


class Account(TypedDict):
    owner: str
    password_hash: str
    balance: int
