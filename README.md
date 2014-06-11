*** Areas for improvement ***

1. In each random card draw, instead of keeping track of what card numbers (0-51) have been drawn in an array and subsequently building the card object by mapping the 0-51 number within a certain range to add to players hand array...
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
