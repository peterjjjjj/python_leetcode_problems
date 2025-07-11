from turtledemo.penrose import start


def paths_to_target(graph: list[list[int]]) -> list[list[int]]:
    """
    Given a directed acyclic graph of n nodes, find all paths from node 0 to n-1 in any order.

    :param graph:list[list[int]] DAG
    :return: list[list[int]] paths
    """

    all_paths = []
    target_vertex = len(graph) - 1

    #Path is the vector from current vertex to the next vertex.
    def dfs(current_vertex: int, current_path = []) -> None:
        nonlocal all_paths

        #Update the current_path.
        current_path.append(current_vertex)

        #Found path, update to all_paths, return.
        if current_vertex == target_vertex:
            all_paths.append(current_path[:])
            return

        #Base case, no further path, return.
        elif not graph[current_vertex]:
            return

        for next_vertex in graph[current_vertex]:
            dfs(next_vertex, current_path)
            current_path.pop()


    dfs(0)

    return all_paths

if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    print(paths_to_target(graph))