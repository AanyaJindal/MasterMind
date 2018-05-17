import pygame

pygame.init()

DISPLAY_WIDTH = 550
DISPLAY_HEIGHT = 700

#         R    G    B
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)

# 0 denotes empty, 1-6 denote different colors
ball = []
ball.append(pygame.image.load('Assets/hole.png'))
ball.append(pygame.image.load('Assets/ball_1.png'))
ball.append(pygame.image.load('Assets/ball_2.png'))
ball.append(pygame.image.load('Assets/ball_3.png'))
ball.append(pygame.image.load('Assets/ball_4.png'))
ball.append(pygame.image.load('Assets/ball_5.png'))
ball.append(pygame.image.load('Assets/ball_6.png'))
fin = pygame.image.load('Assets/final.png')

# 0 denotes empty, 1 denotes white, 2 denotes black
peg = []
peg.append(pygame.image.load('Assets/peg_0.png'))
peg.append(pygame.image.load('Assets/peg_1.png'))
peg.append(pygame.image.load('Assets/peg_2.png'))

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

guesses = [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
results = [[2, 2, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
current_guesses = [1, 2, 4, 6]

def draw_board():
    y = 50
    for i in range(len(guesses)):
        x = 50
        for j in range(len(guesses[i])):
            game_display.blit(ball[guesses[i][j]], (x, y))
            x += 50
        x += 100
        for j in range(len(results[i])):
            game_display.blit(peg[results[i][j]], (x, y))
            x += 30
        y += 50
    y += 50
    x = 50
    for i in range(len(current_guesses)):
        game_display.blit(ball[current_guesses[i]], (x, y))
        x += 50
    y += 100
    x = 50
    for i in range(6):
        game_display.blit(ball[i+1], (x, y))
        x += 50


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    game_display.fill(WHITE)
    draw_board()
    pygame.display.flip()
    clock.tick(60)



    