import os
import platform
from model import Board

# ANSI escape codes
# voir https://en.wikipedia.org/wiki/ANSI_escape_code

def print_at_xy(x: int, y: int, s: str):
    print(f"\033[{y};{x}H{s}")


def hide_cursor():
    print("\033[?25l")


def show_cursor():
    print("\033[?25h")


def clean_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033[2J")


class BoardTerminalDisplay:
    def __init__(self, board: Board):
        self.board = board

    def draw(self):
        clean_screen()
        self.__draw_border()
        self.__draw_entities()
        hide_cursor()

    def __draw_border(self):
        for y in range(self.board.height + 2):
            if y == 0 or y == self.board.height + 1:
                print_at_xy(1, y+1, "X" * (self.board.width + 2))
            else:
                print_at_xy(1, y+1, "X" + " " * self.board.width + "X")

    def __draw_entities(self):
        for entity in self.board.entities:
            # print(f"Drawing {entity.name} at {entity.pos}")
            # Etant donné que le terminal commence à (1,1) et que les frontieres ont une largeur de 1, on décale de 2
            print_at_xy(entity.pos.x + 2, entity.pos.y + 2, entity.name)

