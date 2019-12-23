from engine import *
from random import choice, randrange
from results import *
take = lambda arr: arr.pop(randrange(len(arr)))

redCards = CARDS.copy()
blackCards = CARDS.copy()

# traitors turn
redTraitor = take(redCards)
blackTraitor = take(blackCards)
redCards.append(blackTraitor)
blackCards.append(redTraitor)

# making hands
redHand = [take(redCards) for _ in range(3)]
blackHand = [take(blackCards) for _ in range(3)]
Game = Game()

# game process
while Game.redScore < 4 and Game.blackScore < 4:
    Game.blackCard = take(blackHand)
    blackHand.append(take(blackCards)) if blackCards else None
    print(redHand)
    redNum = int(input())
    ind = [i for i in range(len(redHand)) if redHand[i].power == redNum][0] 
    Game.redCard = redHand.pop(ind)
    redHand.append(take(redCards)) if redCards else None
    fight(Game)
    print('Scores:', Game.redScore, Game.blackScore)
    print('HoldScore:', Game.holdScore)
    print('GangBoosts:', Game.redGangBoost, Game.blackGangBoost)
    print('Boosts:', Game.redBoost, Game.blackBoost)
    print()

# results
print('{} PLAYER IS THE WINNER'.format('RED' if Game.redScore > Game.blackScore else 'BLACK'))







