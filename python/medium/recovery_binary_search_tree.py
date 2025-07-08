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

    def in_order_traversal(node: TreeNode, previous_node = None) -> None:
        if node is None:
            return

        in_order_traversal(node.left, previous_node)

        if previous_node is None:
            previous_node = node

        elif previous_node.val > node.val:
            previous_node.val, node.val = node.val, previous_node.val

        in_order_traversal(node.right, previous_node)

    in_order_traversal(root)


if __name__ == '__main__':
    test_root = TreeNode(2)
    test_root.left = TreeNode(3)
    test_root.right = TreeNode(1)
    recover_binary_search_tree(test_root)
    print()


