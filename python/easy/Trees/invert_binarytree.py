from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree_dfs(root: TreeNode) -> TreeNode:
    if root is None:
        return

    root.left, root.right = root.right, root.left
    invert_tree_dfs(root.left)
    invert_tree_dfs(root.right)

    return root

def invert_tree_bfs(root: TreeNode) -> TreeNode:
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft()

        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

        current_node.left, current_node.right = current_node.right, current_node.left

    return root


if __name__ == "__main__":
    test = TreeNode(2)
    test.left = TreeNode(1)
    test.right = TreeNode(3)
    print(invert_tree_dfs(test))
    print(invert_tree_bfs(test))
    print('1')