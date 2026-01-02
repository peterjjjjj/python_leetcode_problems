class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

#Interation: longest left+right
def find_diameter(root: TreeNode) -> int:

    #Recursion to find max depth each side
    def helper(node: TreeNode, depth: int) -> int:
        if not node:
            return depth

        left = helper(node.left, depth + 1)
        right = helper(node.right, depth + 1)
        return max(left, right)

    diameter = helper(root.left, 0) + helper(root.right, 0)
    return diameter


if __name__ == '__main__':
    test_tree = TreeNode(1)
    test_tree.left = TreeNode(2)
    test_tree.right = TreeNode(3)
    test_tree.left.left = TreeNode(4)
    test_tree.left.right = TreeNode(5)
    print(find_diameter(test_tree))
