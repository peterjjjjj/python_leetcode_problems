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
    if not root:
        return

    current_node_value = root.val

    def in_order_traversal_left(node: TreeNode) -> None:
        nonlocal root
        if node is None:
            return

        in_order_traversal_left(node.left)

        if node.val == current_node_value:
            return

        if current_node_value < node.val:
            root.val, node.val = node.val, root.val
            return

        in_order_traversal_left(node.right)

    def in_order_traversal_right(node: TreeNode) -> None:
        nonlocal root
        if node is None:
            return

        in_order_traversal_right(node.right)

        if node.val == current_node_value:
            return

        if current_node_value > node.val:
            root.val, node.val = node.val, root.val
            return

        in_order_traversal_right(node.left)

    in_order_traversal_left(root)
    in_order_traversal_right(root)




if __name__ == '__main__':
    test_root = TreeNode(1)
    test_root.left = TreeNode(2)
    test_root.right = TreeNode(3)
    result = recover_binary_search_tree(test_root)
    print(result)


