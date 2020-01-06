import pygame as pg
from os import startfile
from cards import *
from random import choice, randrange
from results import *
from engine import *


def loadImage(name):
    image = pg.transform.rotozoom(pg.image.load('../data/' + name), 0, 0.6)
    return image


def lastRender():
    if Game.redScore == Game.blackScore:
        color = BLUE
        text = 'DRAW'
    elif Game.redScore > Game.blackScore:
        color = RED
        text = 'RED PLAYER IS THE WINNER'
    else:
        color = BLACK
        text = 'BLACK PLAYER IS THE WINNER'
    screen.fill(color)
    for i in range(len(redHand)):
        screen.blit(IMG[redHand[i].name], redRects[i])
    screen.blit(image if not blackOpen else IMG[Game.blackCard.name], blackRect)
    holdScore = font.render(str(Game.holdScore), True, WHITE)
    redScore = font.render(str(Game.redScore), True, WHITE)
    blackScore = font.render(str(Game.blackScore), True, WHITE)
    result = font1.render(text, True, WHITE)
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
    if Game.redGangBoost and not blackOpen:
        screen.blit(IMG[blackCard.name], blackRect)
    holdScore = font.render(str(Game.holdScore), True, BLUE)
    redScore = font.render(str(Game.redScore), True, RED)
    blackScore = font.render(str(Game.blackScore), True, BLACK)
    text = Game.story if Game.redCard is not None else ''
    result = font1.render(text, True, BLUE)
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


def update(event):
    global blackOpen, blackCard
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
            Game.blackCard = blackCard.copy()
            Game.redCard = redHand.pop(redHand.index(card))
            redHand.append(take(redCards)) if redCards else None
            fight(Game)
            blackCard = take(blackHand) if blackHand else None
            blackHand.append(take(blackCards)) if blackCards else None
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
MAGENTA = pg.Color('magenta')
IMG = dict()
for card in CARDS:
    IMG[card.name] = loadImage(card.image)

dlt = 30
image = loadImage('Back.png')
cardSizeX = image.get_width()
cardSizeY = image.get_height()
cardRect = image.get_rect()
GameC = Game

# rects for pygame
redRects = [image.get_rect() for _ in range(3)]
x = WIDTH // 2 - cardSizeX * 1.5 - dlt
y = HEIGHT - cardSizeY - dlt
for rect in redRects:
    rect.topleft = x, y
    x += cardSizeX + dlt
blackRect = image.get_rect()
blackRect.topleft = WIDTH // 2 - cardSizeX // 2, dlt

# pygame init
pg.init()
screen = pg.display.set_mode(SIZE)
running = True
restart = False
clock = pg.time.Clock()
pg.display.set_caption('Sicily')
pg.display.set_icon(pg.image.load('../data/icon.png'))
font = pg.font.SysFont('arial', 150)
font1 = pg.font.SysFont('arial', 50)

while running:
    
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
    Game = GameC()
    blackCard = take(blackHand)
    blackHand.append(take(blackCards)) if blackCards else None
    blackOpen = False
    gaming = True
    restart = False
    
    # main loop
    while not restart:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                restart = True
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                startfile('..\\data\\rules.pdf')
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                restart = True
            update(event) if gaming else None
        render(blackOpen) if gaming else lastRender()
        if (Game.redScore >= 4 or Game.blackScore >= 4) and gaming:
            print('{} PLAYER IS THE WINNER'.format('RED' if Game.redScore > Game.blackScore else 'BLACK'))
            gaming = False
        if (not redHand and gaming):
            print('DRAW')
            gaming = False

pg.quit()
