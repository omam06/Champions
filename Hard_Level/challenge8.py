def shortest_path(graph, start, target):
    if start == target:
        return [start]

    queue = [start]
    visited = {start}
    parent = {}

    while queue != []:
        rmv_node = queue.pop(0)
        for all_neighbors in graph[rmv_node]:
            if all_neighbors not in visited:
                visited.add(all_neighbors)
                parent[all_neighbors] = rmv_node

                if all_neighbors == target:
                    path = []
                    current = target

                    while current is not None:
                        path.append(current)
                        current = parent.get(current)

                    path.reverse()
                    return path
                queue.append(all_neighbors)
    return None

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print(shortest_path(graph, "A", "F"))
print(shortest_path(graph, "C", "F"))