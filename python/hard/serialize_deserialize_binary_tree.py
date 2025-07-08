class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root: TreeNode) -> str:
    """
    Take the root of a binary tree as input and converts it into a single string

    :param root: TreeNode
    :return: string
    """

    #empty root
    if not root:
        return ''


    serialized_str = ''
    serialized_list = []

    def preorder(node: TreeNode) -> None:
        nonlocal serialized_list

        #if the current node has leaf nodes, append val, call recursion
        if node:
            serialized_list.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        else:
            serialized_list.append('None')

    preorder(root)

    serialized_str = ','.join(serialized_list)

    return serialized_str

def deserialize(data: str) -> TreeNode:
    """
    Take a string and convert it into a binary tree

    :param data: string
    :return: TreeNode
    """

    if not data:
        return TreeNode(None)

    treepath_list = data.split(',')

    def preorder_transversal(node_value: str) -> TreeNode:
        nonlocal treepath_list
        if node_value == 'None':
            return

        node = TreeNode(int(node_value))
        node.left = preorder_transversal(treepath_list.pop(0))
        node.right = preorder_transversal(treepath_list.pop(0))

        return node

    tree = preorder_transversal(treepath_list.pop(0))

    return tree



if __name__ == '__main__':
    test_tree = TreeNode(1)
    test_tree.left = TreeNode(2)
    test_tree.right = TreeNode(3)
    test_tree.right.left = TreeNode(4)
    test_tree.right.right = TreeNode(5)
    print(serialize(test_tree))
    string = serialize(test_tree)
    print(deserialize(string))
