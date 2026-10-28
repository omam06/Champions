def has_path(graph, start, target):
    Create an empty set called visited
    Create a stack containing start

    while tack is not empty:
        Remove a node from the stack

        if node equals target:
            return True

        if node has not been visited:
            Add node to visited

            for each neighbor of node:
                if neighbor has not been visited:
                    Add neighbor to stack

    return False