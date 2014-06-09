#!/usr/bin/python
import random
import operator
import copy

# Variables
drawn_cards = []
player_scores = []
high_card_win = 0
players_count = 7
number_of_cards = 5
global_player_tracker = []
global_player_hands = []
temp_global_player_hands = []

# Lookups

hand_rank = {
    9: 'Straight Flush',
    8: 'Four of a kind',
    7: 'Full house',
    6: 'Flush',
    5: 'Straight',
    4: '3 of a kind',
    3: 'Two Pair',
    2: 'Pair',
    1: 'High Card',
    0: 'Nothing'
    }

card_rank = {
    14: 'Ace',
    13: 'King',
    12: 'Quenn',
    11: 'Jack',
    10: 'Ten',
    9: 'Nine',
    8: 'Eight',
    7: 'Seven',
    6: 'Six',
    5: 'Five',
    4: 'Four',
    3: 'Three',
    2: 'Two',
}
    


# Classes

class Card(object):

    suit = ""
    rank = 0
    
    def __init__(self, number):
        
        if (number < 13):
            self.suit = "Spades"
        elif (number > 12) and (number < 26):
            self.suit = "Clubs"
        elif (number > 25) and (number < 39):
            self.suit = "Diamonds"
        else:
            self.suit = "Hearts"

        if (number in [0,13,26,39]):
            self.rank = 2
        elif (number in [1,14,27,40]):
            self.rank = 3
        elif (number in [2,15,28,41]):
            self.rank = 4
        elif (number in [3,16,29,42]):
            self.rank = 5
        elif (number in [4,17,30,43]):
            self.rank = 6
        elif (number in [5,18,31,44]):
            self.rank = 7
        elif (number in [6,19,32,45]):
            self.rank = 8
        elif (number in [7,20,33,46]):
            self.rank = 9
        elif (number in [8,21,34,47]):
            self.rank = 10
        elif (number in [9,22,35,48]):
            self.rank = 11
        elif (number in [10,23,36,49]):
            self.rank = 12
        elif (number in [11,24,37,50]):
            self.rank = 13
        else:
            self.rank = 14

# Functions
def straight_flush(hand):
    if straight(hand) and flush(hand):
        return True

def straight_flush_draw(hands):

    players_hands = []
    players_hands = hands
    players_straight_rank = []
    temp_card_store = []
    highest_rank = 0
    counter = 0
    draw_result = []
    global high_card_win
    output = ""
    
    for i in range(len(players_hands)):

        temp_card_store[:] = []
        
        for ii in range(len(players_hands[i])):
            temp_card_store.append(players_hands[i][ii].rank)

        players_straight_rank.append(max(temp_card_store))

    highest_rank = max(players_straight_rank)
    high_card_win = highest_rank

    for iii in range(len(players_straight_rank)):
        if players_straight_rank[iii] == highest_rank:
            counter += 1
            draw_result.append(iii)

    if counter > 1:
    
        # For every item in list of winners
        for i in range(len(draw_result)):
            
            out = ""
            count = 0

            # Build a string of the winners
            for i in range(len(draw_result)):

                # If not the first time looping, prefix with an ampersand 
                if count > 0:
                    out += " & " + str(global_player_tracker[draw_result[i]] + 1)
                # If the first time looping..
                else:
                    out += str(global_player_tracker[draw_result[i]] + 1)
                count += 1

        output = "Split between players: " + out
    else:
        output = "Player " + str(global_player_tracker[players_straight_rank.index(highest_rank)] + 1) + " wins"

    if high_card_win == 14:
        output += " with a royal flush"
    else:
        output += " with a straight flush - " + str(card_rank[high_card_win]) + " high"

    print ""
    print output
    
def four_of_a_kind(hand):

    card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

    for item in hand:
        card_counter[item.rank] += 1

    for item in card_counter:
        if card_counter[item] == 4:
            return True

def four_of_a_kind_draw(hands):

    # Method assumes that every hand passed in contains a quad (four cards of the same rank)
    # Quad is the deciding factor as no more than one player can have four of the same high ranking quad
    
    players_hands = []
    players_hands = hands
    players_quad_rank = []
    highest_quad_rank = 0
    global high_card_win

    # For each individual players hand in the list containing all players hands, do the following...
    for i in range(len(players_hands)):
        
        # Create a clean dictionary to keep a count of how many of each specific card are in this players hand (suit is irrelevant here)
        card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

        # Look at each card in the players hand and increment the corresponding dictionary card by one
        for ii in range(len(players_hands[i])):
            card_counter[players_hands[i][ii].rank] += 1

        # Go through the dictionary afterwards and if one of the items has a count of 4 (indicating a quad) - append that cards rank to
        # the player_quad_rank list to determine everyones actual quad rank (this list maps to the list of hands passed to this function as an argument)
        for iii in range(2, 15):
            if card_counter[iii] > 3:
                players_quad_rank.append(iii)
                
    # Determine the highest ranking trio in the list of players_quad_rank
    highest_quad_rank = max(players_quad_rank)
    high_card_win = highest_quad_rank
    print ""
    print "Player " + str(global_player_tracker[players_quad_rank.index(highest_quad_rank)] + 1) + " wins with a four of a kind " + str(card_rank[high_card_win])
    
def full_house(hand):

    if pair(hand) and three_of_a_kind(hand):
        return True

def full_house_draw(hands):

    # Method assumes that every hand passed in contains a trio (three of the same rank)
    # Trio is the deciding factor as no more than one player can have three of the same high ranking trio
    
    players_hands = []
    players_hands = hands
    players_trio_rank = []
    highest_trio_rank = 0
    global high_card_win

    # For each individual players hand in the list containing all players hands, do the following...
    for i in range(len(players_hands)):
        
        # Create a clean dictionary to keep a count of how many of each specific card are in this players hand (suit is irrelevant here)
        card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

        # Look at each card in the players hand and increment the corresponding dictionary card by one
        for ii in range(len(players_hands[i])):
            card_counter[players_hands[i][ii].rank] += 1

        # Go through the dictionary afterwards and if one of the items has a count of 3 (indicating a trio) - append that cards rank to
        # the player_trio_rank list to determine everyones actual trio rank (this list maps to the list of hands passed to this function as an argument)
        for iii in range(2, 15):
            if card_counter[iii] > 2:
                players_trio_rank.append(iii)
                
    # Determine the highest ranking trio in the list of players_trio_rank
    highest_trio_rank = max(players_trio_rank)
    high_card_win = highest_trio_rank
    print ""
    print "Player " + str(global_player_tracker[players_trio_rank.index(highest_trio_rank)] + 1) + " wins with a full house - three of a kind: " + str(card_rank[high_card_win])
    
    

def flush(hand):

    if hand[0].suit == hand[1].suit  == hand[2].suit  == hand[3].suit  == hand[4].suit:
        return True

def flush_draw(hands):

    # add in global_player_tracker

    player_hands = hands
    player_hands_staging = []
    results = []
    max_result = 0
    counter = 0
    winner_found = False
    player_tracker = []
    player_tracker_staging = []
    first_draw_occurred = False

    print ""

    while winner_found == False:

        player_tracker_staging = []
        player_hands_staging = []
        results = []
        max_result = 0
        counter = 0

        # add highest card in each players hand to results list
        for i in range(len(player_hands)):
            player_hands[i].sort(key = operator.attrgetter("rank"))
            results.append(player_hands[i][-1].rank)
        print results
        # find the highest card in the list of players high cards
        max_result = max(results)

        # check if more than one player has the high card
        for i in range(len(results)):
            if results[i] == max_result:
                counter += 1

        # if more than one player has the highest card and there are more cards to process
        if (counter > 1) and (len(player_hands[0]) > 1):

            for i in range(len(player_hands)):
                
                if player_hands[i][-1].rank == max_result:

                    player_hands[i].pop(len(player_hands[i]) - 1)
                    player_hands_staging.append(player_hands[i])
                    
                    if first_draw_occurred is True:
                        player_tracker_staging.append(player_tracker[i])
                    else:
                        player_tracker.append(i)
                    
            if first_draw_occurred is True:
                player_tracker = copy.deepcopy(player_tracker_staging)
                
            player_hands = copy.deepcopy(player_hands_staging)
            
            first_draw_occurred = True
            
        #if more than one player has the highest card and there are no more cards to process
        elif counter > 1:
        
            result_string = ""
            count = 0
            
            for i in range(len(player_tracker)):
                # If not the first time looping, prefix with an ampersand 
                if count > 0:
                    result_string += " & " + str(global_player_tracker[player_tracker[i]] + 1)
                # If the first time looping..
                else:
                    result_string += str(global_player_tracker[player_tracker[i]] + 1)
                count += 1
                
            print "Players " + result_string + " win with a Flush & " + str(card_rank[max_result]) + " kicker!!"
            
            winner_found = True
            
        # if only one player has the highest card...
        else:
        
            if first_draw_occurred is True:
                print "Player " + str(global_player_tracker[player_tracker[results.index(max_result)]] + 1) + " wins with a Flush & " + str(card_rank[max_result]) + " kicker!!"
            else:
                print "Player " + str(global_player_tracker[results.index(max_result)] + 1) + " wins with a Flush & " + str(card_rank[max_result]) + " kicker!!"

            winner_found = True

def straight(hand):
    
    hand.sort(key=operator.attrgetter("rank"), reverse=False)

    if (
        (hand[1].rank == (hand[0].rank + 1)) and
        (hand[2].rank == (hand[1].rank + 1)) and
        (hand[3].rank == (hand[2].rank + 1)) and
        (hand[4].rank == (hand[3].rank + 1))
        ):
        
        return True

def straight_draw(hands):

    players_hands = []
    players_hands = hands
    players_straight_rank = []
    temp_card_store = []
    highest_rank = 0
    counter = 0
    draw_result = []
    global high_card_win
    
    for i in range(len(players_hands)):

        temp_card_store[:] = []
        
        for ii in range(len(players_hands[i])):
            temp_card_store.append(players_hands[i][ii].rank)

        players_straight_rank.append(max(temp_card_store))

    highest_rank = max(players_straight_rank)
    high_card_win = highest_rank

    for iii in range(len(players_straight_rank)):
        if players_straight_rank[iii] == highest_rank:
            counter += 1
            draw_result.append(iii)

    if counter > 1:

        # For every item in list of winners
        for i in range(len(draw_result)):
            
            output = ""
            count = 0

            # Build a string of the winners
            for i in range(len(draw_result)):

                # If not the first time looping, prefix with an ampersand 
                if count > 0:
                    output += " & " + str(global_player_tracker[draw_result[i]] + 1)
                # If the first time looping..
                else:
                    output += str(global_player_tracker[draw_result[i]] + 1)
                count += 1

        print ""
        print "Split between players: " + output  + " with a straight high: " + str(card_rank[high_card_win])
        
    else:
        print 
        print "Player " + str(global_player_tracker[players_straight_rank.index(highest_rank)] + 1)  + " wins with a straight high: " + str(card_rank[high_card_win])


def three_of_a_kind(hand):
    
    card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

    for item in hand:
        card_counter[item.rank] += 1

    for item in card_counter:
        if card_counter[item] == 3:
            return True

def three_of_a_kind_draw(hands):

    # Method assumes that every hand passed in contains a trio (three of the same rank) and only a trio at most (no player has
    # a full house - otherwise this function wouldn't be executed
    
    players_hands = []
    players_hands = hands
    players_trio_rank = []
    highest_trio_rank = 0
    global high_card_win

    # For each individual players hand in the list containing all players hands, do the following...
    for i in range(len(players_hands)):
        
        # Create a clean dictionary to keep a count of how many of each specific card are in this players hand (suit is irrelevant here)
        card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

        # Look at each card in the players hand and increment the corresponding dictionary card by one
        for ii in range(len(players_hands[i])):
            card_counter[players_hands[i][ii].rank] += 1

        # Go through the dictionary afterwards and if one of the items has a count of 3 (indicating a trio) - append that cards rank to
        # the player_trio_rank list to determine everyones actual trio rank (this list maps to the list of hands passed to this function as an argument)
        for iii in range(2, 15):
            if card_counter[iii] > 2:
                players_trio_rank.append(iii)
                
    # Determine the highest ranking trio in the list of players_trio_rank
    highest_trio_rank = max(players_trio_rank)
    high_card_win = highest_trio_rank
    print ""
    print "Player " + str(global_player_tracker[players_trio_rank.index(highest_trio_rank)] + 1) + " wins with a three of a kind hand " + str(card_rank[high_card_win])
    

def two_pair(hand):
    
    count = 0
    card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

    for item in hand:
        card_counter[item.rank] += 1

    for item in card_counter:
        if card_counter[item] == 2:
            count += 1

    if count > 1:
        return True

def two_pair_draw(hands):
    
    # Method assumes that every hand passed in contains two pairs (two pairs of cards of the same rank) and only two pairs at most (no player has
    # three of a kind or full house - otherwise this function wouldn't be executed
    
    players_hands = []
    players_hands = hands
    players_pair_rank = []
    player_store = []
    highest_pair_rank = 0
    high_hand_player_count = 0
    players_hands_staging = []
    player_tracker = []
    player_tracker_staging = []
    draw_result = []
    winner_found = False
    first_draw_occurred = False
    pairs = []

    print ""
    
    while winner_found is False:
        if len(players_hands[0]) > 1:
            
            players_pair_rank[:] = []
            highest_pair_rank = 0
            high_hand_player_count = 0
            players_hands_staging[:] = []
            player_tracker_staging[:] = []

            # For each individual players hand in the list containing all players hands, do the following...
            for i in range(len(players_hands)):
                
                player_store[:] = []
                
                # Create a clean dictionary to keep a count of how many of each specific card are in this players hand (suit is irrelevant here)
                card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

                # Look at each card in the players hand and increment the corresponding dictionary card by one
                for ii in range(len(players_hands[i])):
                    card_counter[players_hands[i][ii].rank] += 1

                # Go through the dictionary afterwards and if one of the items has a count of 2 (indicating a pair) - append that cards rank to
                # the player_pairs list to determine everyones actual pair rank (this list maps to the list of pairs passed to this function as an argument)
                for iii in range(2, 15):
                    if card_counter[iii] > 1:
                        player_store.append(iii)
                        
                players_pair_rank.append(max(player_store))
                        
            # Determine the highest ranking pair is the list of players_pairs
            highest_pair_rank = max(players_pair_rank)
            pairs.append(highest_pair_rank)

            # Check if more than one player has the highest ranking pair
            for i in range(len(players_pair_rank)):
                if (players_pair_rank[i] == highest_pair_rank):
                    high_hand_player_count += 1
            
            #print players_pair_rank
            # If more than 1 player has the highest ranking pair....
            if high_hand_player_count > 1:
                for i in range(len(players_pair_rank)):
                    if players_pair_rank[i] ==  highest_pair_rank:
                        for ii in xrange(len(players_hands[i]) -1, -1, -1):
                            if players_hands[i][ii].rank == highest_pair_rank:
                                players_hands[i].pop(ii)
                            
                        players_hands_staging.append(players_hands[i])
                        # If no draw has happened previously
                        if first_draw_occurred is False:
                            # add current players_hands position to the player_tracker list to track what players remaining
                            # relative to the original list of hands
                            player_tracker.append(i)
                        else:
                            # otherwise, add the player position relative to the original list of hands to the tracker staging table
                            player_tracker_staging.append(int(player_tracker[i]))

                if first_draw_occurred is True:
                    player_tracker = copy.deepcopy(player_tracker_staging)
                                        
                # after iterating through all hands, update the players_hands list to the staging list contents 
                players_hands = copy.deepcopy(players_hands_staging)
                
                # flag that a draw has occurred for ensure correct program behaviour in the next cycle
                first_draw_occurred = True

            # If only one player has the highest ranking pair...
            else:
                if len(player_tracker) > 0:
                    count = 0
                    output = "Player " + str(global_player_tracker[player_tracker[players_pair_rank.index(highest_pair_rank)]] + 1) + " wins with two pairs: "

                    # Build a string of the pairs
                    for i in range(len(pairs)):

                        # If not the first time looping, prefix with an ampersand 
                        if count > 0:
                            output += " & kicker pair of " + str(card_rank[pairs[i]])
                        # If the first time looping..
                        else:
                            output += str(card_rank[pairs[i]])
                        count += 1
                        
                    print output
                else:
                    print "Player " + str(global_player_tracker[players_pair_rank.index(highest_pair_rank)] + 1) + " wins with two pairs with high pair being " + str(card_rank[pairs[0]])

                winner_found = True
        else:
            
            draw_result = []
            
            # Assign draw_result to list of winner(s) returned by the high_card function that takes the updated list of players_hands
            draw_result = high_card(players_hands)

            # If a draw (more than one player)
            if len(draw_result) > 1:
                
                # For every item in list of winners
                for i in range(len(draw_result)):
                    
                    out = ""
                    count = 0

                    # Build a string of the winners
                    for i in range(len(draw_result)):

                        # If not the first time looping, prefix with an ampersand 
                        if count > 0:
                            out += " & " + str(global_player_tracker[player_tracker[draw_result[i]]] + 1)
                        # If the first time looping..
                        else:
                            out += str(global_player_tracker[player_tracker[draw_result[i]]] + 1)
                        count += 1
                        
                output = ""
                count = 0
                output = "Split between players: " + out  + " with two pairs: " 

                # Build a string of the winners
                for i in range(len(pairs)):

                    # If not the first time looping, prefix with an ampersand 
                    if count > 0:
                        output += " & " + str(card_rank[pairs[i]])
                    # If the first time looping..
                    else:
                        output += str(card_rank[pairs[i]])
                    count += 1

                output += " and with a high card kicker: " + str(card_rank[high_card_win])
                print output
                winner_found = True
            else:
                count = 0
                output = "Player " + str(global_player_tracker[player_tracker[draw_result[0]]] + 1) + " wins with two pairs: "

                # Build a string of the winners
                for i in range(len(pairs)):

                    # If not the first time looping, prefix with an ampersand 
                    if count > 0:
                        output += " & " + str(card_rank[pairs[i]])
                    # If the first time looping..
                    else:
                        output += str(card_rank[pairs[i]])
                    count += 1

                output += " and with a high card kicker: " + str(card_rank[high_card_win])
                print ""
                print output
                winner_found = True

def pair(hand):
    
    card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

    for item in hand:
        card_counter[item.rank] += 1

    for item in card_counter:
        if card_counter[item] == 2:
            return True


def pair_draw(hands):

    # Method assumes that every hand passed in contains a pair (two of the same rank) and only a pair at most (no player has
    # two pairs or a three of a kind - otherwise this function wouldn't be executed
    
    players_hands = []
    players_hands = hands
    players_pair_rank = []
    highest_pair_rank = 0
    high_hand_player_count = 0
    players_hands_staging = []
    player_tracker = []
    draw_result = []

    # For each individual players hand in the list containing all players hands, do the following...
    for i in range(len(players_hands)):
        
        # Create a clean dictionary to keep a count of how many of each specific card are in this players hand (suit is irrelevant here)
        card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

        # Look at each card in the players hand and increment the corresponding dictionary card by one
        for ii in range(len(players_hands[i])):
            card_counter[players_hands[i][ii].rank] += 1

        # Go through the dictionary afterwards and if one of the items has a count of 2 (indicating a pair) - append that cards rank to
        # the player_pairs list to determine everyones actual pair rank (this list maps to the list of pairs passed to this function as an argument)
        for iii in range(2, 15):
            if card_counter[iii] > 1:
                players_pair_rank.append(iii)
                
    # Determine the highest ranking pair in the list of players_pairs
    highest_pair_rank = max(players_pair_rank)
    
    # Check if more than one player has the highest ranking pair
    for i in range(len(players_pair_rank)):
        if (players_pair_rank[i] == highest_pair_rank):
            high_hand_player_count += 1
            
    # If more than 1 player has the highest ranking pair....
    if high_hand_player_count > 1:

        # For each hand in the list of all players hands
        for i in range(len(players_hands)):

            # Counter to count the the number of times the highest ranking pair card appears in this players hand (to essentially determine
            # if the player has in fact got two (a pair) of that card
            highest_pair_counter = 0
            for ii in range(len(players_hands[i])):
                if players_hands[i][ii].rank == highest_pair_rank:
                    highest_pair_counter += 1

            # If this player has the highest ranking pair...
            if highest_pair_counter > 1:
                # Go through each of that players cards to find the highest ranking pair cards
                for ii in xrange(len(players_hands[i]) -1, -1, -1):
                    # If highest ranking pair card found...
                    if players_hands[i][ii].rank == highest_pair_rank:
                        # Remove that card in preparation for deciding who is the winner through high card process of elimination
                        players_hands[i].pop(ii)
                        
                # Add the players new hand (the original hand minus the pair - making three cards) to a players_hands staging table
                players_hands_staging.append(players_hands[i])
                
                # Add the index of the players_hands item to player_tracker to later map the player to the original list of players_hands
                # E.g. original deck: [0, 1, 2, 3, 4, 5]
                # Players 1 & 4 have the highest ranking pair of Aces - therefore, store these in player_tracker: [1, 4]
                # Can then map the result set returned from the high_card function to this list i.e. index 1 of that arrary passed [0,1]
                # [1] -> 4 in the event of a win by player 4 or if both draw in high cards [0,1] -> [1,4]
                player_tracker.append(i)
                
        # Rebuild the players_hands list with the new list of only players who have the highest ranking pair (minus pair cards) which will
        # be sent to the high_card function
        players_hands = copy.deepcopy(players_hands_staging)

        draw_result = []

        # Assign draw_result to list of winner(s) returned by the high_card function that takes the updated list of players_hands
        draw_result = high_card(players_hands)

        # If a draw (more than one player)
        if len(draw_result) > 1:
            
            # For every item in list of winners
            for i in range(len(draw_result)):
                
                output = ""
                count = 0

                # Build a string of the winners
                for i in range(len(draw_result)):

                    # If not the first time looping, prefix with an ampersand 
                    if count > 0:
                        output += " & " + str(global_player_tracker[player_tracker[draw_result[i]]] + 1)
                    # If the first time looping..
                    else:
                        output += str(global_player_tracker[player_tracker[draw_result[i]]] + 1)
                    count += 1
                    
            print ""
            print "Split between players: " + output + " with pair of " + str(card_rank[highest_pair_rank]) + " and a high card kicker: " + str(card_rank[high_card_win])
        else:
            print ""
            print "Player " + str(global_player_tracker[player_tracker[draw_result[0]]] + 1) + " with pair of " + str(card_rank[highest_pair_rank]) + " and a high card kicker: " + str(card_rank[high_card_win])

    # If only one player has the highest ranking pair...
    else:
        print ""
        print "Player " + str(int(global_player_tracker[players_pair_rank.index(highest_pair_rank)] + 1))  + " wins with a pair of " + str(card_rank[highest_pair_rank])
        
def high_card(hands):
    
    # Note: this algorithm works on basis that every hand has a unique set of cards i.e. there are no pairs, trios etc.
    # Will pass back winning position(s) of array passed in which can be taken as is or compared against a look up from a calling function
    # Will use a list to keep track of players (draw_players) still playing (players_hands). The hands get knocked out of players_hands as
    # the software goes but draw_players keeps a track of the remaining positions relative to the original list passed to the proc
    
    players_hands = []
    players_hands = hands
    players_hands_staging = []
    player_tracker = []
    player_tracker_staging = []
    first_draw_occurred = False
    winner_found = False
    card_list = []
    highest_card = 0
    result_list = []
    global high_card_win
    
    # Keep running over and over until a winner is found
    while (winner_found is False):
        
        # Clean down necessary data structures
        card_list[:] = []
        player_tracker_staging[:] = []
        players_hands_staging[:] = []
        highest_card = 0
        card_counter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        
        # Add every card in every players hand to a list (card_list) and also count the number of each card across all players hands
        # card_list will be used to find the highest ranking card
        # The count of cards to see if more than one player has the highest ranking card
        for i in range(len(players_hands)):
            for ii in range(len(players_hands[i])):
                card_counter[players_hands[i][ii].rank] += 1
                card_list.append(players_hands[i][ii].rank)
				
        # highest_card = the highest ranking card in card_list
        highest_card = max(card_list)
        high_card_win = highest_card
       
        # If two or more players have the highest ranking card in this iteration...
        if card_counter[highest_card] >= 2:
            # If there is more than one card remaining (not yet the last round)
            if len(players_hands[0]) > 1:
                for i in range(len(players_hands)):
                        for ii in xrange(len(players_hands[i]) -1, -1, -1):
						
                            # if current card is the highest...
                            if players_hands[i][ii].rank == highest_card:
							
				# remove that from the hand 
                                players_hands[i].pop(ii)
								
				# add the updated hand to the hand staging list
                                players_hands_staging.append(players_hands[i])
                                
				# If no draw has happened previously
                                if first_draw_occurred is False:
                                    # add current players_hands position to the player_tracker list to track what players remaining
                                    # relative to the original list of hands
                                    player_tracker.append(i)
                                else:
                                    # otherwise, add the player position relative to the original list of hands to the tracker staging table
                                    player_tracker_staging.append(int(player_tracker[i]))
                
				# after iterating through all hands, update the player_tracker list to the staging list contents
                if first_draw_occurred is True:
                    player_tracker = copy.deepcopy(player_tracker_staging)
					
                # after iterating through all hands, update the players_hands list to the staging list contents 
                players_hands = copy.deepcopy(players_hands_staging)
                
				# flag that a draw has occurred for ensure correct program behaviour in the next cycle
                first_draw_occurred = True
            # If there is only one card remaining in the players hands - i.e. this is the last round where winner(s) must be decided
            else:
                if len(player_tracker) > 0:
                    for i in range(len(players_hands)):
                        for ii in range(len(players_hands[i])):
                            if players_hands[i][ii].rank == highest_card:
                                result_list.append(player_tracker[i])
                else:
                    for i in range(len(players_hands)):
                        for ii in range(len(players_hands[i])):
                            if players_hands[i][ii].rank == highest_card:
                                result_list.append(i)
							
                # Set winner_found to true to stop the while cycle
                winner_found = True
				
        # If one player has the highest ranking card in this iteration...
        else:
		
            # Go through each hand to find the player with the highest ranking card 
            for i in range(len(players_hands)):
                for ii in range(len(players_hands[0])):
				
                    # If the current card is the highest ranking card...
                    if int(players_hands[i][ii].rank) == highest_card:
					
                        # If the player_tracker has elements (there has been a draw in previous high card check iteration and therefore
                        # the original list of hands could have been modified by players (hands) being eliminated. Therefore, we need to check
                        # the tracker to find out the winner relative to the original list of players
                        if len(player_tracker) > 0:
                            result_list.append(player_tracker[i])
							
                        # If there has been no previous draw / one player has the high card first time around
                        else:
                            result_list.append(i)
                        
                        # Set winner_found to true to stop the while cycle
                        winner_found = True

    return result_list


def no_hand(hands):

    draw_result = []
    players_hands = hands
    
    # Assign draw_result to list of winner(s) returned by the high_card function that takes the updated list of players_hands
    draw_result = high_card(players_hands)

    # If a draw (more than one player)
    if len(draw_result) > 1:
        
        # For every item in list of winners
        for i in range(len(draw_result)):
            
            output = ""
            count = 0

            # Build a string of the winners
            for i in range(len(draw_result)):

                # If not the first time looping, prefix with an ampersand 
                if count > 0:
                    output += " & " + str(global_player_tracker[draw_result[i]] + 1)
                # If the first time looping..
                else:
                    output += str(global_player_tracker[draw_result[i]] + 1)
                count += 1
                
        print ""
        print "Split between players: " + output + " with a high card: " + str(card_rank[high_card_win])
    else:
        print ""
        print str(global_player_tracker[draw_result[0]] + 1) + " wins with a high card: " + str(card_rank[high_card_win])
    
# Take a card at random from the deck and store it in drawn_cards list
def drawCard():
    
    card_found = False

    while (card_found is False):
        
        card = random.randrange(0, 51)

        if card not in drawn_cards:
            card_found = True
            drawn_cards.append(card)

    return card

def evaluate(hand):
    
    if straight_flush(hand):
        return 9
    elif four_of_a_kind(hand):
        return 8
    elif full_house(hand):
        return 7
    elif flush(hand):
        return 6
    elif straight(hand):
        return 5
    elif three_of_a_kind(hand):
        return 4
    elif two_pair(hand):
        return 3
    elif pair(hand):
        return 2
    else:
        return 0

## For every player, add a blank list object to the players_hands list object
## to store the cards of that individual player
for i in range(players_count):
    global_player_hands.append([])

## Burn a card
drawCard()

## Deal two cards to each player - traversing between each
for i in range(number_of_cards):
    for ii in range(players_count):
        
        global_player_hands[ii].append(Card(drawCard()))

for i in range(len(global_player_hands)):
    player_scores.append(evaluate(global_player_hands[i]))

largest = max(player_scores)

high_hand_count = 0

for i in range(len(player_scores)):
    if player_scores[i] == largest:
        high_hand_count += 1

# Print each individual players cards to screen
for i in range(len(global_player_hands)):
    print ""
    print "[Player " + str(i + 1) + " cards]:"
    
    for item in global_player_hands[i]:
        print str(card_rank[item.rank]) + " of " + item.suit
    print "******"
    print "Hand: " + hand_rank[player_scores[i]]

print ""

if high_hand_count > 1:
    for i in range(len(player_scores)):
        if player_scores[i] == largest:
            global_player_tracker.append(i)
            temp_global_player_hands.append(global_player_hands[i])

    global_player_hands = copy.deepcopy(temp_global_player_hands)

    if largest == 9:
        straight_flush_draw(global_player_hands)
    elif largest == 8:
        four_of_a_kind_draw(global_player_hands)
    elif largest == 7:
        full_house_draw(global_player_hands)
    elif largest == 6:
        flush_draw(global_player_hands)
    elif largest == 5:
        straight_draw(global_player_hands)
    elif largest == 4:
        three_of_a_kind_draw(global_player_hands)
    elif largest == 3:
        two_pair_draw(global_player_hands)
    elif largest == 2:
        pair_draw(global_player_hands)
    else:
        no_hand(global_player_hands)
    
else:
    print "Player " + str(int(player_scores.index(largest) + 1)) + " wins with a " + hand_rank[largest]






