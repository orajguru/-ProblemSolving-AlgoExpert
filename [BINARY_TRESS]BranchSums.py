class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    def dfs(node, curr_sum, results):
        if node is None:
            return
        curr_sum += node.value
        if not node.left and not node.right:
            results.append(curr_sum)
            return
        dfs(node.left, curr_sum, results)
        dfs(node.right, curr_sum, results)
    results = []
    dfs(root, 0, results)
    return results
