class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        
        """
        self.rank = rank
        self.suit = suit
        self.visible = True
        

    def __lt__(self, other_card):
        suit_lst = ['clubs', 'diamonds', 'hearts', 'spades']
        rank_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', \
                    'Q', 'K', 'A']
        if int(rank_lst.index(self.rank)) != int(rank_lst.index(other_card.rank)):
            return int(rank_lst.index(self.rank)) < \
                   int(rank_lst.index(other_card.rank))
        else:
            return int(suit_lst.index(self.suit)) < \
                   int(suit_lst.index(other_card.suit))
        
        
        


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """

        if self.visible == True:
            
            if self.suit == 'hearts':
                symbol = '♥'
            elif self.suit == 'spades':
                symbol = '♠'
            elif self.suit == 'clubs':
                symbol = '♣'
            elif self.suit == 'diamonds':
                symbol = '♦'
            rank_dis = self.rank

            
        else:
            symbol = '?'
            rank_dis = '?'
            

        return 4 * '_' + '\n' + '|' + str(rank_dis) + 2 * ' ' + '|' + \
               '\n' + '|' + ' ' + str(symbol) + ' ' + '|' + '\n' + '|' + \
               '__' + str(rank_dis) + '|'

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """

        if self.visible == True:
            return '('+str(self.rank)+', '+str(self.suit)+')'
        elif self.visible == False:
            return '(?, ?)'
            

 
        

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
        

    def set_visible(self, visible):
        assert isinstance(visible,bool)
        self.visible = visible
        
    
