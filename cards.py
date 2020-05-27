
class Cards:
    
    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    FACES = ["Ace", "King", "Queen", "Jack", 2,3,4,5,6,7,8,9,10]
    
    def __init__(self):
        self.deck = []
        self.make_deck()
        
    def __str__(self):
        return str(self.deck)
    
    def __repr__(self):
        return f"{self.__class__.__name__} {self.__dict__}"
        
    def make_deck(self, suits=SUITS, faces=FACES):
        for suit in suits:
            for face in faces:
                self.deck.append(str(f"{face} of {suit}"))
                
    
        