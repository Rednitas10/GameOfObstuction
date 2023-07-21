# Obstructions Game AI README
## AI vs AI

Evaluation Function:

Our evaluation function assesses the 'goodness' of a board state, 
providing a numerical score representing the advantage of one player over another. 
The calculation is based on:

1. Count of Possible Moves: The more moves a player can make, 
the better the position. It's a comparative score between the AI and the human player.

2. Weighted Corners and Edges: Corners and edges are given less weight as they provide 
fewer possibilities for future moves compared to the middle cells.

3. Blocking Moves: The function considers the number of moves that block the opponent's
potential moves. More blocking moves indicate a stronger position for the player.

This function forms the basis of our AI's decision-making process.
*** 6 x 6 Boards ***
AI is player 1:
Minimax
nodes expanded: 7632
Depth level 3
Minimax
nodes expanded: 111563
Depth level 4
Minimax with AB pruning
nodes expanded: 7632
Depth level 3
Minimax with AB pruning
nodes expanded: 35251
Depth level 4
AI is player 2:
Minimax
nodes expanded: 9910
Depth level 3
Minimax
nodes expanded: 213539
Depth level 4
Minimax with AB pruning
nodes expanded: 9910
Depth level 3
Minimax with AB pruning
nodes expanded: 59923
Depth level 4
*** 7 x 6 Boards ***
AI is player 1:
Minimax
nodes expanded: 15479
Depth level 3
Minimax
nodes expanded: 368708
Depth level 4
Minimax with AB pruning
nodes expanded: 15479
Depth level 3
Minimax with AB pruning
nodes expanded: 103783
Depth level 4
AI is player 2:
Minimax
nodes expanded: 17578
Depth level 3
Minimax
nodes expanded: 418184
Depth level 4
Minimax with AB pruning
nodes expanded: 17578
Depth level 3
Minimax with AB pruning
nodes expanded: 110198
Depth level 4
*** 8 x 7 Boards ***
AI is player 1:
Minimax
nodes expanded: 43480
Depth level 3
Minimax
nodes expanded: 1407150
Depth level 4
Minimax with AB pruning
nodes expanded: 43480
Depth level 3
Minimax with AB pruning
nodes expanded: 296408
Depth level 4
AI is player 2:
Minimax
nodes expanded: 47231
Depth level 3
Minimax
nodes expanded: 1605753
Depth level 4
Minimax with AB pruning
nodes expanded: 47231
Depth level 3
Minimax with AB pruning
nodes expanded: 340105
Depth level 4
*** 8 x 8 Boards ***
AI is player 1:
Minimax
nodes expanded: 67002
Depth level 3
Minimax
nodes expanded: 2569626
Depth level 4
Minimax with AB pruning
nodes expanded: 67002
Depth level 3
Minimax with AB pruning
nodes expanded: 430302
Depth level 4
AI is player 2:
Minimax
nodes expanded: 75015
Depth level 3
Minimax
nodes expanded: 3336620
Depth level 4
Minimax with AB pruning
nodes expanded: 75015
Depth level 3
Minimax with AB pruning
nodes expanded: 634260
Depth level 4
