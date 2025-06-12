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


        if current_sum == target_sum:
            all_paths.append(path[:])
            return

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

        path.pop()

    dfs(root)

    return all_paths





if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    print(path_sum2(test, 3))


