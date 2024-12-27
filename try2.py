import random


def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")


def check_win(board, player):
    for i in range(3):
        if all(board[i * 3 + j] == player for j in range(3)):
            return True
        if all(board[j * 3 + i] == player for j in range(3)):
            return True
    if all(board[i * 4] == player for i in range(3)):
        return True
    if all(board[i * 2 + 2] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    return all(cell != " " for cell in board)


def get_computer_move(board):
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_win(board, "O"):
                return i
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                board[i] = "O"
                return i
            board[i] = " "

    if board[4] == " ":
        return 4

    corners = [0, 2, 6, 8]
    available_corners = [corner for corner in corners if board[corner] == " "]
    if available_corners:
        return random.choice(available_corners)

    sides = [1, 3, 5, 7]
    available_sides = [side for side in sides if board[side] == " "]
    if available_sides:
        return random.choice(available_sides)

    for i in range(9):
        if board[i] == " ":
            return i
    return -1


def play_tic_tac_toe():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if 0 <= move <= 8 and board[move] == " ":
                        board[move] = "X"
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number between 1 and 9.")
        else:
            print("Computer's turn...")
            move = get_computer_move(board)
            board[move] = "O"
            print(f"Computer chose {move + 1}")

        if check_win(board, current_player):
            print_board(board)
            print(current_player, "wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_tic_tac_toe()
