class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_BST(root: TreeNode) -> bool:

    def dfs(node: TreeNode, left_bound = -float('INF'), right_bound = float('INF')) -> bool:

        if not node:
            return True

        if node.val < left_bound or node.val > right_bound:
            return False

        left = dfs(node.left, left_bound, node.val)
        right = dfs(node.right, node.val, right_bound)

        return left and right

    return dfs(root)


if __name__ == '__main__':
    test = TreeNode(2)
    test.left = TreeNode(1)
    test.right = TreeNode(3)

    print(is_valid_BST(test))




