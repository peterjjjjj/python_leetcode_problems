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

    trees_list = []

    def dfs(start: int, end: int) -> TreeNode:
        nonlocal trees_list
        if start == end:
            return TreeNode(start)

        if start > end:
            return None

        for i in range(start, end+1):
            tree = TreeNode(i)
            tree.left = dfs(start, i-1)
            tree.right = dfs(i+1, end)
            trees_list.append(tree)

    dfs(1, n)
    return trees_list

if __name__ == '__main__':
    print(generate_trees(3))


