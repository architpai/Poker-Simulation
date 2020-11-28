# Poker Simulation
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
    card = random.choice(suits) + '-' + random.choice(values) 
    while card in drawn_cards: 
        card = random.choice(suits) + '-' + random.choice(values)
    else:
        drawn_cards.append(card) 
    return card

```
The above function generates a card at random using `random.choice()` which takes an iterable as an argument and returns a random choice from the iterable.
the card is generated in the form of "suit-value" Eg: D-10 is 10 of Diamonds.
It then checks for that card in `drawn_cards` if its unique the card is returned else a new card is generated until a unique one is generated.
### Below are its uses:
#### 1.Table hands 
```
# Generates 5 cards for the Table
def table_hand():
    for i in range(0, 5):
        table_cards.append(generate_card())
 ```
#### 2. Player hands
```
# Generates Card for each player
def player_hand(number_of_players):
    if 1 < number_of_players <= 7:  
        for i in range(1, int(number_of_players) + 1):
            Player_Dict[f'Player{i}'] = [generate_card(),
                                         generate_card()] 
    else:
        print("Session could not be formed due to too many or too few players")
```
The Player hands are stored in the `Player_Dict`.
## Check functions:
### 1. Flush
```
def check_flush(number_of_players):
    list_of_flush = []  # maintains list of player with active Flush hand
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']  # combines table and hand cards
        flush = [h[0] for h in hand]  # strips suits from hand
        if flush.count('C') == 5 or flush.count('H') == 5 or flush.count('A') == 5 or flush.count(
                'S') == 5:  # condition checks count of each suit to confirm Flush
            list_of_flush += [f'Player{i}']
    return list_of_flush

```
### 2. Staright 
```
def check_straight(number_of_players):
    list_of_straight = []  # maintains list of player with straight hand
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']  # combines table and hand cards
        straight = [h[2:] for h in hand]  # strips values from hand
        rank_values = [card_order_dict[j] for j in straight]  # creates new list by replacing value with rank
        rank_values = list(set(rank_values))
        rank_values.sort()
        if len(rank_values) > 4:
            # check for 5 consecutive rank values
            for z in range(0, len(rank_values) - 4):
                if rank_values[z + 4] - rank_values[z] == 4:
                    list_of_straight += [f'Player{i}']
                elif rank_values == [2, 3, 4, 5, 14]:  # condition for A 1 2 3 4
                    list_of_straight += [f'Player{i}']
    return list_of_straight

```
### 3. Staright flush
```
def check_straight_flush(number_of_players):
    list_of_straight_flush = []  # maintains list of player with straight flush
    # uses check_straight and check_flush to find intersection between the two
    if check_flush(number_of_players) and check_straight(number_of_players):
        temp = set(check_flush(number_of_players))
        intersect = temp.intersection(check_straight(number_of_players))
        list_of_straight_flush += intersect
    return list_of_straight_flush
```
### 4. Royal flush
```
def check_royal_flush(number_of_players):
    list_of_royal_flush = []
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']
        #  checks for special case of straight flush
        if check_straight_flush(number_of_players):
            rflush = [h[2:] for h in hand]
            rank_values = [card_order_dict[j] for j in rflush]
            rank_values = list(set(rank_values))
            rank_values.sort()
            if len(rank_values) > 4:
                for z in range(0, len(rank_values) - 4):
                    if rank_values[z:z + 5] == [10, 11, 12, 13, 14]:
                        list_of_royal_flush += [f'Player{i}']
    return list_of_royal_flush
```
### 5. Four of a kind
```
def check_four_of_a_kind(number_of_players):
    list_of_four_of_a_kind = []
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']
        four_kind = [h[2:] for h in hand]
        unique = set(four_kind)
        #  checks for count of any card rank to be 4
        for j in unique:
            if four_kind.count(j) == 4:
                list_of_four_of_a_kind += [f'Player{i}']
    return list_of_four_of_a_kind
```
### 6. Full house
```
def check_full_house(number_of_players):
    list_of_full_house = []
    for i in range(1, int(number_of_players) + 1):
        threeofkind = False
        twoofkind = False
        hand = table_cards + Player_Dict[f'Player{i}']
        full_house = [h[2:] for h in hand]
        full_house.sort()
        unique = set(full_house)
        #  separately checks for 2 of a kind and 3 of a kind
        for j in unique:
            if full_house.count(j) == 3:
                threeofkind = True
            elif full_house.count(j) == 2:
                twoofkind = True
        if threeofkind and twoofkind:
            list_of_full_house += [f'Player{i}']
    return list_of_full_house
```
### 7. Three of a kind
```
def check_three_of_kind(number_of_players):
    list_of_three_of_kind = []
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']
        threeofkind = [h[2:] for h in hand]
        unique = set(threeofkind)
        #  checks for count of any card to be three
        for j in unique:
            if threeofkind.count(j) == 3:
                list_of_three_of_kind += [f'Player{i}']
    return list_of_three_of_kind

```
### 8. Two pair
```
def check_two_pair(number_of_players):
    list_of_two_pair = []
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']
        twopair = [h[2:] for h in hand]
        unique = set(twopair)
        counter = 0
        #  checks for count of any card to be two and updates counter
        for j in unique:
            if twopair.count(j) == 2:
                counter += 1
        if counter == 2:
            list_of_two_pair += [f'Player{i}']
    return list_of_two_pair
```
### 9. pair
```
def check_pair(number_of_players):
    list_of_pair = []
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']
        pair = [h[2:] for h in hand]
        unique = set(pair)
        highofcur = 0
        for j in unique:
            if pair.count(j) == 2:
                highofcur = j
        if highofcur:
            list_of_pair += [f'Player{i}']
    return list_of_pair
```
### 10.high card
```
def check_highcard(number_of_players, eligible_player_list):
    highcard = 0
    sec_high_card = 0
    list_of_highcard = []
    eligible_player_dict = {key: Player_Dict[key] for key in eligible_player_list}
    for i in eligible_player_dict:
        hand = eligible_player_dict[i]
        high = [h[2:] for h in hand]
        rank_values = [card_order_dict[j] for j in high]
        temp_highcard = max(rank_values)
        sec_temp_highcard = min(rank_values)
        if temp_highcard > highcard:
            highcard = temp_highcard
            sec_high_card = sec_temp_highcard
            list_of_highcard.clear()
            list_of_highcard += [i]
        elif temp_highcard == highcard:
            if sec_temp_highcard > sec_high_card:
                list_of_highcard.clear()
                list_of_highcard += [i]
    return list_of_highcard

```
## Determination of Winner:
```
def determine_winner(number_of_players):
    list_of_winners = []
    if potent_list := check_royal_flush(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_straight_flush(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_four_of_a_kind(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_full_house(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_flush(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_straight(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_three_of_kind(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_two_pair(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_pair(number_of_players):
        if len(potent_list) == 1:
            list_of_winners = potent_list
        else:
            list_of_winners = check_highcard(number_of_players, potent_list)
    elif potent_list := check_highcard(number_of_players, Player_Dict.keys()):
        list_of_winners = potent_list
    return list_of_winners
```
The function determines a list of winners by checking for each win criteria in order using and `if..elif` ladder.
It checks for all player that won in said criteria and compares thier highcards to determine the winner.
### Note: The following App is not indented to be used anywhere and is in noway bug-free enough to be used in app. Its only purpose is as an exercise to improve my understanding of random library and Python fudanmentals.
