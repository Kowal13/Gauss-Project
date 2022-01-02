from Avatar import Snake
from Food import Apple
from Game import Game
from Display import Display
from Keyboard import Keyboard
from UserMovement import UserMovement

def main():
    Game(Display(), Snake(), Apple(), UserMovement(), Keyboard()).run()
    
if __name__ == "__main__":
    main()


        
        