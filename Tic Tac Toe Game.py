

# This code is not my own. I got it from ChatGPT. 
# However, I thought it would be a great learning opportunity to use "someone else's" code, figure out how it works, and moddify it to my needs.


while True:
    import random

# Printing the openning message to the player.
    print("""
Let's play Tic-Tac-Toe!
        
Only input numbers please.
        
        """)

# This code creates a function to print the board. 
# For every row in the board (3), it will first skip over the initial horizontal line, then print 3 vertical and 2 horizontal line alternating.
    def print_board(board):
        stop = True
        for row in board:
            if stop == False:
                print("-" * 9)
            print(" | ".join(row))
            stop = False
        print("""
            """)

# This code creates a function to check for a winner. 
# First it defines 'lines' as all the horizontal, vertical, and diagonal lines within the board.
# Then it checks through 'lines' to see if all values within any given line equals all 'X' or all 'O' (with no empty spaces).
# If no winner is found, it checks for any empty tiles (a tie). If there is no winner or tie, then the game continues as normal.
    def check_winner(board):
        lines = board + [[board[i][j] for i in range(3)] for j in range(3)] + [[board[i][i] for i in range(3)]] + [[board[i][2-i] for i in range(3)]]
        for line in lines:
            if line.count(line[0]) == len(line) and line[0] != ' ':
                return line[0]
        if ' ' not in [cell for row in board for cell in row]:
            return 'Tie'
        return None

# This code creates a function to take in player input.
# It first prompts the player to select the space (or cell) that they want. Then checks to see if that space is empty. 
# If it is, it returns the row and column. If not, it prints a message to the player to try again.
# If the player input is not valid, it will print a message to the player to repeat the valid input format.
    def player_move(board):
        while True:
            try:
                row, col = map(int,input("Enter row and then column (0, 1, or 2) separated by a space: ").split())
                if board[row][col] == ' ':
                    return row, col
                print("Cell already taken. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

# This code creates a function to decide the computer's move.
# It decides on a random row and column if it happens to be an empty space.
    def computer_move(board):
        return random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])

# This code creates a function to use the defined functions above to play the game.
# First it creates the array, defines the player/computer moves, and sets the current player to "X".
# Then it uses a while loop to print the board and check for a winner.
    def main():
        # The line below creates the array. I double checked that it was nested lists by using "print(board)".
        board = [[' ' for _ in range(3)] for _ in range(3)]
        players = {'X': player_move, 'O': computer_move}
        current_player = 'X'
        while True:
            print_board(board)
            row, col = players[current_player](board)
            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                if winner == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Player {winner} wins!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
    if __name__ == "__main__":
        main()
# This will reboot the program if desired.
    reboot = input("Restart Program? (Y/N): ")
    if (reboot == "N") or (reboot == "n"):
        break
    else:
        continue
