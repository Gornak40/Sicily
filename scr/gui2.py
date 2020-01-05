import pygame as pg
from cards import *
from random import choice, randrange
from results import *
from engine import *


def loadImage(name):
    return pg.transform.rotozoom(pg.image.load('../data/' + name), 0, 0.6)


def render(blackOpen):
    screen.fill(WHITE)
    for i in range(3):
        screen.blit(IMG[redHand[i].name], redRects[i])
    screen.blit(image if not blackOpen else IMG[Game.blackCard.name], blackRect)
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
            if redRects[i].collidepoint(pos):
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
running = True
clock = pg.time.Clock()
pg.display.set_caption('Sicily')
pg.display.set_icon(pg.image.load('../data/icon.png'))

# main loop
blackOpen = False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        update(event)
    render(blackOpen)
    if Game.redScore >= 4 or Game.blackScore >= 4:
        print('{} PLAYER IS THE WINNER'.format('RED' if Game.redScore > Game.blackScore else 'BLACK'))
        running = False

pg.quit()
