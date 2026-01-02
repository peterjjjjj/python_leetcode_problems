#Recursion DFS, BFS, iterative DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recursive_DFS(root: TreeNode) -> int:

    def helper(node: TreeNode, depth: int) -> int:
        if not node:
            return depth

        left = helper(node.left, depth + 1)
        right = helper(node.right, depth + 1)
        return max(left, right)

    return helper(root, 0)

if __name__ == "__main__":
    testcase = TreeNode(3)
    testcase.left = TreeNode(9)
    testcase.right = TreeNode(20)
    testcase.right.left = TreeNode(15)
    testcase.right.right = TreeNode(7)
    print(recursive_DFS(testcase))