from cards import Cards
import random

class Play(Cards):
    
    def __init__(self, players=1):
        self.players = players
        super().__init__()
        
    def deal(self, players=1, cards=1):
        random.shuffle(self.deck)
        #initial = self.deck
        self.hands = [self.deck[i:players*cards:players]
                        for i in range(players)]
        return self.hands
        

