def find_words(matrix, dictionary):
    def is_valid_cell(x, y):
        return 0 <= x < M and 0 <= y < N and not visited[x][y]

    def backtrack(x, y, current_word):
        if current_word in dictionary:
            valid_words.add(current_word)

        visited[x][y] = True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_cell(nx, ny):
                new_word = current_word + matrix[nx][ny]
                if any(word.startswith(new_word) for word in dictionary):
                    backtrack(nx, ny, new_word)

        visited[x][y] = False

    M, N = len(matrix), len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited = [[False for _ in range(N)] for _ in range(M)]
    valid_words = set()

    for i in range(M):
        for j in range(N):
            start_char = matrix[i][j]
            backtrack(i, j, start_char)

    return list(valid_words)


boggle_board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

dictionary = ['START', 'NOTE', 'SAND', 'STONED']

valid_words = find_words(boggle_board, dictionary)
print(valid_words)
