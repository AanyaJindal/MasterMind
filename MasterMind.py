import pygame

pygame.init()

DISPLAY_WIDTH = 550
DISPLAY_HEIGHT = 700

# balls till now
guesses = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# pegs till now
results = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# current selection of balls
current_guesses = [0, 0, 0, 0]
# the specific all selected
current_ball = 0
# to maintain the number of turns till now
turn = 0

#         R    G    B
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)
GRAY  = (169, 169, 169)

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
pygame.display.set_caption("MASTERMIND");
clock = pygame.time.Clock()

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

    pygame.draw.rect(game_display, GRAY, (350, 510, 120, 30))

def click_ball(idx):
    global current_ball
    current_ball = idx
    print("click_ball")
    print(idx)

def click_slot(idx):
    global current_ball
    if current_ball != 0:
        current_guesses[idx-1] = current_ball
        current_ball = 0
        print("click_slot")
        print(idx)

def click_submit():
    global current_guesses
    global guesses
    global results
    global turn
    global answer
    global current_ball
    black_pegs = 0
    white_pegs = 0
    freq_temp = [0, 0, 0, 0, 0, 0, 0]
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
    while black_pegs != 0:
        results[turn][j] = 2
        black_pegs -= 1
        j += 1
    while white_pegs != 0:
        results[turn][j] = 1
        white_pegs -= 1
        j += 1

    turn += 1
    current_ball = 0
    current_guesses = [0, 0, 0, 0]

def mouse_click(mx, my):

    if my >= 510 and my <= 540 and mx >= 350 and mx <= 470:
        click_submit()

    # my is 500 (click_slot)
    elif my >= 500 and my <= 550:
        x = 50
        for i in range(1, 5):
            if mx >= x and mx <= x+50:
                click_slot(i)
                return
            x += 50

    # my is 600 (click_ball)
    elif my >= 600 and my <= 650:
        x = 50
        for i in range(1, 7):
            if mx >= x and mx <= x+50:
                click_ball(i)
                return
            x += 50


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            print(mx)
            print(my)
            mouse_click(mx, my)

    game_display.fill(WHITE)
    draw_board()
    pygame.display.flip()
    clock.tick(60)






    