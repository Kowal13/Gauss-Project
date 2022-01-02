
import pygame
from Display import Display
from Avatar import Snake
from Food import Apple

import torch

# tuple1 = (1, 2, "3")
# tuple2 = (1, 2, "4")
# print(tuple1[0] == tuple2[0] and tuple1[1] == tuple2[1])
# s = Snake()
# a = Apple()
# #s.move("right", s, a)
# print(s.get_mask()[0])
# print(a.get_mask()[0])
# print(s.food_eaten(s, a))
# print(s.get_mask()[0][0] == a.get_mask()[0][0] and s.get_mask()[0][1] == a.get_mask()[0][1])


s = Snake()

print(s.head)
print(s.body)
print(s.head in s.body[1:])

print(s.get_mask())