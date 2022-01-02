import pygame
from Display import Display

class Game:
    FPS = 10

    def __init__(self, display, snake, apple, movement, keyboard):
        self.keyboard = keyboard
        self.clock = pygame.time.Clock()
        self.score = 0 
        self.snake = snake 
        self.apple = apple
        self.display = display
        self.movement = movement

    def run(self):
        is_game_over = False
        while not is_game_over:
            is_game_over = self.play_step()

        print("Score:", self.score)
        pygame.quit()            
 
    def should_quit(self, key_list):
        for ev in key_list:
            if ev.type == pygame.QUIT or ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                return True

    def play_step(self):
        print("hello")
        key_list = self.keyboard.get_event_list()
        if self.should_quit(key_list):
            return True


        self.snake.move(self.movement.get_move(key_list), self.food_eaten())

        #if was_apple_eaten:
        #    self.score += 1
        #    self.apple.place_apple(self.snake.body)
        #self.game_over = self.is_game_over()
        self.display.update(self.snake, [self.apple])
        self.clock.tick(self.FPS)

        return self.is_game_over()

    def food_eaten(self):
        if self.snake.head == self.apple.location:
            return True

    def is_game_over(self):
        if self._is_collision() or self._is_out_of_boundary():
            return True

        return False

    def _is_collision(self):
        if self.snake.head in self.snake.body[1:]:
            return True

        return False
    
    def _is_out_of_boundary(self):
        if self.snake.head[0] > Display.WIDTH - Display.BLOCK_SIZE:
            return True
        elif self.snake.head[0] < 0:
            return True
        elif self.snake.head[1] > Display.HEIGHT - Display.BLOCK_SIZE:
            return True
        elif self.snake.head[1] < 0:
            return True

        return False