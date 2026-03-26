### Tic Tac Toe ###

# Set up variables
board = ["", "", "", "", "", "", "", "", ""]
current_player = "X"
turn_counts = 0
game_active = True

# winning conditions
win_lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],    # Horizontal
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],    # Vertical
    [0, 4, 8],
    [2, 4, 6],    # Diagonal
]

def print_board():     
    print("\n")
    print(f" {board[0]}  | {board[1]}  | {board[2]}  ")
    print("---+---+---")
    print(f" {board[3]}  | {board[4]}  | {board[5]}  ")
    print("---+---+---")
    print(f" {board[6]}  | {board[7]}  | {board[8]}  ")
    print("\n")

while game_active:
    print_board()

    valid_move = False
    while not valid_move:    
        move = input(f"Player {current_player}, Please enter a spot from 0 - 8: ")

        #validate the input and deal with edge cases
        if move.isdigit():
            move = int(move)

            if 0 <= move <=8:           #if move > 8 or move < 0
                if board[move] == "":
                    valid_move = True
                else:
                    print("Spot is already taken")    
            else:
                print("Please enter a number within 0 and 8") 
        else:
            print("Please enter only nubers")             

board[move] = current_player
# print(board)
# game_active = False
turn_counts += 1

for line in win_lines: