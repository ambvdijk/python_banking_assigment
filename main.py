import os
from src.program import Program

if __name__ == "__main__":
    root_path = os.path.dirname(os.path.realpath(__file__))
    Program(root_path).run()
    