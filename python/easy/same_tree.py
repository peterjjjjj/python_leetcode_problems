class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test2 = TreeNode(1)
    test2.left = TreeNode(2)
    test2.right = TreeNode(3)
    print(is_same_tree(test, test2))