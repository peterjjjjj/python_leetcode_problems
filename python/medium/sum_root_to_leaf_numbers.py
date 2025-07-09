class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_root_to_leaf_numbers(root: TreeNode) -> int:
    """
    Return the sum of the path from

    :param root:
    :return:
    """

    all_paths = []

    def dfs(node: TreeNode, path: list) -> None:
        nonlocal all_paths

        path.append(node.val)

        if node.left is None and node.right is None:
            all_paths.append(path[:])
            return


        dfs(node.left, path)
        path.pop()
        dfs(node.right, path)
        path.pop()

    dfs(root, [])

    all_paths_sum = 0

    for path in all_paths:
        for i in range(len(path)):
            all_paths_sum += (10 ** (len(path) - i - 1)) * path[i]


    return all_paths_sum


if __name__ == '__main__':
    tree = TreeNode(4)
    tree.left = TreeNode(9)
    tree.left.left = TreeNode(5)
    tree.left.right = TreeNode(1)
    tree.right = TreeNode(0)
    print(sum_root_to_leaf_numbers(tree))



