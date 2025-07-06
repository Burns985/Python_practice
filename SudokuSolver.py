def is_safe(board, row, col, num):
    # Check if 'num' is not present in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' is not present in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_cell(board):
    # Find the first empty cell in the Sudoku grid (marked by 0)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None


def solve_sudoku(board):
    row, col = find_empty_cell(board)

    # If no empty cells are found, the Sudoku is already solved
    if row is None and col is None:
        return True

    # Try placing numbers from 1 to 9 in the current cell
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            # If the number is safe, place it in the cell
            board[row][col] = num

            # Recursively solve the remaining Sudoku
            if solve_sudoku(board):
                return True

            # If the current placement doesn't lead to a solution,
            # reset the cell and try the next number
            board[row][col] = 0

    # If no number can be placed in the current cell, backtrack
    return False


if __name__ == "__main__":
    # Example Sudoku grid (0 represents empty cells to be filled)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku_grid):
        print("Sudoku Solved:")
        for row in sudoku_grid:
            print(row)
    else:
        print("No solution exists for the given Sudoku.")
