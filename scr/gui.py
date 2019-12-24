import pygame as pg
from cards import *
from random import choice


def render():
    screen.fill(WHITE)
    redCardSprite.draw(screen)


def makeSprite(card, x, y):
    sprite = pg.sprite.Sprite()
    sprite.image = loadImage(card.image)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x, sprite.rect.y = x, y
    sprite.card = card
    redCardSprite.add(sprite)


WIDTH, HEIGHT = SIZE = 1200, 800
FPS = 50
WHITE = pg.Color('white')
loadImage = lambda name: pg.transform.rotozoom(pg.image.load('../data/' + name), 0, 0.6)

pg.init()
screen = pg.display.set_mode(SIZE)
running = True
clock = pg.time.Clock()
pg.display.set_caption('Sicily')
pg.display.set_icon(pg.image.load('../data/icon.png'))

redHand = [Capo, Officer, Soldier]
dlt = 30
cardSizeX = loadImage('Joker.png').get_width()
cardSizeY = loadImage('Joker.png').get_height()

x = WIDTH // 2 - cardSizeX * 1.5 - dlt
y = HEIGHT - cardSizeY - dlt
redCardSprite = pg.sprite.Group()
for card in redHand:
    makeSprite(card, x, y)
    x += cardSizeX + dlt

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            for sprite in redCardSprite:
                if sprite.rect.collidepoint(event.pos):
                    print(sprite.card)
                    newSprite = makeSprite(choice(CARDS), sprite.rect.x, sprite.rect.y)
                    redCardSprite.remove(sprite)

    render()
    pg.display.flip()
    pg.display.update()
    clock.tick(FPS)

pg.quit()
