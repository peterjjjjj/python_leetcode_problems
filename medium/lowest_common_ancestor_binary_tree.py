class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_command_ancestor(p: Treenode, q: Treenode, root: Treenode) -> Treenode:

    def dfs(node: Treenode) -> Treenode:
        #if found one of the target nodes
        if node.val == q.val or node.val == p.val:
            return True

        if node is None:
            return False

        if dfs(node.left) and dfs(node.right):
            return node

    return dfs(root)



if __name__ == '__main__':
    test = Treenode(3)
    test.left = Treenode(5)
    test.right = Treenode(1)
    test.left.left = Treenode(6)
    test.left.right = Treenode(2)
    test.left.right.left = Treenode(7)
    test.left.right.right = Treenode(4)
    test.right.left = Treenode(0)
    test.right.right = Treenode(8)
    print(lowest_command_ancestor(test.left, test.right, test).val)