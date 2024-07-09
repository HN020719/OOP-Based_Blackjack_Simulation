class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        #assert isinstance(cards,list) and isinstance(num,int)
        if num == 0:
            return cards
        else:
            
            if (len(cards) % 2 == 0) and (num % 2 != 0):
                half = int(len(cards)//2)
                top_half = cards[:half]
                second = cards[half:]
                move = top_half[-(num//2 + 1):] + second[:(num//2)] 
                ind1 = len(top_half) - (num//2 + 1)
                cards = move + top_half[:ind1] + (second[(num//2):])
                
            elif (len(cards) % 2 != 0) and (num % 2 == 0):
                middle_ind = len(cards) // 2                
                ind1 = middle_ind - int(num / 2)
                ind2 = middle_ind + int(num / 2)
                move = cards[ind1:ind2]
                cards = move + cards[:ind1] + cards[ind2:]
                
            elif (len(cards) % 2 == 0) and (num % 2 == 0):
                middle_ind = len(cards) // 2 
                ind1 = middle_ind - int(num / 2) 
                ind2 = middle_ind + int(num / 2)
                move = cards[ind1:ind2]
                cards = move + cards[:ind1] + cards[ind2:]
                
            elif (len(cards) % 2 != 0) and (num % 2 != 0):        
                middle_ind = len(cards) // 2
                ind1 = middle_ind - int(num / 2)
                ind2 = middle_ind + int(num / 2) + 1
                move = cards[ind1:ind2]
                cards = move + cards[:ind1] + cards[ind2:]
                
                 
        return Shuffle.modified_overhand(cards, num-1)
		

                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        
        lst = []
        ind = 0
        def func2(cards, ind, lst):
            if len(cards) == 0:
                return lst
            
            else:
                if ind % 2 != 0:
                    lst = [cards[0]] + lst
                    
                    
                elif ind % 2 == 0 :
                    lst += [cards[0]]
                    
                ind += 1
                return func2(cards[1:], ind, lst)
                
        return func2(cards, ind, lst)
        
             
        
    
