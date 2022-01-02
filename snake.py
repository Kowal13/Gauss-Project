from Avatar import Snake
from Food import Apple
from Game import Game
from Display import Display
from Keyboard import Keyboard
from UserMovement import UserMovement
from AIMovement import  AIMovement
from Model import M1
from RewardFunction import RF

def main():

    model = M1(RF())

    Game(Display, Snake, Apple, UserMovement(), Keyboard()).run()
    #Game(Display, Snake, Apple, AIMovement(model), Keyboard()).run(True)

if __name__ == "__main__":
    main()


        
        