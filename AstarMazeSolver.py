from queue import PriorityQueue

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


def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not pq.empty():
        current_cost, current_node = pq.get()

        if current_node == goal:
            break

        for dx, dy in directions:
            next_node = current_node[0] + dx, current_node[1] + dy
            new_cost = cost_so_far[current_node] + 1

            if is_valid(*next_node) and (next_node not in cost_so_far or new_cost < cost_so_far[next_node]):
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                pq.put((priority, next_node))
                came_from[next_node] = current_node

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path, cost_so_far[goal]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    start = (0, 0)
    goal = (9, 9)

    path, cost = astar(start, goal)

    print("Path:", path)
    print("Cost:", cost)
