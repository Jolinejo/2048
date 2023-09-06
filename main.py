import pygame
from mods.consts import WIDTH, HEIGHT, C1, C2, C3, C4
from mods.board import Board
from player import Player

pygame.init()

player1 = Player()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Empire's 2048")


font = pygame.font.SysFont("Monospace", 32, bold=True) #font style
newGame = pygame.Rect((10, 10, 50, 50))
text = font.render("New Game", True, 'white')

button = pygame.Rect(50, 40, 160, 50)
box1 = pygame.Rect(255, 40, 90, 50)
box2 = pygame.Rect(360, 40, 90, 50)

click = 0 #current score
best = player1.get_best() #best score
new = 0 #temp

def run_game():
    global click, best, new
    run = True
    board = Board()
    score = font.render("%d" %(click), True, 'white')
    bestS = font.render("%d" %(best), True, 'white')

    while run:

        pygame.time.delay(100)
        
        score = font.render("%d" %(click), True, 'white')
        bestS = font.render("%d" %(best), True, 'white')
        board.draw_cubes(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(event.pos):
                pygame.time.delay(10)
                click += 1
                new = max(best, click)
                best = new
                
        pygame.draw.rect(WIN, '#5c381c', button)

        WIN.blit(text, (button.x+5, button.y+5))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_UP]:
            pass
        elif keys[pygame.K_DOWN]:
            pass
        pygame.draw.rect(WIN, '#1c5c2f', box1)
        pygame.draw.rect(WIN, '#1c5c2f', box2)
        WIN.blit(score, (box1.x+35, box1.y+7))
        WIN.blit(bestS, (box2.x+35, box2.y+7))
        pygame.display.update()
    player1.write(best)    
    pygame.quit()

if __name__ == "__main__":
    run_game()

