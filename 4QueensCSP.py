BOARD_SIZE = 4

left_diagonal = [0] * 30
right_diagonal = [0] * 30
column = [0] * 30


def print_solution(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(" Q " if board[i][j] == 1 else " . ", end="")
        print()


def solve_n_queens_util(board, col):
    if col >= BOARD_SIZE:
        return True

    for i in range(BOARD_SIZE):
        if (left_diagonal[i - col + BOARD_SIZE - 1] != 1 and right_diagonal[i + col] != 1) and column[i] != 1:
            board[i][col] = 1
            left_diagonal[i - col + BOARD_SIZE - 1] = right_diagonal[i + col] = column[i] = 1

            if solve_n_queens_util(board, col + 1):
                return True

            board[i][col] = 0
            left_diagonal[i - col + BOARD_SIZE - 1] = right_diagonal[i + col] = column[i] = 0

    return False


def solve_n_queens():
    chess_board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    if not solve_n_queens_util(chess_board, 0):
        print("Solution does not exist")
        return False

    print_solution(chess_board)
    return True


if __name__ == "__main__":
    solve_n_queens()
