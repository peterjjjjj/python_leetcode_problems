def isBipartite(graph: list[list[int]]) -> bool:
    """
    There is an undirected graph with n nodes, where each node is numbered between 0 and n-1.
    A graph is bipartite if the nodes can be partitioned into two independent sets A and B,
    Such that every edge in the graph connects a node in set A and a node in set B.

    :param graph:
    :return:
    """

    #A dict that stores all the colour
    nodes_set = dict()

    def dfs(current_node: int, current_set: int) -> bool:
        #If current node has been recorded.
        if current_node in nodes_set:
            #And the previous record has different value.
            if nodes_set[current_node] != current_set:
                return False

            return True

        #Mark the current node with the set number.
        nodes_set[current_node] = current_set

        #Loop through all neighbors next to current_node.
        for neighbor_node in graph[current_node]:
            #Use bitwise to switch between 1 and 0.
            if not dfs(neighbor_node, (current_set ^ 1)):
                return False

        return True

    #In case not all nodes are connected.
    for i in range(len(graph)):
        if i not in nodes_set:
            if not dfs(i, 0):
                return False

    return True


if __name__ == '__main__':
    print(isBipartite([ [1,2,3], [0,2], [0,1,3], [0,2] ]))






