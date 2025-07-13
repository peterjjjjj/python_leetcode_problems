from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view_bfs(root: TreeNode) -> list[int]:
    numbers = []
    if not root:
        return numbers

    current_queue = deque()
    current_queue.append(root)

    while current_queue:
        numbers.append(current_queue[0].val)

        for _ in range(len(current_queue)):
            current_node = current_queue.popleft()
            if current_node.right is not None:
                current_queue.append(current_node.right)
            if current_node.left is not None:
                current_queue.append(current_node.left)


    return numbers

if __name__ == '__main__':
    test = TreeNode(1)
    test.left = TreeNode(2)
    test.right = TreeNode(3)
    test.left.left = TreeNode(5)
    test.right.right = TreeNode(4)
    print(right_side_view_bfs(test))