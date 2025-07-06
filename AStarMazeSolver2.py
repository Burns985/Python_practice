from heapq import heappop, heappush

maze = [
    [' ', ' ', 'w', ' ', 'x', 'y'],
    ['r', 's', 't', 'u', ' ', 'v'],
    ['m', 'n', ' ', 'o', 'p', 'q'],
    ['h', 'i', 'j', ' ', 'k', 'l'],
    ['f', 'g', ' ', ' ', ' ', ' '],
    ['a', ' ', 'b', 'c', 'd', 'e']
]

start = (5, 0)
goal = (0, 5)


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_search(graph, start, goal):
    queue = []
    heappush(queue, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while queue:
        current_cost, current_node = heappop(queue)

        if current_node == goal:
            break

        for next_node in neighbors(graph, current_node):
            new_cost = cost_so_far[current_node] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(goal, next_node)
                heappush(queue, (priority, next_node))
                came_from[next_node] = current_node

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


def neighbors(graph, node):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = []
    for dir in dirs:
        x, y = node[0] + dir[0], node[1] + dir[1]
        if 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] != 'w':
            result.append((x, y))
    return result


result_path = astar_search(maze, start, goal)
print("Resulting Path:")
for node in result_path:
    print(node)
