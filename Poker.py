import random

card_order_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13,
                   "A": 14}  # stores rank of each card value
suits = ['C', 'H', 'A', 'S']  # All possible suits C-Clubs,H-Hearts,A-Ace,S-Spades, CHASed order is used as a nod for
# my fellow magic enthusiasts
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # All possible values
drawn_cards = []  # list to store all drawn cards
table_cards = []  # list of table cards
Player_Dict = {}  # used to keep of players hand


# Generates unique card
def generate_card():
    card = random.choice(suits) + '-' + random.choice(values)  # Generates card
    while card in drawn_cards:  # continuously loops until Unique card is generated
        card = random.choice(suits) + '-' + random.choice(values)
    else:
        drawn_cards.append(card)  # Appends generated card to list used to check uniqueness
    return card


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


# Checks Flush - 5 cards of same suit returns list of players with flush hand
def check_flush(number_of_players):
    list_of_flush = []  # maintains list of player with active Flush hand
    for i in range(1, int(number_of_players) + 1):
        hand = table_cards + Player_Dict[f'Player{i}']  # combines table and hand cards
        flush = [h[0] for h in hand]  # strips suits from hand
        if flush.count('C') == 5 or flush.count('H') == 5 or flush.count('A') == 5 or flush.count(
                'S') == 5:  # condition checks count of each suit to confirm Flush
            list_of_flush += [f'Player{i}']
    return list_of_flush


# Checks Straight - 5 cards in order returns list of players with straight hands
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

# Checks Straight Flush - 5 cards of same suit in order returns list of player with straight flush hands
def check_straight_flush(number_of_players):
    list_of_straight_flush = []  # maintains list of player with straight flush
    # uses check_straight and check_flush to find intersection between the two
    if check_flush(number_of_players) and check_straight(number_of_players):
        temp = set(check_flush(number_of_players))
        intersect = temp.intersection(check_straight(number_of_players))
        list_of_straight_flush += intersect
    return list_of_straight_flush

# Checks for Royal Flush - rank values of 10,J,Q,K,A with the same suit
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

# Checks for Four of a Kind - 4 cards with same rank
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

#  Checks for full house - Three of a kind and a pair
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

#  Checks for Three of a kind - Three cards with same rank value
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

#  Checks for two Pair - two sets of two cards with same rank value
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

#  Checks for Pair - two cards with same rank value
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

#  Checks for HighCard - card with highest rank value
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

#  uses all the above check functions to determine winner of current round
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


# driver
table_hand()
player_hand(7)
print(table_cards)
print(Player_Dict)
print('Royal Flush' + str(check_royal_flush(7)))
print('Straight Flush' + str(check_straight_flush(7)))
print('Four Of A Kind' + str(check_four_of_a_kind(7)))
print('Full House ' + str(check_full_house(7)))
print('Flush' + str(check_flush(7)))
print('Straight' + str(check_straight(7)))
print('Three Of A Kind' + str(check_three_of_kind(7)))
print('Two Pair' + str(check_two_pair(7)))
print('Pair' + str(check_pair(7)))
print('HighCard' + str(check_highcard(7, Player_Dict.keys())))
print('Winner -->' + str(determine_winner(7)))
