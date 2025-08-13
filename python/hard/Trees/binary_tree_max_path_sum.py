import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode) -> int:
    """
    LC 124.
    """

    max_sum = -math.inf

    def dfs(node: TreeNode) -> int:
        nonlocal max_sum

        if node is None:
            return 0

        left_sum = max(dfs(node.left), 0)
        right_sum = max(dfs(node.right), 0)

        current_path_sum = node.val + left_sum + right_sum

        max_sum = max(max_sum, current_path_sum)

        return node.val + max(left_sum, right_sum)

    dfs(root)

    return max_sum



if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(-2)
    tree.right = TreeNode(-3)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(-2)
    tree.left.left.left = TreeNode(-1)
    print(max_path_sum(tree))