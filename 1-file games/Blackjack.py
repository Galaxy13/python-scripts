### Mini Project of Week #2 ###
### Blackjack ###
### The purpouse of this project, is to implement this simple game, using object programming
# As some external things, I've used: background image, bet system (very simple)
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

# uploading background image
TABLE = simplegui.load_image(
    "https://www.dropbox.com/s/h4ol6hlkasogwva/360_F_93364974_eoos8QGsa9CzTa5hGRRL6EutXMSKgdOA.jpg?dl=1")

# global variable for text in center of canvas
CENTER_TEXT = 'Make your bet!'


class Card:
    def __init__(self, suit, rank):
        self.exposed = True
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print('Invalid card rank: ', suit, rank)

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
        self.is_played = False

    def add_card(self, card):
        self.hand_cards.append(card)

    def cards(self):
        return self.hand_cards

    def get_value(self):
        sum = 0
        count = 0
        for card in self.hand_cards:
            sum += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                count += 1
        if count == 1 and sum + 10 <= 21:
            sum += 10
        return sum

    def cover(self):
        for card in self.hand_cards:
            card.cover()

    def expose(self):
        for card in self.hand_cards:
            card.expose()

    def is_played(self):
        return self.is_played

    def played(self):
        self.is_played = True

    def new_game(self):
        self.is_played = False

    def draw(self, canvas, pos):
        for card in self.hand_cards:
            card.draw(canvas, pos)
            pos[0] += 50


# external class for implementing bet system
class Balance:
    def __init__(self, start_balance):
        self.balance = start_balance
        self.bet = 0
        self.is_bet = False

    def add(self):
        self.balance += self.bet * 2

    def set_bet(self, bet):
        self.bet = bet

    def make_bet(self):
        self.is_bet = True
        self.balance -= self.bet

    def new_bet(self):
        self.is_bet = False

    def is_bet(self):
        return self.is_bet

    def increase_bet(self, bet):
        self.bet += bet

    def decrease_bet(self, bet):
        self.bet -= bet

    def current_balance(self):
        return self.balance

    def current_bet(self):
        return self.bet

    def __str__(self):
        return str(self.balance)


class Deck:
    def __init__(self):
        self.cards_deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards_deck.append(Card(suit, rank))

    def __str__(self):
        return str(self.cards_deck)

    def shuffle(self):
        random.shuffle(self.cards_deck)

    def deal_card(self):
        card = self.cards_deck[0]
        self.cards_deck.pop(0)
        return card


def draw_handler(canvas):
    player.draw(canvas, [200, 360])
    dealer.draw(canvas, [200, 100])
    if player_balance.is_bet or player.is_played:
        canvas.draw_text(str(player.get_value()), [50, 400], 30, 'White')
    if player.is_played:
        canvas.draw_text(str(dealer.get_value()), [50, 100], 30, 'White')
    canvas.draw_text('Balance: ' + str(player_balance.current_balance()), [400, 50], 30, 'White')
    canvas.draw_text('Bet: ' + str(player_balance.current_bet()), [400, 500], 30, 'White')
    canvas.draw_text(CENTER_TEXT, [170, 275], 40, 'White', 'serif')


def deal():
    global deck, player, dealer, player_balance, CENTER_TEXT
    if player_balance.is_bet:
        player.expose()
        dealer.cards()[1].expose()
        if player.get_value() == 21:
            stand()
            CENTER_TEXT = 'Player wins! Press "Deal" to restart'
    else:
        CENTER_TEXT = 'Make your bet!'
        player_balance.set_bet(50)
        deck = Deck()
        deck.shuffle()
        player, dealer = Hand(), Hand()
        player.new_game()
        i = 2
        while i != 0:
            player.add_card(deck.deal_card())
            dealer.add_card(deck.deal_card())
            i -= 1
        player.cover()
        dealer.cover()


def hit():
    global player, deck
    if player.is_played or not player_balance.is_bet:
        return
    player.add_card(deck.deal_card())
    if player.get_value() >= 21:
        stand()


def stand():
    global dealer, deck, player, CENTER_TEXT
    if player.is_played or not player_balance.is_bet:
        return
    player.played()
    dealer.cards()[0].expose()
    if player.get_value() <= 21:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
    else:
        print('Dealer wins! Press "Deal" to restart')
        CENTER_TEXT = 'Dealer wins! Press "Deal" to restart'
        player_balance.new_bet()
        return
    if dealer.get_value() < player.get_value() <= 21 or dealer.get_value() > 21:
        print('Player wins! Press "Deal" to restart')
        CENTER_TEXT = 'Player wins! Press "Deal to restart'
        player_balance.add()
    elif dealer.get_value() <= 21:
        print('Dealer wins! Press "Deal" to restart')
        CENTER_TEXT = 'Dealer wins! Press "Deal" to restart'
    player_balance.new_bet()


# below here are some external buttons for bet system
# as number to increment of decrement bet, i've used number 50
def increase_bet():
    global player_balance, player, CENTER_TEXT
    if player_balance.is_bet or player.is_played:
        return
    if player_balance.current_balance() <= player_balance.current_bet():
        CENTER_TEXT = 'Not enough balance'
    else:
        player_balance.increase_bet(50)
        CENTER_TEXT = 'Make your bet!'


def decrease_bet():
    global player_balance, CENTER_TEXT
    if player_balance.is_bet or player.is_played:
        return
    if player_balance.current_bet() == 50:
        CENTER_TEXT = "Your bet can't be zero!"
    else:
        player_balance.decrease_bet(50)
        CENTER_TEXT = 'Make your bet!'


def bet():
    global player_balance, CENTER_TEXT
    if player_balance.is_bet or player.is_played:
        return
    player_balance.make_bet()
    deal()
    CENTER_TEXT = 'Hit or stand?'


frame = simplegui.create_frame("BlackJack", 800, 534)
frame._set_canvas_background_image(TABLE)
frame.set_draw_handler(draw_handler)
frame.add_button('Deal', deal, 100)
frame.add_button('Hit', hit, 100)
frame.add_button('Stand', stand, 100)
frame.add_button('Increase bet', increase_bet, 150)
frame.add_button('BET', bet, 100)
frame.add_button('Decrease bet', decrease_bet, 150)

# default setting of player's balance
player_balance = Balance(1000)
deal()
frame.start()
