from constants import *
import pygame
from math import floor
DA = 1 # diffusion a
DB = 0.5 # diffusion b
feedRate = 0.055
killRate = 0.062
positive_infinity = float('inf')

class Cell:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        self.value = 0
    def update(self, a, b, grid, x, y, delta_time):
        self.a = (a + (DA * LaplaceA(grid, x, y)) - (a * b * b) + (feedRate * (1 - a)) )
        self.b = (b + (DB * LaplaceB(grid, x, y)) + (a * b * b) - ((killRate + feedRate) * b) )
    def Draw(self, x, y, screen):
        try:
            self.value = int(min((max(self.a - self.b, 0) * 255, 255)))
        except:
            pass
        pygame.draw.rect(screen, (self.value, self.value, self.value), [x * cell_size, y * cell_size, cell_size, cell_size])

def LaplaceA(grid, x, y):
    s = 0
    s += grid[x][y].a * -1
    s += grid[x-1][y].a * 0.2
    s += grid[x+1][y].a * 0.2
    s += grid[x][y-1].a * 0.2
    s += grid[x][y+1].a * 0.2
    s += grid[x-1][y-1].a * 0.05
    s += grid[x+1][y+1].a * 0.05
    s += grid[x-1][y+1].a * 0.05
    s += grid[x+1][y-1].a * 0.05
    return s
def LaplaceB(grid, x, y):
    s = 0
    s += grid[x][y].b * -1
    s += grid[x-1][y].b * 0.2
    s += grid[x+1][y].b * 0.2
    s += grid[x][y-1].b * 0.2
    s += grid[x][y+1].b * 0.2
    s += grid[x-1][y-1].b * 0.05
    s += grid[x+1][y+1].b * 0.05
    s += grid[x-1][y+1].b * 0.05
    s += grid[x+1][y-1].b* 0.05
    return s
