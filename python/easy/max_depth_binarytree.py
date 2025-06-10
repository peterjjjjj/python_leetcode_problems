class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode, depth=0) -> int:
    if root is None:
        return depth

    left_depth = max_depth(root.left, depth+1)
    right_depth = max_depth(root.right, depth+1)

    return max(left_depth, right_depth)

if __name__ == "__main__":
    test = TreeNode(3)
    test.left = TreeNode(9)
    test.right = TreeNode(20)
    test.right.left = TreeNode(15)
    test.right.right = TreeNode(7)
    print(max_depth(test))

