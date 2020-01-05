import pygame as pg
from cards import *
from random import choice, randrange
from results import *
from engine import *


def loadImage(name):
    return pg.transform.rotozoom(pg.image.load('../data/' + name), 0, 0.6)


def lastRender(redWins):
    screen.fill(RED if redWins else BLACK)
    for i in range(len(redHand)):
        screen.blit(IMG[redHand[i].name], redRects[i])
    screen.blit(image if not blackOpen else IMG[Game.blackCard.name], blackRect)
    holdScore = font.render(str(Game.holdScore), True, WHITE)
    redScore = font.render(str(Game.redScore), True, WHITE)
    blackScore = font.render(str(Game.blackScore), True, WHITE)
    winner = 'RED' if redWins else 'BLACK'
    result = font1.render('{} PLAYER IS THE WINNER'.format(winner), True, WHITE)
    holdScoreRect = holdScore.get_rect()
    redScoreRect = redScore.get_rect()
    blackScoreRect = blackScore.get_rect()
    resultRect = result.get_rect()
    x = WIDTH // 2 - cardSizeX - dlt - redScoreRect.width // 2
    y = dlt + cardSizeY // 2 - redScoreRect.height // 2
    redScoreRect.topleft = x, y
    x += dlt * 2 + cardSizeX * 2
    blackScoreRect.topleft = x, y
    x = WIDTH // 2 - resultRect.width // 2
    y = HEIGHT // 2 - resultRect.height // 2
    resultRect.topleft = x, y
    screen.blit(holdScore, holdScoreRect)
    screen.blit(redScore, redScoreRect)
    screen.blit(blackScore, blackScoreRect)
    screen.blit(result, resultRect)
    pg.display.flip()
    pg.display.update()
    clock.tick(FPS)


def render(blackOpen):
    screen.fill(WHITE)
    for i in range(len(redHand)):
        screen.blit(IMG[redHand[i].name], redRects[i])
    screen.blit(image if not blackOpen else IMG[Game.blackCard.name], blackRect)
    holdScore = font.render(str(Game.holdScore), True, BLUE)
    redScore = font.render(str(Game.redScore), True, RED)
    blackScore = font.render(str(Game.blackScore), True, BLACK)
    holdScoreRect = holdScore.get_rect()
    redScoreRect = redScore.get_rect()
    blackScoreRect = blackScore.get_rect()
    x = WIDTH // 2 - cardSizeX - dlt - redScoreRect.width // 2
    y = dlt + cardSizeY // 2 - redScoreRect.height // 2
    redScoreRect.topleft = x, y
    x += dlt * 2 + cardSizeX * 2
    blackScoreRect.topleft = x, y
    screen.blit(holdScore, holdScoreRect)
    screen.blit(redScore, redScoreRect)
    screen.blit(blackScore, blackScoreRect)
    pg.display.flip()
    pg.display.update()
    clock.tick(FPS)


def update(event):
    global blackOpen
    if event.type == pg.MOUSEBUTTONDOWN:
        if blackOpen:
            blackOpen = False
            return
        pos = event.pos
        card = None
        for i in range(3):
            if redRects[i].collidepoint(pos) and i < len(redHand):
                card = redHand[i]
# game process        
        if card is not None:
            blackOpen = True
            Game.blackCard = take(blackHand)
            blackHand.append(take(blackCards)) if blackCards else None
            Game.redCard = redHand.pop(redHand.index(card))
            redHand.append(take(redCards)) if redCards else None
            fight(Game)
            print('Scores:', Game.redScore, Game.blackScore)
            print('HoldScore:', Game.holdScore)
            print()


# const
WIDTH, HEIGHT = SIZE = 1200, 800
FPS = 50
WHITE = pg.Color('white')
BLACK = pg.Color('black')
RED = pg.Color('red')
BLUE = pg.Color('blue')
IMG = dict()
for card in CARDS:
    IMG[card.name] = loadImage(card.image)

dlt = 30
image = loadImage('Back.png')
cardSizeX = image.get_width()
cardSizeY = image.get_height()
cardRect = image.get_rect()

# rects for pygame
redRects = [image.get_rect() for _ in range(3)]
x = WIDTH // 2 - cardSizeX * 1.5 - dlt
y = HEIGHT - cardSizeY - dlt
for rect in redRects:
    rect.topleft = x, y
    x += cardSizeX + dlt
blackRect = image.get_rect()
blackRect.topleft = WIDTH // 2 - cardSizeX // 2, dlt

# game modules
take = lambda arr: arr.pop(randrange(len(arr)))
redCards = CARDS.copy()
blackCards = CARDS.copy()
redTraitor = take(redCards)
blackTraitor = take(blackCards)
redCards.append(blackTraitor)
blackCards.append(redTraitor)
redHand = [take(redCards) for _ in range(3)]
blackHand = [take(blackCards) for _ in range(3)]
Game = Game()
Game.blackCard = choice(CARDS)

# pygame init
pg.init()
screen = pg.display.set_mode(SIZE)
running = gaming = True
clock = pg.time.Clock()
pg.display.set_caption('Sicily')
pg.display.set_icon(pg.image.load('../data/icon.png'))
font = pg.font.SysFont('arial', 150)
font1 = pg.font.SysFont('arial', 50)

# main loop
blackOpen = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        update(event) if gaming else None
    render(blackOpen) if gaming else lastRender(Game.redScore > Game.blackScore)
    if (Game.redScore >= 4 or Game.blackScore >= 4) and gaming:
        print('{} PLAYER IS THE WINNER'.format('RED' if Game.redScore > Game.blackScore else 'BLACK'))
        gaming = False

pg.quit()
