class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode, k: int) -> int:
    """
    LC 230.

    """

    #Use a list cuz it's mutable.
    def bst(node: TreeNode, count: list[int]) -> int:
        if node is None:
            return

        value = bst(node.left, count)

        count[0] -= 1
        if count[0] == 0:
            return node.val
        if value is not None:
            return value

        value = bst(node.right, count)

        #If k in right branch.
        if value is not None:
            return value

    result = bst(root, [k])

    if result is None:
        raise ValueError("k is out of range for the given tree.")

    return result


if __name__ == '__main__':
    test_tree = TreeNode(3)
    test_tree.left = TreeNode(1)
    test_tree.right = TreeNode(4)
    test_tree.left.right = TreeNode(2)
    print(kth_smallest(test_tree, 4))

