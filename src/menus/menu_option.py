from typing import Callable, Optional

class MenuOption:
    def __init__(
        self, char: str, text: str, action: Optional[Callable[[], None]] = None
    ) -> None:
        super().__init__()
        self.char = char
        self.text = text
        self.action = action
