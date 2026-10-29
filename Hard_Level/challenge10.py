def has_cycle(graph):
    visiting = set()
    visited = set()

    def helper(node):
        if node in visiting:
            return True

        if node in visited:
            return False

        visiting.add(node)

        for each_neighbor in graph[node]:
            if helper(each_neighbor) is True:
                return True

        rmv_node = visiting.remove(node)
        visited.add(rmv_node)

        return False

    for each_node in graph:
        if helper(each_node):
            return True

    return False


graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}
print(has_cycle(graph))