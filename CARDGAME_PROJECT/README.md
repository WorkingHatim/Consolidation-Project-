 # The card game

**Tricksy Battle** is a simple 2-player card game implemented in Python. This game uses a standard deck of playing cards, with the Kings removed The game ends early if one player reaches 9 points while the other has at least 1.
There are 16 rounds to the game, so there will be a total of 16 points if all rounds are played.


## How to Run
Make sure you have Python3 installed.

Save the Python file as card_game.py
using VS Code

open the command prompt or terminal in VS Code

Run the game by typing `python3 card_game.py`

## Features
- A game that uses a 48 card deck (52 - 4 kings) the kings are removed from the deck because thats how the game is played
- The code also defines the cards like real cards, with suits and values.
- The different suits that we can get are hearts, diamonds, clubs, and spades
- The code also sets a system were values will range from 1 - 11 2 is the weakest, and Queen is the strongest
- The game also has a scoring system, where the player with the highest score at the end of 16 rounds wins the game
- The code also runs all 16 round when pressing run so in the prompt you will see the round number and the cards that were drawn
- Its scores the the game based off each card that is drawn from each round 1 round is equivalent to 1 point
- The code is made so that the first person that gets to 16 points wins the game.
- The code will allow two players to play the game.
- The keeps track of the score of each player and the round number which they won if needed.


## Known Limitations
-   The game does not handle the case where both players have the same score at the end of the 16 because after it reaches 16 it will stop the game and declare the winner but what if they are both at 8 points. 
- The game does not have a way to save the game state, so if you close the game,the progress of what the previous game had will be lost.
- my code doesnt full implement the rules of the game. because my code doesnt end the game when one player reaches 9 points while the other has at least 1. it just keeps going until the 16 rounds are over.
- The game does not allow more than 2 players . If you try to add more than 2 players, the game will crash. Because the code was made to be a 2 player game.

