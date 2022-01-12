import pygame
import pygame_menu


class Display:
    WIDTH, HEIGHT = 640, 480
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    BLOCK_SIZE = 20

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('comicsans', 40)

        # def width and height of the display window
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # caption name
        pygame.display.set_caption("Snake")
    
    def update(self, drawable_list, score):
        self.display.fill(self.BLACK)
        txt = self.font.render("Score:" + str(score), True, self.WHITE)
        self.display.blit(txt, [0, 0])

        for d in drawable_list:
            mask_list = d.get_mask()
            for el in mask_list:
                pygame.draw.rect(self.display, el[2], pygame.Rect(el[0], el[1], self.BLOCK_SIZE, self.BLOCK_SIZE))

        pygame.display.flip()

