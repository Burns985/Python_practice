graph = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}


def dfs(graph, start, goal):
    stack = [(start, [start], 0)]
    visited = set()

    while stack:
        current, path, total_distance = stack.pop()
        visited.add(current)

        if current == goal:
            return path, total_distance

        for neighbor, distance in graph.get(current, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_distance = total_distance + distance
                stack.append((neighbor, new_path, new_distance))

    return None, 0


start_city = 'Arad'
goal_city = 'Bucharest'
shortest_path, total_distance = dfs(graph, start_city, goal_city)

if shortest_path:
    print("Shortest path from {} to {}: {}".format(start_city, goal_city, shortest_path))
    print("Total distance: {} km".format(total_distance))
else:
    print("There is no path from {} to {}.".format(start_city, goal_city))
