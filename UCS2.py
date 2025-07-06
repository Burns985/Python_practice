import heapq


def find_words(matrix, dictionary):
    def is_valid_cell(x, y):
        return 0 <= x < M and 0 <= y < N and not visited[x][y]

    M, N = len(matrix), len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    valid_words = set()

    for depth_limit in range(1, M * N + 1):
        visited = [[False for _ in range(N)] for _ in range(M)]

        heap = []  # Priority queue

        for i in range(M):
            for j in range(N):
                current_word = matrix[i][j]
                if current_word in dictionary:
                    heapq.heappush(heap, (current_word, i, j, [current_word]))

        while heap:
            current_word, x, y, path = heapq.heappop(heap)
            visited[x][y] = True

            if current_word in dictionary:
                valid_words.add(current_word)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid_cell(nx, ny):
                    new_word = current_word + matrix[nx][ny]
                    new_path = path + [new_word]
                    heapq.heappush(heap, (new_word, nx, ny, new_path))

            visited[x][y] = False

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
