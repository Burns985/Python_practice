maze = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0]
]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_valid(x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def hill_climbing(start, goal):
    current = start
    path = [current]
    cost = 0

    while current != goal:
        neighbors = []
        for dx, dy in directions:
            next_node = current[0] + dx, current[1] + dy
            if is_valid(*next_node):
                neighbors.append(next_node)

        if not neighbors:
            break

        next_node = min(neighbors, key=lambda x: manhattan_distance(x, goal))
        if manhattan_distance(next_node, goal) >= manhattan_distance(current, goal):
            break

        current = next_node
        cost += 1
        path.append(current)

    return path, cost


if __name__ == '__main__':
    start = (0, 0)
    goal = (9, 9)

    path, cost = hill_climbing(start, goal)

    print("Path:", path)
    print("Cost:", cost)
