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

# balls till now
guesses = [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# pegs till now
results = [[2, 2, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# current selection of balls
current_guesses = [1, 2, 4, 6]
# the specific all selected
current_ball = 0
# to maintain the number of turns till now
turn = 0

# computer choses randomly for player to enjoy
answer = [1, 4, 2, 5]
freq_ans = [0, 0, 0, 0, 0, 0, 0]
for i in range(len(answer)):
    freq_ans[answer[i]] += 1

def draw_board():
    y = 50

    # for filling the status of game till now
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

    # for filling the slots
    for i in range(len(current_guesses)):
        game_display.blit(ball[current_guesses[i]], (x, y))
        x += 50
    y += 100
    x = 50

    # for filling the balls of selection
    for i in range(6):
        game_display.blit(ball[i+1], (x, y))
        x += 50

def click_ball(idx):
    current_ball = idx

def click_slot(idx):
    if current_ball != 0:
        current_guesses[idx] = current_ball
        current_ball = 0

def click_submit():
    black_pegs = 0
    white_peg = 0
    freq_temp = [0, 0, 0, 0, 0, 0, 0 ]
    for i in range(len(current_guesses)):
        freq_temp[current_guesses[i]] += 1;
        if current_guesses[i] == 0:
            # display prompt
            return
        if current_guesses[i] == answer[i]:
            black_pegs += 1
    for i in range(1, 7):
        white_pegs += min(freq_temp[i], freq_ans[i])
    white_pegs -= black_pegs

    # if black_pegs == 4:
    #     # display "WIN"

    # updating current_guesses (status of balls)
    for i in range(len(current_guesses)):
        guesses[turn][i] = current_guesses[i]

    # updating results (status of pegs)
    j = 0
    while black_pegs:
        results[turn][j] = 2
        black_pegs -= 1
        j += 1
    while white_pegs:
        results[turn][j] = 1
        white_pegs -= 1
        j += 1

    turn += 1
    current_ball = 0
    current_guesses = [0, 0, 0, 0]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    game_display.fill(WHITE)
    draw_board()
    pygame.display.flip()
    clock.tick(60)



    