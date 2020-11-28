## Introduction:
The app uses random Module to generate, table cards, hands of players and function which can determine winnner of various possible winning condition such as Royal Flush, Four of a kind,Straights etc.I have included comments along with the code

## Setup:
```
card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}  
suits = ['C', 'H',  'S', 'D']  
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  
drawn_cards = []  
table_cards = [] 
Player_Dict = {}  
```
We start by creating a card rank dictionary to save the displayed value of the cards to the actual rank of the cards , A can be placed as either 1 or 14 ,I put it as 14.
Next are 2 lists with saved the various possible suits and card values.`drawn_cards` saves the cards generated and helps with avoiding duplicates.
`table_cards` saves the table cards for said hand and `Player_Dict` is a dictionary of all the players hand stored as {"Player{n}":[*hand*]}.
##  How the cards are generated:
*Short Answer: random module* 
```
def generate_card():
    card = random.choice(suits) + '-' + random.choice(values)  # Generates card
    while card in drawn_cards:  # continuously loops until Unique card is generated
        card = random.choice(suits) + '-' + random.choice(values)
    else:
        drawn_cards.append(card)  # Appends generated card to list used to check uniqueness
    return card

```
The above function generates a card at random using `random.choice()` which takes an iterable as an argument and returns a random choice from the iterable.
the card is generated in the form of "suit-value" Eg: A-10 is 10 of 
# Generates 5 cards for the Table
def table_hand():
    for i in range(0, 5):
        table_cards.append(generate_card())


# Generates Card for each player
def player_hand(number_of_players):
    if 1 < number_of_players <= 7:  # condition to check player count is atleast 2 and less than equal to 8
        for i in range(1, int(number_of_players) + 1):
            Player_Dict[f'Player{i}'] = [generate_card(),
                                         generate_card()]  # Appends Each Players Hand to dict
    else:
        print("Session could not be formed due to too many or too few players")
### Note: The following App is not indented to be used anywhere and is in noway bug-free enough to be used in app. Its only purpose is as an exercise to improve my understanding of random library and Python fudanmentals.
