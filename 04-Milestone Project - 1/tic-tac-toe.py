def tic_tac_toe():
    print('Welcome to Tic Tac Toe!')

    # Determine player 1 and player 2, and there letter of choice
    player1, player2 = setup_players()
    board = setup_board()
    turn = 0

    winning_player = ''
    while winning_player == '':
        print_board(board)
        if turn >= 9:
            break

        board = make_a_move(turn, (player1 if turn %
                            2 == 0 else player2), board)
        turn += 1
        winning_player = winner(board)

    if turn < 9:
        print(f'Congrats {winning_player} you have won!')
    else:
        print("The game has ended in a draw!")


def setup_players():
    player1 = ''
    player2 = ''

    while player1 != 'X' and player1 != 'O':
        print(player1)
        player1 = input(
            "Player 1 -- Please select X or O to play with: ").upper().rstrip()

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)


def setup_board():
    return [['*'] * 3, ['*'] * 3, ['*'] * 3]


def print_board(board):
    print('    1    2    3')
    for index, row in enumerate(board):
        print(f'{index + 1} {row}')


def make_a_move(turn, player_letter, board):
    row = -1
    col = -1
    move_available = False
    while not move_available:
        row = int(input(
            f'{"Player 1" if turn % 2 == 0 else "Player 2"} input your next moves row: '))
        col = int(input(
            f'{"Player 1" if turn % 2 == 0 else "Player 2"} input your next moves col: '))
        move_available = is_move_available(row, col, board)
        if not move_available:
            print(
                "Please make a valid move! That move was out of bound or already taken...")

    board[row - 1][col - 1] = player_letter
    return board


def is_move_available(row, col, board):
    row_index = row - 1
    col_index = col - 1

    if row_index < 0 or row_index > 2:
        return False

    if col_index < 0 or col_index > 2:
        return False

    return board[row_index][col_index][0] == '*'


def winner(board):
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    col1 = [board[0][0], board[1][0], board[2][0]]
    col2 = [board[0][1], board[1][1], board[2][1]]
    col3 = [board[0][2], board[1][2], board[2][2]]
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[2][0], board[1][1], board[0][2]]

    sequences = [
        row1,
        row2,
        row3,
        col1,
        col2,
        col3,
        diag1,
        diag2
    ]

    for seq in sequences:
        if winning_sequence(seq):
            return seq[0]

    return ''


def winning_sequence(seq):
    seq_set = set(seq)
    if len(seq_set) == 1:
        if 'X' in seq_set or 'O' in seq_set:
            return True
    return False


tic_tac_toe()
