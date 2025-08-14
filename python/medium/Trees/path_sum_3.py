class TreeNode:
    def __init__ (self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def path_sum(root: TreeNode, target_sum: int) -> int:
    """
    LC 437.

    """

    #Use preorder for the dfs to track the current sum.
    #Hasmap to track past sums.
    #And backtrack in the recursion.

    path_count = 0
    map = [0]
    i = 0

    def dfs(node: TreeNode) -> None:
        nonlocal path_count, i, map

        i += 1

        map.append(node.val)

        for j in range(i):
            current_sum = node.val + map[j]
            if current_sum == target_sum:
                path_count += 1

        if node.left is not None:
            dfs(node.left)
        if node.right is not None:
            dfs(node.right)

        map.pop()
        i -= 1


    dfs(root)

    return path_count

if __name__ == '__main__':
    test1 = TreeNode(10)
    test1.left = TreeNode(5)

    print(path_sum(test1, 8))