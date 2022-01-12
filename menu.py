import pygame
import pygame_menu
from Game import Game
from game.Display import Display
from game.Avatar import Snake
from game.Food import Apple
from game.Display import Display
from game.Keyboard import Keyboard
from game.UserMovement import UserMovement
from net.AIMovement import AIMovement
from net.Model import M1
from net.RewardFunction import RF


class Menu:
    def __init__(self, display):
        self.display_obj = display
        self.reset_game = True
        self.play_option = "Human"
        self.menu = pygame_menu.Menu('Welcome', self.display_obj.WIDTH, self.display_obj.HEIGHT,
                                     theme=pygame_menu.themes.THEME_BLUE)

    def menu_display(self):
        self.menu.add.button('Play', self.start_the_game)
        self.menu.add.selector('Player :', [('Human', 1), ('AI', 2)], onchange=self._set_player)
        self.menu.add.selector('Restart Game :', [('Yes', 1), ('No', 2)], onchange=self._set_restart_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.display_obj.display)

    def _set_restart_game(self, _, option):
        if option == 1:
            self.reset_game = True

        if option == 2:
            self.reset_game = False

    def _set_player(self, _, option):
        if option == 1:
            self.play_option = "Human"

        if option == 2:
            self.play_option = "AI"

    def start_the_game(self):
        if self.play_option == "Human":
            Game(self.display_obj, Snake, Apple, UserMovement(), Keyboard()).run(self.reset_game)

        if self.play_option == "AI":
            model = M1(RF(10, -10))
            Game(self.display_obj, Snake, Apple, AIMovement(model), Keyboard()).run(self.reset_game)
