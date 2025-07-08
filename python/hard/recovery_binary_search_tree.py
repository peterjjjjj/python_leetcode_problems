class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recover_binary_search_tree(root: TreeNode) -> None:
    """
    Correct the given tree by swapping the 2 nodes that were in the wrong places.

    :param root: Tree to be correct.
    :return: None
    """

    def bst(node: TreeNode) -> TreeNode:
        if not node:
            return None

        if node.left:
            if node.val < node.left.val:
                node.val, node.left.val = node.left.val, node.val


        if node.right:
            if node.val > node.right.val:
                node.val, node.right.val = node.right.val, node.val

        bst(node.left)
        bst(node.right)

        return node

    bst(root)

if __name__ == '__main__':
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    result = recover_binary_search_tree(test_root)
    print(result)


