from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode, depth=0) -> int:
    if root is None:
        return depth

    left_depth = max_depth(root.left, depth+1)
    right_depth = max_depth(root.right, depth+1)

    return max(left_depth, right_depth)

def max_depth_bfs(root: TreeNode) -> int:
    queue = deque()
    queue.append(root)
    visited = set()
    depth = 0

    while queue:
        depth += 1
        current_level_size = len(queue)

        #clear current level
        for _ in range(current_level_size):
            current_node = queue.popleft()
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    return depth

if __name__ == "__main__":
    test = TreeNode(3)
    test.left = TreeNode(9)
    test.right = TreeNode(20)
    test.right.left = TreeNode(15)
    test.right.right = TreeNode(7)
    print(max_depth(test))
    print(max_depth_bfs(test))

