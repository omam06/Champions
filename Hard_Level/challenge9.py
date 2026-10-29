def is_valid_bst(root):
    def helper(node, lower, upper):

        if node is None:
            return True

        value = node[0]
        if value <= lower or value >= upper:
            return False

        if not helper(node[1], lower, value):
            return False

        if not helper(node[2], value, upper):
            return False

        return True
    return helper(root, float("-inf"), float("inf"))

root1 = [
    8, 
    [3, [1, None, None],[6,None, None]],
    [10, None, [14, None, None]]
]

root2 = [
    8,
    [3, None, None],
    [10, [4, None, None]]
]

print(is_valid_bst(root1))
print(is_valid_bst(root2))