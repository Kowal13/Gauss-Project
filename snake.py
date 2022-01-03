from game.Avatar import Snake
from game.Food import Apple
from game.Game import game.Game
from game.Display import Display
from game.Keyboard import Keyboard
from game.UserMovement import UserMovement
from AIMovement import  AIMovement
from Model import M1
from RewardFunction import RF

def main():

    model = M1(RF(10, -10))

    # starts the game
    Game(Display, Snake, Apple, UserMovement(), Keyboard()).run()
    #Game(Display, Snake, Apple, AIMovement(model), Keyboard()).run(True)

if __name__ == "__main__":
    main()
