# Implementation-and-Exploration-of-Chess
This is the first part in a larger project. In this part, the game of chess was implemented from scratch, a visual representation mechanism was set up, a simple random selector with no pruning strategy was programmed, a database for this strategy to store its experiences playing games against others was created, and an exchange system was set up against another chess engine called Sunfish (https://github.com/thomasahle/sunfish).

### High Level Details of Implementation
* AN.py: A helper module to aid in the conversion between algebraic notation and the program understandable notation (binary lists which represent squares on the board) and vice versa.
* Database.py: Defines several helper functions that help with things such as: making custom positions, retrieving positions of pieces, and converting a string of a piece's name to its corresponding object.
* Deeper Blue - Sunfish Exchange.py: An implementation of an interface between the two computer chess engines. Using this module, the programs can play each other over and over. Each can use the experience that it gains in the games to improve itself.
* DeeperBlue.py: The main implementation of the chess engine. Most of the rules of the game, functions for running dynamic chess games, and functions for interfacing between the computer and a human player are implemented here.
* GA.py: A helper module that helps the chess engine store its experiences and not choose previously experienced loosing paths
* Gamefile.txt: A text file storing all the different ways the program has lost.
* Pawn.py: A helper module implementing the way pawns move, capture, and promote (pawns are more difficult to implement than other pieces because of irregularities in their capabilities).
* Piececlasses.py: Module that implements object-oriented functionality for chess pieces so that they can also be treated as objects, which makes several other implementations more convenient.
* Printboard.py: Implements functions to print chess positions pictorially.

<!-- Incomplete -->
