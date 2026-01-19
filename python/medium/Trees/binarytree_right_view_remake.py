from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def

if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test.left.left = TreeNode(5)
    test.right.right = TreeNode(4)
