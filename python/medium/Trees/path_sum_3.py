from collections import defaultdict


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
    #Hasmap to track past cumulative sums.
    #And backtrack in the recursion.

    path_count = 0
    map = defaultdict(int)
    map[0] = 1

    def dfs(node: TreeNode, current_sum: int) -> None:
        nonlocal path_count

        if node is None:
            return

        #The cumulative sum from root to node.
        current_sum += node.val

        #The required_sum is the cumulative sum from the root to a node,
        #Such that can be taken out and so the rest of the path is equal to target.
        required_sum = current_sum - target_sum
        if required_sum in map:
            path_count += map[required_sum]

        #Update the map with the cumulative sum from root to node.
        map[current_sum] += 1

        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

        #Backtrack, take the cumulative sum out of the map.
        map[current_sum] -= 1

    dfs(root, 0)

    return path_count

if __name__ == '__main__':
    test1 = TreeNode(10)
    test1.left = TreeNode(5)
    test1.right = TreeNode(-2)
    test1.right.left = TreeNode(10)
    test1.right.right = TreeNode(0)
    test1.right.right.left = TreeNode(8)
    test1.left.left = TreeNode(3)
    test1.left.right = TreeNode(3)

    print(path_sum(test1, 8))