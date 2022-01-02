import pygame

class Display():
    WIDTH, HEIGHT = 640, 480
    WHITE = (255, 255, 255)
    RED = (200,0,0)
    BLACK = (0,0,0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    BLOCK_SIZE = 20    

    def __init__(self):
        pygame.init()
        # def width and height of the display window
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # caption name
        pygame.display.set_caption("Snake")
    
    def update(self, avatar, food, background = None):
        # if background is None:
        #     background = self.WHITE

        self.display.fill(self.WHITE)
        for el in avatar.body:
            pygame.draw.rect(self.display, self.GREEN, pygame.Rect(el[0], el[1], self.BLOCK_SIZE, self.BLOCK_SIZE))

        pygame.draw.rect(self.display, self.DARK_GREEN, pygame.Rect(avatar.head[0], avatar.head[1], self.BLOCK_SIZE, self.BLOCK_SIZE))

        for el in food:
            pygame.draw.rect(self.display, self.RED, pygame.Rect(el.location[0], el.location[1], self.BLOCK_SIZE, self.BLOCK_SIZE))
        
        pygame.display.flip()