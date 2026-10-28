def count_leaves(root):
    if root is None:
        return 0

    if root has no left child and no right child:
        return 1

    left_count = count_leaves(root.left)
    right_count = count_leaves(root.right)

    return left_count + right_count