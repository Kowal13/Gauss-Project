import pygame
from game.Display import Display

class Game:
    FPS = 10
    
    def __init__(self, display, av, food, movement, keyboard):
        self.keyboard = keyboard
        self.clock = pygame.time.Clock()
        self.score = 0
        self.iteration = 0
        self.avatar_cl = av
        self.avatar = self.avatar_cl()
        self.food_cl = food
        self.food = self.food_cl()
        self.display_cl = display
        self.display = self.display_cl()
        self.movement = movement
        self.plot_score = []
        self.plot_mean_score = []
        self.eating_sound = pygame.mixer.Sound("Assets/eating_sound.wav")

    def reset(self):
        self.score = 0
        self.iteration = 0
        self.avatar = self.avatar_cl()
        self.food = self.food_cl()
        self.display = self.display_cl()

    def run(self, run_forever = False):
        is_game_over = False
        
        while not is_game_over:
            is_game_over = self.play_step(run_forever)

        print("Score:", self.score)
        pygame.quit()            
 
    def should_quit(self, key_list):
        for ev in key_list:
            if ev.type == pygame.QUIT or ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return True

    def play_step(self, run_forever):
        # get key inputs from keyboard as a list
        key_list = self.keyboard.get_event_list()
        if self.should_quit(key_list):
            return True

        food_eaten = self.movement.move(key_list, self.avatar, self.food)
        is_game_over = self.is_game_over()
        if is_game_over:
            if not run_forever:
                return True
            else:
                self.reset()
                is_game_over = False

        if food_eaten:
            self.score += 1
            self.food.place_food(self.avatar.body)
            self.eating_sound.play()
        

        self.display.update([self.avatar, self.food], self.score)
        self.clock.tick(self.FPS)

        return is_game_over


    def is_game_over(self):
        if self.avatar.is_collision() or self.avatar.is_out_of_boundary():
            return True

        return False