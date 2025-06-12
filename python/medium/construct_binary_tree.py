from distutils.command.build import build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    if len(preorder) == 0:
        return None

    root = TreeNode(preorder[0])

    #with the place of root in inorder we can tell what are the nodes on the left and on the right
    root_index = inorder.index(root.val)

    root.left = build_tree(preorder[1:root_index + 1], inorder[:root_index])
    root.right = build_tree(preorder[root_index + 1:], inorder[root_index + 1:])

    return root

if __name__ == '__main__':
    root = (build_tree([3,9,20,15,7], [9,3,15,20,7]))
    print(build_tree([3,9,20,15,7], [9,3,15,20,7]))