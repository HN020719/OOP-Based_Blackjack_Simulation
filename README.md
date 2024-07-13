# OOP-Based_Blackjack_Simulation
In this project, we developed a fully functional Blackjack game using Python and Object-Oriented Programming (OOP) principles. The game was designed with modularity in mind, breaking down the functionality into separate Python files for better organization and maintainability. The components of the game include:

- **Card.py:** The `Card` class in the `card.py` file is a crucial component of a blackjack game, representing individual playing cards with attributes for rank, suit, and visibility. It includes methods for initializing cards, displaying them in an ASCII art format, and comparing them based on rank and suit. Additionally, it allows toggling the card's visibility, affecting how it is represented in string and tuple-like formats. 
- **Deck.py:** The `Deck` class in the `deck.py` file represents a standard deck of 52 playing cards for a blackjack game. It initializes the deck with cards sorted in ascending order of rank and suit. The class provides methods to shuffle the deck using different shuffling techniques, such as modified overhand and Mongean shuffles, and to deal cards to a player's hand by transferring the top card of the deck to the specified hand. The class also includes methods for retrieving the current list of cards in the deck and features doctests to demonstrate and verify its functionality.
- **Hand.py:** The `hand.py` file defines two classes, `PlayerHand` and `DealerHand`, for managing hands in a blackjack game. The `PlayerHand` class allows adding multiple cards, sorting them in ascending order, and provides string representations for displaying the cards. The `DealerHand` class inherits from `PlayerHand` and introduces functionality specific to the dealer's hand, such as keeping some cards hidden initially and revealing them later. 
- **Shuffle.py:** The `shuffle.py` file defines the `Shuffle` class, which contains different techniques for shuffling a deck of cards. The class includes methods for two types of shuffles: `modified_overhand` and `mongean`. The `modified_overhand` shuffle takes a specified number of cards from the middle of the deck and moves them to the top, repeatedly decrementing the number of cards moved until it reaches zero. The `mongean` shuffle alternates placing cards at the top and bottom of a new deck, effectively reversing the order of cards in a specific pattern.

These components were then integrated into the main game logic within `blackjack.py`, ensuring clear separation of concerns and easy readability. The use of OOP allowed us to create a clean and efficient codebase, making the game extensible and easy to understand.
