import pygame as pg
from cards import *
from random import choice, randrange
from results import *


def loadImage(name):
    return pg.transform.rotozoom(pg.image.load('../data/' + name), 0, 0.6)


def render():
    screen.fill(WHITE)
    for i in range(3):
        screen.blit(IMG[redHand[i].name], redRects[i])
    screen.blit(IMG[Game.blackCard.name], blackRect)
    pg.display.flip()
    pg.display.update()
    clock.tick(FPS)


def update(event):
    if event.type == pg.MOUSEBUTTONDOWN:
        pos = event.pos
        for i in range(3):
            if redRects[i].collidepoint(pos):
                print(redHand[i])


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
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        card = update(event)
    
    render()

pg.quit()
