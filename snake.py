from game.Display import Display
from menu import Menu

<<<<<<< HEAD
=======

def main():
>>>>>>> 9d9188eed3d1c55f5051b3c0742f4e54909d85c0

def main():
    display = Display()
    menu = Menu(display)
    menu.menu_display()

<<<<<<< HEAD
=======
    # starts the game
    Game(Display, Snake, Apple, UserMovement(), Keyboard()).run()
    # Game(Display, Snake, Apple, AIMovement(model), Keyboard()).run(True)

>>>>>>> 9d9188eed3d1c55f5051b3c0742f4e54909d85c0

if __name__ == "__main__":
    main()
