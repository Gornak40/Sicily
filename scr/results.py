class Game:
    redCard = blackCard = None
    redScore = blackScore = holdScore = 0
    redGangBoost = blackGangBoost = False
    redBoost = blackBoost = False
    
    def hold(self):
        self.holdScore += 1
        print('hold')
    
    def red(self, plus):
        plus += self.holdScore
        self.redScore += plus
        self.holdScore = 0
        print('red +{}'.format(plus))
    
    def black(self, plus):
        plus += self.holdScore
        self.blackScore += plus
        self.holdScore = 0
        print('black +{}'.format(plus))  
