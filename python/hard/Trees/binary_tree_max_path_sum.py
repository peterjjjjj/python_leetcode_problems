class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode) -> int:
    """
    LC 124.
    """

    sum = 0

    def dfs(node: TreeNode) -> None:
        nonlocal sum
        if node is None:
            return

        sum += node.val

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return sum


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    print(max_path_sum(tree))