class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generate_trees(n: int) -> list[TreeNode]:
    """
    Given an integer n, return all the structurally unique BST which has exactly n elements.

    :param n: integer
    :return: list[TreeNode]
    """

    if n == 0:
        return []

    def dfs(start: int, end: int) -> list[TreeNode]:
        all_trees_for_range = []

        if start > end:
            return [None]

        if start == end:
            return [TreeNode(start)]

        for i in range(start, end+1):
            left_sub_trees = dfs(start, i - 1)
            right_sub_trees = dfs(i + 1, end)

            for left_tree in left_sub_trees:
                for right_tree in right_sub_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree

                    all_trees_for_range.append(root)

        return all_trees_for_range

    return dfs(1, n)

if __name__ == '__main__':
    print(generate_trees(3))


