class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def path_sum(root: TreeNode, target: int) -> bool:
    if root is None:
        return False

    remaining_target = target - root.val

    if root.left is None and root.right is None:
        return remaining_target == 0

    left_sum = path_sum(root.left, remaining_target)
    right_sum = path_sum(root.right, remaining_target)

    return left_sum or right_sum


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    print(path_sum(root, 22))






