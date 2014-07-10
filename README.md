DESCRIPTION:

To run this code (yes, bad script name :-) ): python 10.py


High level explanation:

Deal five cards to a specified number of players, evaluate the hands of each player and decide who wins (draws in hands are handled by the app)


Detailed explanation:

This piece of code when ran, will randomly deal 5 cards to each of a specified number of players (set by players_count variable - found beneath #Variables header at very top of python file). The cards are randomly dealt by randomly picking a number between 0 and 51 (each number representing a unique card in the 52 card deck) on each draw. Each time a random 0-51 number is picked during the dealing process, there is a check to first see that the card is not in the list of drawn cards. If the card is in the list, the system will keep going until it finds a card not in the list of drawn cards. When a card not already drawn has been found, that card will be added to the players list of cards (this is a list of card objects - each of which gets constructed based off the number during instantiation i.e. range 0-13 = hearts, 14-27=spades etc...). When 5 cards have been dealt to each player, the system will then evaluate each players cards to see what hand each player has - if any. When that process has completed, the system will then pick the winner based off highest hand rank (i.e. straight would be 9 but a weaker hand such as a pair would be 3, 9 is stronger than 3 so that hand wins). However, if there is a tie in the highest hand rank (i.e. two or more players have a pair or a full house etc), then the system will compare those individual players hands to see which one has the strongest (ie. pair of Aces beats pair of KIngs). There is further logic within each draw method to cater for a draw in a draw. i.e. if both players have a pair of Aces, then the system will look for the highest card and so on....

Also important to note that there are tracker variables throughout... these are used to determine winners at end of evaluations. i.e. if 5 players started out in the game but there was a draw between 3 players (3 players had a pair), then only those 3 players will go through to the draw stage i.e. pair_draw which is used to find out who has the highest pair. If player 2 of those three wins, then it's not necessarily player 2 that wins as that player might actually have been player 4 relative to the original group of 5 players.


Areas for improvement:

1. In each random card draw, instead of keeping track of what card numbers (0-51) have been drawn in an array and subsequently building the card object by mapping the 0-51 number within to certain ranges (to decide rank & suit) which is then added to the current players hand...
Instead have an array of card objects to pull from, each of which gets directly added to the players hand at deal time. On
each draw, if the number isn't within the deck of available cards, go again. With this change, can then most likely
pull out the card_rank look up - getting this information from the card object itself when necessary

2. Can most likely make one results printing function that all hand evaluation functions pass result arrays to - along with
player mapping arrays (these are used to find out the winning player relative to the original array when it comes to draws).
global_player_tracker is used to map relative to the original set of players i.e. 8. For example: if 8 players started out 
and 5 were in a high card draw , this will map those 5 players relative to the original 8. There are also function specific
i.e. player_tracker. For example a high_card function received 5 players hands. if 3 of those players have an ace,
player_tracker will map those 3 players to the relative position in the original array of 5 throughout the process of
elimination. At the end of a draw-draw (i.e. multiple players with a high card-multiple players with an Ace high),
the position of the true winner is found by wrapping the position in the current array of players within a player_tracker
lookup, which itself is wrapped within a global_player_lookup

3. flush_draw function is actually an improved version of high_card - high_card code should be called instead of copied

4. straight_flush & straigh_draw use the same code - could be combined into one function

5. the two_pair_draw function could use the pair_draw function to find the high pair and then do another call if there's 
a draw... (this function already calls on the high_card function if there is a draw for both pairs)

6. there really isn't a need for no_hand function as high_card gets called when this situation arises

7. as mentioned in point 1, drawCard could be re-written accordingly to satisfy this
