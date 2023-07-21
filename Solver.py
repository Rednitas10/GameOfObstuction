#Satinder Singh
#TCSS 435
from Board import Board

class Solver:
    def __init__(self, board, player, method):
        #This constructor initializes the solver with a reference to the game board, 
        #the player it represents (1 or 2), and the search method (Minimax or Minimax with Alpha-Beta pruning).
        self.board = board
        self.player = player
        self.method = method
        self.nodes_expanded = 0
        self.depth_level = 0

    def best_move(self, depth):
        #This method returns the best move for the player, as determined by the Minimax algorithm. 
        # It iterates through all valid moves, applies each one, calls the Minimax method, 
        # undoes the move, and updates the best move and score if a better one is found.
        best_score = float('-inf') if self.player == 1 else float('inf')
        best_move = None

        for move in self.board.get_valid_moves():
            blocked = self.board.mark_cell(*move, self.player)
            if self.method == 'MM':
                score = self.minimax(depth - 1, 2 if self.player == 1 else 1)
            elif self.method == 'AB':
                score = self.minimax_alpha_beta(depth - 1, float('-inf'), float('inf'), 2 if self.player == 1 else 1)
            self.board.undo_move(*move, blocked)

            if self.player == 1 and score > best_score:  # the AI is the MAX player
                best_score = score
                best_move = move
            elif self.player == 2 and score < best_score:  # the AI is the MIN player
                best_score = score
                best_move = move

        return best_move

    def minimax(self, depth, player):
        #This method implements the Minimax algorithm with Alpha-Beta pruning. 
        # It recursively explores the game tree up to a certain depth and 
        # returns the best move (as a tuple of row and column) and its heuristic score. 
        if self.board.game_over() or depth == 0:
            return self.evaluate()

        self.depth_level = max(self.depth_level, depth)
        self.nodes_expanded += 1

        if player == 1:  # AI
            max_eval = float('-inf')
            for move in self.board.get_valid_moves():
                blocked = self.board.mark_cell(*move, player)
                eval = self.minimax(depth - 1, 2)
                self.board.undo_move(*move, blocked)
                max_eval = max(max_eval, eval)
            return max_eval
        else:  # Human
            min_eval = float('inf')
            for move in self.board.get_valid_moves():
                blocked = self.board.mark_cell(*move, player)
                eval = self.minimax(depth - 1, 1)
                self.board.undo_move(*move, blocked)
                min_eval = min(min_eval, eval)
            return min_eval

    def minimax_alpha_beta(self, depth, alpha, beta, player):
        # Alpha and Beta are used for pruning branches that don't need to be explored.
        if self.board.game_over() or depth == 0:
            return self.evaluate()

        self.depth_level = max(self.depth_level, depth)
        self.nodes_expanded += 1

        if player == 1:  # AI
            max_eval = float('-inf')
            for move in self.board.get_valid_moves():
                blocked = self.board.mark_cell(*move, player)
                eval = self.minimax_alpha_beta(depth - 1, alpha, beta, 2)
                self.board.undo_move(*move, blocked)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # alpha-beta pruning
            return max_eval
        else:  # Human
            min_eval = float('inf')
            for move in self.board.get_valid_moves():
                blocked = self.board.mark_cell(*move, player)
                eval = self.minimax_alpha_beta(depth - 1, alpha, beta, 1)
                self.board.undo_move(*move, blocked)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # alpha-beta pruning
            return min_eval

    def evaluate(self):
        #This method is the heuristic evaluation function. 
        # It assigns a score to the current board state, 
        # based on the depth of the search tree and whether it's the maximizing player's turn. 
        score = 0
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                if self.board.board[i][j] == 'O':  # If it is AI's cell
                    score += 1  # AI's cell is a positive score
                elif self.board.board[i][j] == 'X':  # If it is opponent's cell
                    score -= 1  # Opponent's cell is a negative score
                elif self.board.board[i][j] == '/':  # If it is a blocked cell
                    score += 0.5  # Blocked cell is also beneficial for the AI, but less than AI's own cell
        return score

        


