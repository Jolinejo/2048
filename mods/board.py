import pygame
from .consts import x, y, C1, C2, C3, C4, rows, cols, thickness

class Board:
    def __init__(self) -> None:
        self.board = []
        self.full = False
        self.cubes = 2

    def draw_cubes(self, win):
        win.fill(C1)
        points = [(50, 100), (450, 100), (450, 500), (50, 500)]

        for row in range(rows):
            for col in range(cols):

                pygame.draw.rect(win, C3, ((row*x+50), (col*x+100), x, y))
        pygame.draw.lines(win, C4, True, points, thickness)
        for i in range((x+50), (3*x)+51, x):
            pygame.draw.line(win, C4, (i,100), (i, 500), thickness)
        for i in range((x+100), (3*x)+101, x):
            pygame.draw.line(win, C4, (50,i), (450,i),thickness)

                
