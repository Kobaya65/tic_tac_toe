LINE = "-" * 9


def main():
    """Main function of the game."""
    print_instruction()
    # initialize board with value -1
    board = [-1] * 9
    # flag to see if there's a winner
    win = False
    # number of move in the game
    move = 0
    while not win:
        print_board(board)
        print(f"Turn number {move + 1}")
        turn = 'X' if move % 2 == 0 else 'O'

        # get user input
        user = get_input(turn)
        while board[user] != -1:
            print("Invalid move! Cell already taken. Please try again.\n")
            user = get_input(turn)
        board[user] = 1 if turn == 'X' else 0

        # invrease move and check for end game
        move += 1
        check_end_game(board, move)


def print_instruction():
    """Print playing instructions to the terminal."""
    texte = '| Please use the following cell numbers to make your move. |'
    len_texte = len(texte)
    encadre = ('-' * len_texte)
    print(f"\n{encadre}\n{texte}")
    print_board([2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f'{encadre}\n')


def print_board(board: list):
    """Print the game board.
    - board : game board
    """
    print("The board looks like this :")
    for i in range(3):
        print()
        for j in range(3):
            if board[i * 3 + j] == 1:
                print('X', end='')
            elif board[i * 3 + j] == 0:
                print('O', end='')
            elif board[i * 3 + j] != -1:
                print(board[i * 3 + j] - 1, end='')
            else:
                print(' ', end='')

            if j != 2:
                print(" | ", end='')

        if i != 2:
            print(f'\n{LINE}', end='')
        else:
            print()


def get_input(turn: str) -> int:
    """Get users input and verify them.
    - turn : player's token (X or O)\n
    Return
    - cell to be played
    """
    valid = False
    while not valid:
        try:
            user = input(f"Where would you like to place {turn} (1-9) ?")
            user = int(user)
            if user >= 1 and user <= 9:
                return (user - 1)
            else:
                print("That is not a valid move! Please try again.\n")
                print_instruction()
        except Exception:
            print(f"{user} is not a valid move! Please try again.\n")


def check_win(board: list):
    """Check if there's a winner.
    - board : game board\n
    Return index of the winner or -1
    """
    win_cond = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for each in win_cond:
        try:
            if board[each[0] - 1] == board[each[1] - 1] and board[each[1] - 1] == board[each[2] - 1]:
                return board[each[0] - 1]
        except Exception as e:
            print(f"Error: {e.__str__()}.")
    return -1


def quit_game(board: list, msg: str):
    """Display the game play and a message.
    - board : game board
    - msg   : message to be displayed
    """
    print_board(board)
    print(msg)
    quit()


def check_end_game(board: list, move: int):
    """Check for the end of the game.
    - board : game board
    - move  : number of move
    """
    if move > 4:
        winner = check_win(board)
        if winner != -1:
            final_message = f"The winner is {'X' if winner == 1 else 'O'} :-)"

            quit_game(board, final_message)
        elif move == 9:
            quit_game(board, "No winner :-(")


if __name__ == "__main__":
    main()
    