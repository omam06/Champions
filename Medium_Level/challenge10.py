def has_path(graph, start, target):
    visited = set()
    stack = [start]

    while stack != []:
        node = stack.pop()

        if node == target:
            return True

        if node not in visited:
            visited.add(node)

            for each_node in graph[node]:
                if each_node not in visited:
                    stack.append(each_node)

    return False

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(has_path(graph, "A", "F"))
print(has_path(graph, "D", "A"))