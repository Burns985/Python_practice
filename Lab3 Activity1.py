class Node:
    def __init__(self, state, parent, actions, total_cost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.total_cost = total_cost


def breadth_search():
    initial_position = input('Please provide a starting node: ')
    goal = input('Please provide a goal node: ')
    frontier = [initial_position]
    explored = set()

    while frontier:
        current = frontier.pop(0)
        explored.add(current)
        print(current)
        if current == goal:
            return construct_path(graph, initial_position, goal)

        for child_state in graph[current].actions:
            if child_state not in frontier and child_state not in explored:
                graph[child_state].parent = current
                frontier.append(child_state)

    print("Goal not reached.")
    return None


def construct_path(graph, initial_state, goal_state):
    path = []
    current_state = goal_state
    while current_state != initial_state:
        path.append(current_state)
        current_state = graph[current_state].parent
    path.append(initial_state)
    path.reverse()
    return path


graph = {
    'A': Node("A", None, ['B', 'C', 'E'], None),
    'B': Node("B", None, ['A', 'D', 'E'], None),
    'C': Node("C", None, ['A', 'F', 'G'], None),
    'D': Node("D", None, ['B', 'E'], None),
    'E': Node("E", None, ['A', 'B', 'D'], None),
    'F': Node("F", None, ['C'], None),
    'G': Node("G", None, ['C'], None),
}

path = breadth_search()
if path:
    print("Path found:", ' -> '.join(path))
else:
    print("No path found.")

