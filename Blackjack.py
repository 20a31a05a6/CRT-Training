import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = 100
        
    def take_bet(self):
        while True:
            try:
                bet = int(input(f'{self.name}, how many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if bet > self.chips:
                    print(f'Sorry, your bet cannot exceed {self.chips}')
                else:
                    break
        return bet
    
    def hit(self, deck):
        self.hand.add_card(deck.deal())
        self.hand.adjust_for_ace()
        
    def hit_or_stand(self, deck):
        while True:
            x = input(f'{self.name}, would you like to hit or stand? ')
            
            if x[0].lower() == 'h':
                self.hit(deck)
            elif x[0].lower() == 's':
                print(f'{self.name} stands.\n')
                break
            else:
                print('Sorry, I did not understand that. Please enter hit or stand.')
                continue
        
    def show_some(self):
        print(f'{self.name} Cards:')
        for card in self.hand.cards:
            print(card)
            
    def show_all(self):
        print(f'{self.name} Cards:')
        for card in self.hand.cards:
            print(card)
        print(f'Value: {self.hand.value}\n')

def play_game():
    deck = Deck()
