class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode) -> int:
    """
    LC 124.
    """

    #Initialize the dp table.
    dp = [root.val]
    i = 0
    max_sum = root.val

    def dfs(node: TreeNode) -> None:
        nonlocal max_sum, dp, i

        if node is None:
            return

        #Use inorder to make sure that all the nodes are linked.
        dfs(node.left)

        #Append an 0 to the dp list.
        dp.append(0)
        #Increment index.
        i += 1

        current_path_sum = dp[i - 1] + node.val

        if node.val > current_path_sum:
            max_sum = node.val
            dp[i] = max_sum

        elif current_path_sum >= max_sum:
            max_sum = dp[i - 1] + node.val
            dp[i] = max_sum

        dfs(node.right)

    dfs(root)

    return max_sum



if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(-2)
    tree.right = TreeNode(3)
    print(max_path_sum(tree))