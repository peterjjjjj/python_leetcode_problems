#DFS, recursion
from unittest import TestCase

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def DFS(root: TreeNode) -> list[str]:
    paths = []

    def helper(node: TreeNode, curr_path: list[int]) -> None:
        nonlocal paths

        #Basecase
        if not node:
            return

        curr_path.append(node.val)

        #Leaf found
        if not node.left and not node.right:
            paths.append(list(curr_path))
            curr_path.pop()
            return

        helper(node.left, curr_path)
        helper(node.right, curr_path)
        curr_path.pop()

    helper(root, [])
    return paths


if __name__ == "__main__":
    testcase = TreeNode(1)
    testcase.left = TreeNode(2)
    testcase.right = TreeNode(3)
    testcase.left.right = TreeNode(5)
    print(DFS(testcase))



