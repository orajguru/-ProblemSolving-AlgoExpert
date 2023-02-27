def nodeDepths(root, depth = 0):
    if root != None:
        depth += nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
    else:
        return 0
    return depth

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
