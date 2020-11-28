## Introduction:
The app uses random Module to generate, table cards, hands of players and function which can determine winnner of various possible winning condition such as Royal Flush, Four of a kind,Straights etc.I have included comments along with the code

## Setup:
```
card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}  # stores rank of each card value
suits = ['C', 'H', 'A', 'S']  # All possible suits C-Clubs,H-Hearts,A-Ace,S-Spades, CHASed order is used as a nod for
# my fellow magic enthusiasts
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # All possible values
drawn_cards = []  # list to store all drawn cards
table_cards = []  # list of table cards
Player_Dict = {}  # used to keep of players hand
```
We start by creating a card rank dictionary to save the displayed value of the cards to the actual rank of the cards , A can be placed as either 1 or 14 i h
##  How the cards are generated:
*Short Answer: random module* 


### Note: The following App is not indented to be used anywhere and is in noway bug-free enough to be used in app. Its only purpose is as an exercise to improve my understanding of random library and Python fudanmentals.
