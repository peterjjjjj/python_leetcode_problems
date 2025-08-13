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
    dp = [0]
    i = 0
    max_sum = 0

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

        #If including the current node would make the path larger.
        #Update the max_sum and dp list.
        if dp[i - 1] + node.val >+ max_sum:
            max_sum = dp[i - 1] + node.val
            dp[i] = max_sum

        dfs(node.right)

    dfs(root)

    return max_sum



if __name__ == '__main__':
    tree = TreeNode(-10)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    print(max_path_sum(tree))