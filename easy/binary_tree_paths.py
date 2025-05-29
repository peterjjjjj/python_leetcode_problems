class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_paths(root:TreeNode) -> list[str]:
    paths = []
    side_path = []

    def dfs(node:TreeNode):
        nonlocal paths, side_path
        if node is None:
            return

        side_path.append(str(node.val))

        if node.left is None and node.right is None:
            paths.append(str(side_path))

        dfs(node.left)
        dfs(node.right)
        side_path.pop()

    dfs(root)

    return paths

if __name__ == '__main__':
    test_tree = TreeNode(1)
    test_tree.left = TreeNode(2)
    test_tree.right = TreeNode(3)
    test_tree.left.left = TreeNode(5)
    print(tree_paths(test_tree))