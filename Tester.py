#Satinder Singh
#TCSS 435
import sys
from Board import Board
from Solver import Solver

class Tester:
    def __init__(self):
        self.readme = open("readme.txt", "w")

    def main(self):
        #main method that takes in input from user
        while True:
            print("Enter '1' to play a game, '2' to generate README, or '3' to quit:")
            choice = input().strip()
            if choice == '1':
                print("Who goes first? 1 for AI, 2 for Human:")
                first_player = int(input().strip())
                print("Enter the search method. 'MM' for Minimax, 'AB' for Minimax with AB pruning:")
                method = input().strip()
                print("Enter the board size in the format 'rows/columns':")
                rows, cols = map(int, input().strip().split('/'))
                self.play_game(3, first_player=first_player, method=method, rows=rows, cols=cols)
                print("Would you like to play again or exit? Enter '1' to play again, '2' to exit:")
                again = input().strip()
                if again == '2':
                    break
            elif choice == '2':
                self.generate_readme(3)
                self.readme.close()
                print("README has been generated.")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def play_game(self, depth, first_player=None, method=None, rows=None, cols=None, ai_vs_ai=False, print_to_console=True):
        #This method sets up and executes a game, based on various input parameters. 
        # It can facilitate games of AI vs AI, Human vs AI and it can print the game progress to the console.
        board_size = (rows, cols) if rows and cols else self.get_board_size()
        first_player = first_player if first_player else self.get_first_player()
        method = method if method else self.get_search_method()
        board = Board(*board_size)
        player1_solver = Solver(board, 1, method)
        player2_solver = Solver(board, 2, method)
        current_player_solver = player1_solver if first_player == 1 else player2_solver
        nodes_expanded = 0
        while not board.game_over():
            if ai_vs_ai or current_player_solver.player == 1:
                move = current_player_solver.best_move(depth)
            else:
                move = self.get_human_move(board)
            
            board.mark_cell(*move, current_player_solver.player)
            nodes_expanded += current_player_solver.nodes_expanded
            print(f"Player {current_player_solver.player} {'(AI)' if ai_vs_ai or current_player_solver.player == 1 else '(Human)'} moves: {move}")
            if print_to_console:
                print(f"Player {current_player_solver.player} {'(AI)' if ai_vs_ai or current_player_solver.player == 1 else '(Human)'} moves: {move}")
                board.print_board()
            current_player_solver = player1_solver if current_player_solver == player2_solver else player2_solver
        winner = 2 if current_player_solver == player1_solver else 1
        return winner, nodes_expanded

    def get_human_move(self, board):
        #This method prompts the human player for a move and ensures it's valid.
        while True:
            move = input("Please enter your move in the format 'row/column':")
            try:
                row, col = map(int, move.split('/'))
                if board.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid format. Try again.")


    '''def write_to_readme(self, board_size, player, method, depth, winner, nodes_expanded):
        if player == 1:
            ai_player = "1 (MAX Player)"
        else:
            ai_player = "2 (MIN Player)"
        if method == 'MM':
            search_method = "Minimax"
        else:
            search_method = "Minimax with AB pruning"
        self.readme.write(f"*** {board_size[0]} x {board_size[1]} Boards ***\n")
        self.readme.write(f"AI is player {ai_player}:\n")
        self.readme.write(f"{search_method}\n")
        self.readme.write(f"nodes expanded: {nodes_expanded}\n")
        self.readme.write(f"Depth level {depth}\n")
        self.readme.write(f"Winner: Player {winner}\n")'''

    #def close(self):
        #self.readme.close()

    def generate_readme(self, depth):
        #this generates the readme file
        #print("debug 1")
        self.readme.write("# Obstructions Game AI README\n")
        self.readme.write("## AI vs AI\n")
        self.readme.write("""
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
""")
        for board_size in [(6, 6), (7, 6), (8, 7), (8, 8)]:
            #print("debug 2")
            self.readme.write(f"*** {board_size[0]} x {board_size[1]} Boards ***\n")
            for player in [1, 2]:
                if player == 1:
                    self.readme.write("AI is player 1:\n")
                else:
                    self.readme.write("AI is player 2:\n")
                for method in ['MM', 'AB']:
                    #print("debug 3")
                    for depth in [3, 4]:
                        self.readme.write(f"{self.method_name(method)}\n")
                        winner, nodes_expanded = self.play_game(depth, first_player=player, method=method, rows=board_size[0], cols=board_size[1], ai_vs_ai=True, print_to_console=False)
                        self.readme.write(f"nodes expanded: {nodes_expanded}\n")
                        self.readme.write(f"Depth level {depth}\n")

    def method_name(self, method):
        if method == 'MM':
            return "Minimax"
        else:
            return "Minimax with AB pruning"

if __name__ == "__main__":
    tester = Tester()
    tester.main()