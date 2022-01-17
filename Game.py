import pygame
from game.Display import Display
from plot_score import score_plot

class Game:
    FPS = 10
    
    def __init__(self, display, av, food, movement, keyboard):
        self.keyboard = keyboard
        self.clock = pygame.time.Clock()
        self.score = 0
        self.iteration = 0
        self.plot_iteration = []
        self.avatar_cl = av
        self.avatar = self.avatar_cl()
        self.food_cl = food
        self.food = self.food_cl()
        self.display = display
        self.movement = movement
        self.plot_score = []
        self.plot_mean_score = []
        self.eating_sound = pygame.mixer.Sound("Assets/eating_sound.wav")
        try:
            self.rf = movement.model.reward_function
        except AttributeError:
            self.rf = None

    def reset(self):
        self.plot_score.append(self.score)
        self.plot_iteration.append(str(self.iteration))
        self.score = 0
        self.iteration += 1
        self.avatar = self.avatar_cl()
        self.food = self.food_cl()
        self.display = Display()
        self.movement.prev_direction = 'right'
        score_plot(self.plot_score, self.plot_iteration)


    def run(self, run_forever=False):
        is_game_over = False
        
        while not is_game_over:
            is_game_over, reward = self.play_step(run_forever)

        print("Score:", self.score)
        pygame.quit()

    def should_quit(self, key_list):
        for ev in key_list:
            if ev.type == pygame.QUIT or ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return True

    def play_step(self, run_forever):
        reward = 0
        # get key inputs from keyboard as a list
        key_list = self.keyboard.get_event_list()
        if self.should_quit(key_list):
            return True

        food_eaten = self.movement.move(key_list, self.avatar, self.food)
        is_game_over = self.is_game_over()
        if is_game_over:
            if self.rf is not None:
                reward = self.rf.penalty
            if not run_forever:
                return True, reward
            else:
                self.reset()
                is_game_over = False

        if food_eaten:
            if self.rf is not None:
                reward = self.rf.reward

            self.score += 1
            self.food.place_food(self.avatar.body)
            self.eating_sound.play()

        self.display.update([self.avatar, self.food], self.score)
        self.clock.tick(self.FPS)
        return is_game_over, reward

    def is_game_over(self):
        if self.avatar.is_collision() or self.avatar.is_out_of_boundary():
            return True
        return False
