def path_to_next_node(graph, current_node: tuple, arrive_node: tuple):
    visited = {current_node}
    queue = [current_node]
    tree = {}
    while len(queue) > 0:
        node_v = queue.pop(0)
        visited.add(node_v)
        for node_u in graph[node_v]:
            if node_u not in visited:
                queue.append(node_u)
                visited.add(node_u)
                tree[node_u] = node_v
                if node_u == arrive_node:
                    path = []
                    while node_u in tree:
                        path.insert(0, node_u)
                        node_u = tree[node_u]
                    #path.insert(0, node_u)  # forse va tolto
                    return path
    return []


if __name__ == '__main__':
    graph = {(0, 0): [(0, 1), (1, 0), (1, 1)],
             (0, 1): [(0, 0)],
             (1, 0): [(0, 0)],
             (1, 1): [(0, 0)]}

    current_node = (0, 0)
    arrive_node = (1, 1)

    print(path_to_next_node(graph, current_node, arrive_node))
