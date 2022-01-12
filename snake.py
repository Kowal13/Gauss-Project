from game.Display import Display
from menu import Menu


def main():
    display = Display()
    menu = Menu(display)
    menu.menu_display()


if __name__ == "__main__":
    main()
