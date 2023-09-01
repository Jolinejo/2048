import pygame
from mods.consts import WIDTH, HEIGHT
from mods.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Empire's 2048")


def run_game():
    run = True
    board = Board()

    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_RIGHT]:
            pass
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        board.draw_cubes(WIN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    run_game()