def findClosestValueInBst(tree, target):
    node = tree
    closest = float("inf")

    while node is not None: 
        closest = node.value if abs(node.value - target) < abs(closest - target) else closest
        if node.value < target:
            node = node.right
        else:    
            node = node.left
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
