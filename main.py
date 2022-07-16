board = ['_','_','_','_','_','_','_','_','_'] #the simple board setup
i = 1 #initialising iterator value

def print_board(board):     #printing the board by breaking the list in 3 parts
    count = 1               
    for x in board:
        print(x, end=' ')
        if count % 3 == 0:
            print()
        count += 1

def win_test(board):        #checking the winning condition for each player
    x_count = board.count('X') 
    o_count = board.count('O')

    if (board[0] == board[4] == board[8] == 'X'):
        print('X wins!')
        return 'exit' 
    elif board[0] == board[4] == board[8] == 'O':
        print('O wins!')
        return 'exit'
    elif board[2] == board[4] == board[6] == 'X':
        print('X wins!')
        return 'exit'
    elif board[2] == board[4] == board[6] == 'O':
        print('O wins!')
        return 'exit'
    elif board[0] == board[3] == board[6] == 'X':
        print('X wins!')
        return 'exit'
    elif board[0] == board[3] == board[6] == 'O':
        print('O wins!')
        return 'exit'
    elif board[1] == board[4] == board[7] == 'X':
        print('X wins!')
        return 'exit'
    elif board[1] == board[4] == board[7] == 'O':
        print('O wins!')
        return 'exit'
    elif board[2] == board[5] == board[8] == 'X':
        print('X wins!')
        return 'exit'
    elif board[2] == board[5] == board[8] == 'O':
        print('O wins!')
        return 'exit'
    elif board[0] == board[1] == board[2] == 'X':
        print('X wins!')
        return 'exit'
    elif board[0] == board[1] == board[2] == 'O':
        print('O wins!')
        return 'exit'
    elif board[3] == board[4] == board[5] == 'X':
        print('X wins!')
        return 'exit'
    elif board[3] == board[4] == board[5] == 'O':
        print('O wins!')
        return 'exit'
    elif board[6] == board[7] == board[8] == 'X':
        print('X wins!')
        return 'exit'
    elif board[6] == board[7] == board[8] == 'O':
        print('O wins!')
        return 'exit'
    elif x_count + o_count == 9:
        print('Draw!')
        return 'exit'

def player_move(board):     #player's move by taking input from the user
    global i
    if board[move - 1] == '_':
        if i % 2 == 0:
            board[move - 1] = 'X'
        else:
            board[move - 1] = 'O'
        i += 1
    else:
        print('Invalid move!')

while '_' in board:

    print_board(board)
    move = int(input('Enter move number (1 - 9): ')) #user input

    if move < 1 or move > 9:    #checking if move is invalid
        print('Invalid move!')
        continue

    player_move(board)
    win_test(board)
    if win_test(board) == 'exit': #code exit condition
        break
