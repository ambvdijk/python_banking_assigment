from .menu_option import MenuOption

class Menu:
    def __init__(self, options: list[MenuOption]) -> None:
        super().__init__()
        self.options = options

    def run(self) -> None:
        option: MenuOption = None
        while option is None:

            for opt in self.options:
                print(f"[{opt.char}]: {opt.text}")

            choice = input("Enter your choice: ")
            option = next(
                (
                    option
                    for option in self.options
                    if option.char.lower() == choice.lower()
                ),
                None,
            )
            if option is None:
                print(f"Unknown option [{choice}]. Please try again...")
        return option
