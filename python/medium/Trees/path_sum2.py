class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum2(root: TreeNode, target_sum: int) -> list[list[int]]:

    all_paths = []
    path = []

    def dfs(node: TreeNode, current_sum=0):
        nonlocal all_paths, path

        if node is None:
            return

        current_sum += node.val
        path.append(node.val)


        if current_sum == target_sum and node.left is None and node.right is None:
            all_paths.append(path[:])


        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

        path.pop()

    dfs(root)

    return all_paths



if __name__ == '__main__':
    test = TreeNode(5)
    test.left = TreeNode(4)
    test.right = TreeNode(8)
    test.left.left = TreeNode(11)
    test.left.left.left = TreeNode(7)
    test.left.left.right = TreeNode(2)
    test.right.left = TreeNode(13)
    test.right.right = TreeNode(4)
    test.right.right.left = TreeNode(5)
    test.right.right.right = TreeNode(1)
    print(path_sum2(test, 22))



