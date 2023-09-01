import pygame
from .consts import x, y, C1, C2, C3, C4, rows, cols, thickness

class Board:
    def __init__(self) -> None:
        self.board = []
        self.full = False
        self.cubes = 2

    def draw_cubes(self, win):
        win.fill(C1)
        points = [(50, 50), (450, 50), (450, 450), (50, 450)]

        for row in range(rows):
            for col in range(cols):

                pygame.draw.rect(win, C3, ((row*x+50), (col*x+50), x, y))
        pygame.draw.lines(win, C4, True, points, thickness)
        for i in range((x+50), (3*x)+51, x):
            pygame.draw.line(win, C4, (i,50), (i, 450), thickness)
        for i in range((x+50), (3*x)+51, x):
            pygame.draw.line(win, C4, (50,i), (450, i), thickness)

                
