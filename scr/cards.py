class Card:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.image = '{}.png'.format(self.name)
    
    def __repr__(self):
        return '{}({})'.format(self.name, self.power)
    
    def __eq__(self, card):
        return self.name == card.name
    
    def copy(self):
        return Card(self.name, self.power)


Joker = Card('Joker', 0)
Ace = Card('Ace', 1)
Gang = Card('Gang', 2)
Officer = Card('Officer', 3)
Soldier = Card('Soldier', 4)
Killer = Card('Killer', 5)
Capo = Card('Capo', 6)
Don = Card('Don', 7)

CARDS = [Joker, Ace, Gang, Officer, Soldier, Killer, Capo, Don]
