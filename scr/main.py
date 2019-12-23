from engine import *
from random import choice
from results import *
enemy = CARDS.copy()
me = CARDS.copy()
Game = Game()
while Game.redScore < 4 and Game.blackScore < 4:
    Game.blackCard = choice(enemy)
    Game.redCard = me[int(input())]
    fight(Game)
    print('Scores:', Game.redScore, Game.blackScore)
    print('HoldScore:', Game.holdScore)
    print('GangBoosts:', Game.redGangBoost, Game.blackGangBoost)
    print('Boosts:', Game.redBoost, Game.blackBoost)
    print()