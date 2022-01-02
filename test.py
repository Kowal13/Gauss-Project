import pygame
from Display import Display
from Avatar import Snake
from Food import Apple

s = Snake()
a = Apple()

pygame.init()
d = Display()
print(s.body)
print(s.head)
print(a.location)

while True:
    d.update(s, [a])

