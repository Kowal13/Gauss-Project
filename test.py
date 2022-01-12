import pygame
import snake

def run(screen=None):
    print('[menu] run')

    if not screen:
        pygame.init()
        screen = pygame.display.set_mode((800,600))

    mainloop(screen)

def mainloop(screen):
    print('[menu] mainloop')

    running = True
    while running:

        print('running menu ...')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() # skip rest of code
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    snake.main()  # run game

        screen.fill((255,0,0))
        pygame.display.flip()

run()
