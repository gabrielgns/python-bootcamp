from tic_tac_toe import *

print('Welcome to Tic TAC TOE')

while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n?: ').lower()

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)

            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if(win_check(the_board,player1_marker)):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
       
        else:
            if turn == 'Player 2':
                display_board(the_board)

            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if(win_check(the_board,player2_marker)):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'
            

    if not replay():
        break