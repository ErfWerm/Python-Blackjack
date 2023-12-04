A game of Blackjack, written in Python 3.12

This game has 3 modes -

	Quick Blackjack - Just play a normal hand of blackjack
	All Stars - Play with some fake money. You can set the start amount.
	Fixed Income - Play with some fake money like All Stars, but start with a strict $1000.

Object of the game is to get the closest to 21 without going over.
21 is perfect.
Kings, Queens, and Jacks all equal 10. 
As such, they are not in the game, but instead have an additional placeholder of 10.
For example, the dealers deck has...

	0, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10

In the above example 0 will not be indexed, but instead is a place holder for a blank card.
We use this for the dealers first hand, as a replacement for the hidden second card.
11 is the Ace, which will be an 11 unless the player or computer is over 21.
In this case, Ace will be used as a 1.

Questions? Hit me up.