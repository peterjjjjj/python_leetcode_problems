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

    #If a tree is   1
    #             2   3
    #There are 2 paths, 1 -> 2, 1 ->3
    #Sum would be 12 + 13 = 25

    #List to hold all paths from root to leaf
    all_paths = []

    def dfs(node: TreeNode, current_path: list) -> None:
        nonlocal all_paths

        #Append node value to current path
        current_path.append(node.val)

        #Node found
        if node.left is None and node.right is None:
            all_paths.append(current_path[:])
            return

        #If left and right node exist
        if node.left:
            dfs(node.left, current_path)
            current_path.pop()
        if node.right:
            dfs(node.right, current_path)
            current_path.pop()

    dfs(root, [])

    all_paths_sum = 0

    for path in all_paths:
        all_paths_sum += int(''.join(map(str, path)))


    return all_paths_sum


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    print(sum_root_to_leaf_numbers(tree))



