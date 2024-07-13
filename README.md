# OOP-Based_Blackjack_Simulation
In this project, we developed a fully functional Blackjack game using Python and Object-Oriented Programming (OOP) principles. The game was designed with modularity in mind, breaking down the functionality into separate Python files for better organization and maintainability. The components of the game include:

- **Card.py:** The `Card` class in the `card.py` file is a crucial component of a blackjack game, representing individual playing cards with attributes for rank, suit, and visibility. It includes methods for initializing cards, displaying them in an ASCII art format, and comparing them based on rank and suit. Additionally, it allows toggling the card's visibility, affecting how it is represented in string and tuple-like formats. 
- **Deck.py:** The `Deck` class in the `deck.py` file represents a standard deck of 52 playing cards for a blackjack game. It initializes the deck with cards sorted in ascending order of rank and suit. The class provides methods to shuffle the deck using different shuffling techniques, such as modified overhand and Mongean shuffles, and to deal cards to a player's hand by transferring the top card of the deck to the specified hand. The class also includes methods for retrieving the current list of cards in the deck and features doctests to demonstrate and verify its functionality.
- **Hand.py:** Represents a player's hand of cards, allowing for operations such as adding a card and calculating the hand's value.
- **Shuffle.py:** Handles the shuffling logic for the deck.

These components were then integrated into the main game logic within `blackjack.py`, ensuring clear separation of concerns and easy readability. The use of OOP allowed us to create a clean and efficient codebase, making the game extensible and easy to understand.
