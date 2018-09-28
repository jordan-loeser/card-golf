# Six Card Golf 🏌️‍♂️⛳🏌️‍♀️

Six Card Golf was one of my favorite games as a kid, so I really enjoyed diving into the mechanics, strategy, and usability of the game.
I had a lot of fun working on this challenge problem, and I hope you enjoy playing it! 
![Screenshot](https://github.com/Jordan-Loeser/card-golf/blob/master/screenshot.png)

## Game Rules

| Players | 2-4 |
|---------|-----|

As defined by Bicycle Playing Cards:
> #### THE DEAL
> Each player is dealt 6 cards face down from the deck. The remainder of the cards are placed face down, and the top card is turned up to start the discard pile beside it. Players arrange their 6 cards in 2 rows of 3 in front of them and turn 2 of these cards face up. The remaining cards stay face down and cannot be looked at. 
> #### THE PLAY
> The object is for players to have the lowest value of the cards in front of them by either swapping them for lesser value cards or by pairing them up with cards of equal rank. <br><br> Beginning with the player to the dealer's left, players take turns drawing single cards from either the stock or discard piles. The drawn card may either be swapped for one of that player's 6 cards, or discarded. If the card is swapped for one of the face down cards, the card swapped in remains face up. The round ends when all of a player's cards are face-up. <br><br> A game is 1-9 rounds, and the player with the lowest total score is the winner.
> #### SCORING
> * Each ace counts 1 point.
> * Each 2 counts minus 2 points.
> * Each numeral card from 3 to 10 scores face value.
> * Each jack or queen scores 10 points.
> * Each king scores zero points.
> * A pair of equal cards in the same column scores zero points for the column (even if the equal cards are 2s).


## How to Run
1. `cd` into the `card-golf` directory
2. Run `python3 play_golf.py`
3. Follow the on-screen prompts to play the game
4. Press `ctrl-c` to exit the game

## Design Decisions

I decided to implement this game in Python using curses, because curses allows an interactive user experience that makes the card game both recognizeable and accessible. I utilized python classes to take an object-oriented approach to structuring the data. This allowed clarity between the many card decks that are in play at one time.

#### Considerations
* What happens if the terminal size is not large enough to display some graphics?
* What happens if the round ends without everyone getting equal turns?
* What happens if the draw pile runs out of cards?
* What happens if the keyboard input is invalid (during game initialization, drawing, or discarding)?
* What happens if the score is tied at the end of a round or game?

#### Resources
* [Six Card Golf - Card Game Rules](https://www.bicyclecards.com/how-to-play/six-card-golf/) by Bicycle Playing Card
* [Curses Programming with Python](https://docs.python.org/3/howto/curses.html) by Python 3.7 docs
