class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_BST(root: TreeNode) -> bool:

    def dfs(node: TreeNode) -> bool:

        if not node:
            return True

        if node.left and node.right:
            if not node.left.val < node.val < node.right.val:
                return False


        left = dfs(node.left)
        right = dfs(node.right)

        if right and left:
            return True


    return dfs(root)

if __name__ == '__main__':
    test = TreeNode(2)
    test.left = TreeNode(1)
    test.right = TreeNode(3)

    print(is_valid_BST(test))




