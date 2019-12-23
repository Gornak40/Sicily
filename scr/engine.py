from cards import *
from results import *


def fight(Game):
    red = Game.redCard.copy()
    black = Game.blackCard.copy()
    
    # Capo Spec
    red.power += Game.redBoost * 2
    black.power += Game.blackBoost * 2
    print(red, 'vs', black)
    
    # Killer Spec
    redSpec = black != Killer
    blackSpec = red != Killer
    
    # Soldier Spec
    redScore = 1 + redSpec * (red == Soldier)
    blackScore = 1 + blackSpec * (black == Soldier)
    
    # Gang Spec
    Game.redGangBoost = redSpec * (red == Gang)
    Game.blackGangBoost = blackSpec * (black == Gang)
    
    # Capo Spec
    Game.redBoost = redSpec * (red == Capo)
    Game.blackBoost = blackSpec * (black == Capo)
    
    # Draw situation
    if redSpec and red == Joker or blackSpec and black == Joker or red.power == black.power:
        return Game.hold()
    
    # Killer situation
    if not redSpec or not blackSpec:
        return Game.red(1) if red.power > black.power else Game.black(1)
    
    # Ace situation
    if red == Ace and black == Don or black == Ace and red == Don:
        return Game.red(4) if red == Ace else Game.black(4)
    
    # Don situation
    if red == Don and black == Don:
        return Game.red(1) if red.power > black.power else Game.black(1)
    if red == Don:
        return Game.red(1)
    if black == Don:
        return Game.black(1)
    
    # Officer situation
    if red == Officer or black == Officer:
        red.power *= -1
        black.power *= -1
    
    return Game.red(redScore) if red.power > black.power else Game.black(blackScore)
