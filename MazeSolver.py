def solve_maze(maze):
    def is_valid(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start_x, start_y = i, j

    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1]
        if maze[x][y] == 'G':
            return maze

        if maze[x][y] == ' ':
            maze[x] = maze[x][:y] + 'X' + maze[x][y + 1:]

        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        found = False
        for nx, ny in neighbors:
            if is_valid(nx, ny) and maze[nx][ny] not in ['X', 'S']:
                stack.append((nx, ny))
                found = True
                break

        if not found:
            stack.pop()

    return "No path found"


maze = [
    "#####G##",
    "#      #",
    "# #### #",
    "# #S#  #",
    "# # ## #",
    "# # #  #",
    "#      #",
    "########"
]

solution = solve_maze(maze)

if solution != "No path found":
    for row in solution:
        print(row)
else:
    print("No path found")
