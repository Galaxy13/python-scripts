import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_image = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

TILE_SIZE = (72, 96)
TILE_CENTER = (36, 48)
tile_image = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:
    def __init__(self, suit, rank):
        self.exposed = True
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ('Invalid card rank: ', suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def is_exposed(self):
        return self.exposed

    def cover(self):
        self.exposed = False

    def expose(self):
        self.exposed = True

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if self.exposed:
            canvas.draw_image(card_image, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)
        else:
            canvas.draw_image(tile_image, TILE_CENTER, TILE_SIZE, [pos[0] + TILE_CENTER[0], pos[1] + TILE_CENTER[1]],
                              TILE_SIZE)

class Hand:
    def __init__(self):
        self.hand_cards = []

    def add_card(self, card):
        self.hand_cards.append(card)

    def cards(self):
        return self.hand_cards

    def get_value(self):
        summ = 0
        count = 0
        for card in self.hand_cards:
            summ += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                count += 1
        if count == 1:
            summ += 10
        return summ

    def draw(self, canvas, pos):
        for card in self.hand_cards:
            card.draw(canvas, pos)
            pos[0] += 50

class Deck:
    def __init__(self):
        self.cards_deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards_deck.append(Card(suit, rank))

    def __str__(self):
        return str(self.cards_deck)

    # def card(self):
    #     return self.cards_deck[0].rank

    def shuffle(self):
        random.shuffle(self.cards_deck)

    def deal_card(self):
        card = self.cards_deck[0]
        self.cards_deck.pop(0)
        return card

def draw_handler(canvas):
    player.draw(canvas, [200, 300])
    dealer.draw(canvas, [200, 100])
    canvas.draw_text(str(player.get_value()), [50, 300], 30, 'White')
    canvas.draw_text(str(dealer.get_value()), [50, 100], 30, 'White')

def deal():
    global deck, player, dealer
    deck = Deck()
    deck.shuffle()
    player, dealer = Hand(), Hand()
    i = 2
    while i != 0:
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        i -= 1
    dealer.cards()[0].cover()
    if player.get_value() == 21:
        stand()

def hit():
    global player, deck
    player.add_card(deck.deal_card())
    if player.get_value() >= 21:
        stand()

def stand():
    global dealer, deck
    dealer.cards()[0].expose()
    if player.get_value() <= 21:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
    else:
        print ('Dealer wins!')
        return
    if dealer.get_value() < player.get_value() and player.get_value() <= 21 or dealer.get_value() > 21:
        print ('Player wins!')
    elif dealer.get_value() <= 21:
        print ('Dealer wins!')


# deck = Deck()
# deck.shuffle()
# deck.deal_card()
# player = Hand()
# i = 3
# while i != 0:
#     player.add_card(deck.deal_card())
#     i -= 1

frame = simplegui.create_frame("BlackJack", 600, 600)
frame.set_canvas_background("Green")
frame.set_draw_handler(draw_handler)
frame.add_button('Deal', deal, 100)
frame.add_button('Hit', hit, 100)
frame.add_button('Stand', stand, 100)

deal()
frame.start()


