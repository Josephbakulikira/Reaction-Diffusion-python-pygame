import pygame
from event import HandleEvent
from constants import *
from random import uniform
from copy import copy, deepcopy
from cell import *

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

grid = [[Cell(1, 0) for y in range(w)] for x in range(h)]
midx, midy = w//2, h//2
NextFrameGrid = [[Cell(1, 0) for y in range(w)] for x in range(h)]

for x in range(midx - 2, midx + 2):
    for y in range(midy - 2, midy + 2):
        grid[x][y].b = 1

events=[]
run = True
while run:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    frame_rate = clock.get_fps()
    pygame.display.set_caption(str(int(frame_rate)))
    delta_time = clock.tick(fps)/1000


    for x in range(1, w-1):
        for y in range(1, h-1):
            NextFrameGrid[x][y].update(grid[x][y].a, grid[x][y].b, grid, x, y, delta_time)

    for x in range(w):
        for y in range(h):
            grid[x][y].Draw(x, y, screen)

    grid, NextFrameGrid = NextFrameGrid, grid

    run = HandleEvent(events)
    pygame.display.flip()

pygame.quit()
