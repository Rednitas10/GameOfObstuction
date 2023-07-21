#Satinder Singh
#TCSS 435

# The Board class represents the game board. It includes methods to mark cells, block neighbors, 
# undo moves, and check the state of the game.
class Board:
    def __init__(self, rows, cols):
        # Constructor initializes the board with '-' (indicating empty cells) 
        # and sets up the directions for neighbors
        self.rows = rows
        self.cols = cols
        self.board = [['-' for _ in range(cols)] for _ in range(rows)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 directions for neighbors

    def block_neighbors(self, row, col):
        # Blocks the valid neighbors of a cell by replacing '-' with '/'
        # and returns the list of blocked cells
        blocked = []
        for dr, dc in self.directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.board[new_row][new_col] == '-':
                    self.board[new_row][new_col] = '/'
                    blocked.append((new_row, new_col))
        return blocked

    def is_valid_move(self, row, col):
        # Checks whether a move is valid (inside the board and on an empty cell)
        return 0 <= row < self.rows and 0 <= col < self.cols and self.board[row][col] == '-'
    
    def game_over(self):
        # Checks if the game is over (no valid moves left)
        return not self.get_valid_moves()

    def get_valid_moves(self):
        # Returns a list of all valid moves (empty cells)
        valid_moves = [(i, j) for i in range(self.rows) for j in range(self.cols) if self.is_valid_move(i, j)]
        return valid_moves

    def print_board(self):
        # Prints the current state of the board
        for row in self.board:
            print(' '.join(row))
        print()

    def mark_cell(self, row, col, player):
        # Marks a cell with 'O' or 'X', blocks its neighbors, and returns the blocked cells
        # If the move is invalid, returns None
        if self.is_valid_move(row, col):
            self.board[row][col] = 'O' if player == 1 else 'X'
            blocked = self.block_neighbors(row, col)
            return blocked  # return the blocked cells
        return None

    def undo_move(self, row, col, blocked):
        # Undoes a move, unblocking the blocked cells
        self.board[row][col] = '-'
        for r, c in blocked:
            self.board[r][c] = '-'

    def is_empty(self):
        # Checks whether the board is empty (all cells are '-')
        for row in self.board:
            for cell in row:
                if cell != '-':
                 return False
        return True
