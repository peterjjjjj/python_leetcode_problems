class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def diameter(root):
    """
    O(n)
    O(H), height of depth
    :param root:
    :return:
    """
    max_depth = 0

    def calculate_depth(node):
        nonlocal max_depth
        if node is None:
            return 0

        #call the nodes recursively, inorder left mid right
        left_depth = calculate_depth(node.left)
        right_depth = calculate_depth(node.right)

        #left_depth + right_depth because one of them is gonna be 0
        max_depth = max(max_depth, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)

    calculate_depth(root)

    return max_depth

if __name__ == '__main__':
    test_tree = TreeNode(1)
    test_tree.left = TreeNode(2)
    test_tree.right = TreeNode(3)
    test_tree.left.left = TreeNode(4)
    test_tree.left.right = TreeNode(5)
    print(diameter(test_tree))