class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree_dfs(root: TreeNode) -> TreeNode:
    if root is None:
        return

    root.left, root.right = root.right, root.left
    invert_tree_dfs(root.left)
    invert_tree_dfs(root.right)

    return root

if __name__ == "__main__":
    test = TreeNode(2)
    test.left = TreeNode(1)
    test.right = TreeNode(3)
    print(invert_tree_dfs(test))
    print('1')