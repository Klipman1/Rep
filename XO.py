def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    marker = ''
    while marker != 'X' and marker != '0':
        marker = input('Игрок1 - выберите Х или 0:').upper()

    if marker == 'X':
        return ('X', '0')

    else:
        return ('0', 'X')


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    if board[1] == board[2] == board[3] == marker or \
        board[4] == board[5] == board[6] == marker or \
        board[7] == board[8] == board[9] == marker or \
        board[1] == board[4] == board[7] == marker or \
        board[2] == board[8] == board[5] == marker or \
        board[3] == board[6] == board[9] == marker or \
        board[1] == board[5] == board[9] == marker or \
        board[7] == board[3] == board[5] == marker:
        return True
    else:
        return False

import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Игрок1'
    else:
        return 'Игрок2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while str(position) not in '123456789' or not space_check(board, position):
        position = int(input('Куда ходим?(1-9):'))
    return position

def replay():
    choice = input('Играем снова?(Yep/No):')
    return choice == 'Yep'



while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' ходит первым')

    play_game = input('Вы готовы играть? Yep/No:')
    if play_game == 'Yep':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                display_board(board)
                print('Игрок1 выиграл!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Ничья!')
                    game_on = False
                else:
                    turn = 'Игрок2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print('Игрок2 выиграл!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Ничья!')
                    game_on = False
                else:
                    turn = 'Игрок1'











    if not replay():
        break








