def print_board(board):
    header = ''
    for num in range(1, len(board) + 1):
        header += "  " + str(num) + " "
    print(header)
    print('+---' * (len(board)) + '+')

    for row in range(len(board[0])):
        print(('|   ') * (len(board) + 1))

        row_with_items = ''
        for col in range(len(board)):
            row_with_items += ('| '+str(board[col][row])) + ' '
        print(row_with_items + '|')

        print('|   ' * (len(board) + 1))
        print('+---' * len(board) + '+')


def move_is_valid(board, column):
    if column < 1 or column > len(board):
        return False
    if board[column - 1][0] != ' ':
        return False
    return True


def available_moves(board):
    moves = []
    for column in range(1, len(board)+1):
        if move_is_valid(board, column):
            moves.append(column)
    return moves


def select_space(board, column, piece):
    if not move_is_valid(board, column):
        print("Trying to place an " + piece + " in column " + str(column))
        print("Make sure to pick a column between 1 and " +
              str(len(board)) + " that is not full")
        print()
        return False

    if piece != 'X' and piece != 'O':
        print("Trying to place an " + piece + " in column " + str(column))
        print("Make sure to use either an 'X' or an 'O' as your piece")
        print()
        return False

    for row in range(len(board[0]) - 1, -1, -1):
        if board[column - 1][row] == ' ':
            board[column - 1][row] = piece
            print('Placed an ' + piece + ' in column ' + str(column))
            print()
            return False
    available_moves(board)
    return True


def has_won(board, piece):
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == piece and board[x+1][y] == piece and board[x+2][y] == piece and board[x+3][y] == piece:
                return True

    for y in range(len(board[0]) - 3):
        for x in range(len(board)):
            if board[x][y] == piece and board[x][y+1] == piece and board[x][y+2] == piece and board[x][y+3] == piece:
                return True

    for y in range(3, len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == piece and board[x+1][y-1] == piece and board[x+2][y-2] == piece and board[x+3][y-3] == piece:
                return True

    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == piece and board[x+1][y+1] == piece and board[x+2][y+2] == piece and board[x+3][y+3] == piece:
                return True
    return False


def game_over(board):
    return has_won(board, 'X') or has_won(board, 'O') or len(available_moves(board)) == 0


def play_game():

    my_board = []
    for col in range(7):
        my_board.append([' '] * 6)

    turn = 'X'
    winner = False
    while(not game_over(my_board)):
        print_board(my_board)
        move = 0
        available = available_moves(my_board)

        while (move not in available):
            move = int(input(
                "It is " + turn + "'s turn. Please select a column. Your optionns are " + str(available)))
            select_space(my_board, move, turn)

        if has_won(my_board, turn):
            print(turn + " has won!")
            print_board(my_board)
            winner = True
            break

            # Switching the players turn
        if turn == 'X':
            turn = "O"
        else:
            turn = 'X'
        # If we exit the loop and haven't determined a winner, that means it was a tie
    if not winner:
        print("It was a tie!")
        print_board(my_board)


play_game()

