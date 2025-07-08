class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recover_binary_search_tree(root: TreeNode) -> None:
    """
    Correct the given tree by swapping the 2 nodes that were in the wrong places.
    Time Complexity: O(N)
    Space Complexity: O(N)

    :param root: Tree to be correct.
    :return: None
    """

    #these variables are declared outside to maintain state across recursive calls
    previous_node = None
    first_error_node = None
    second_error_node = None

    def in_order_traversal(node: TreeNode) -> None:
        nonlocal previous_node, first_error_node, second_error_node
        if node is None:
            return

        in_order_traversal(node.left)

        #identify the first misplaced node based on the previous node
        #if there is only 1 misplaced node, swap with it's next node
        #is there is a second node, instead of swapping the node next to the first node, swap with second

        #if we found a misplaced node
        if previous_node is not None and previous_node.val > node.val:
            #and it's the first node found
            if first_error_node is None:
                first_error_node = previous_node

            second_error_node = node

        previous_node = node

        in_order_traversal(node.right)

    in_order_traversal(root)

    first_error_node.val, second_error_node.val = second_error_node.val, first_error_node.val


if __name__ == '__main__':
    test_root = TreeNode(1)
    test_root.left = TreeNode(3)
    test_root.right = TreeNode(2)
    recover_binary_search_tree(test_root)
    print()


