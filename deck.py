from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    """

    # Class Attribute(s)

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        suit_lst = ['clubs', 'diamonds', 'hearts', 'spades']
        rank_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J','Q', 'K', 'A']
        self.cards = [Card(rank, suit) for rank in rank_lst for suit in suit_lst]

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        if len(shuffle_and_count) == 1:
            if shuffle_and_count.keys()[0] == 'modified_overhand':
                self.cards = Shuffle.modified_overhand(self.cards, shuffle_and_count['modified_overhand'])
            elif shuffle_and_count.keys()[0] == 'mongean':
                for time in range(shuffle_and_count['mongean']):
                    self.cards = Shuffle.mongean(self.cards)

        if len(shuffle_and_count) > 1:
            self.cards = Shuffle.modified_overhand(self.cards, shuffle_and_count['modified_overhand'])
            for time in range(shuffle_and_count['mongean']):
                    self.cards = Shuffle.mongean(self.cards)
            
            
            
        

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.car
        """
        
        assert isinstance(hand, PlayerHand)
        

        store = self.cards[0]
        self.cards.remove(self.cards[0])
        hand.add_card(store)

    def get_cards(self): 
        return self.cards
