import random   

def display_board(board):
    print('\n'*100)
    print(board[7] +'|'+board[8]+'|'+board[9])
    print(board[4] +'|'+board[5]+'|'+board[6])
    print(board[1] +'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        try:
            position = int(input('Choose a position: (1-9) '))
        except:
            print("Only numbers")
        
    return position

def replay():
    choice = input('Play again? Enter Yes or No => ').lower()
    
    return choice == 'yes'