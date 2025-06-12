class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_command_ancestor(p: TreeNode, q: TreeNode, root: TreeNode) -> TreeNode:
    """
    O(N) worst case
    O(H) height
    :param p:
    :param q:
    :param root:
    :return:
    """

    def dfs(node: TreeNode) -> TreeNode:

        #base case when reached end of the tree
        if node is None:
            return None

        #when found both target nodes
        if node == p or node == q:
            return node

        #left branch
        left = dfs(node.left)
        #right branch
        right = dfs(node.right)

        #if one on each branch
        if left and right:
            return node

        #if both on left branch
        if left and not right:
            return left
        #on right branch
        if right and not left:
            return right

    return dfs(root)



if __name__ == '__main__':
    test = TreeNode(3)
    test.left = TreeNode(5)
    test.right = TreeNode(1)
    test.left.left = TreeNode(6)
    test.left.right = TreeNode(2)
    test.left.right.left = TreeNode(7)
    test.left.right.right = TreeNode(4)
    test.right.left = TreeNode(0)
    test.right.right = TreeNode(8)
    print(lowest_command_ancestor(test.left, test.right, test).val)