from isrlab_project.ReadConfig import ReadConfig
import numpy as np


class Graph:
    _graph: dict
    _visited: set
    _queue: list
    _actual_node: tuple
    _radius: float

    def __init__(self, start_node):
        self._radius = ReadConfig().read_data("SPACE")/2
        self._graph = {start_node: []}

    def add_node(self, node_from: tuple, new_node: tuple):
        self._graph[node_from].append(new_node)
        self._graph[new_node] = [node_from]
        self._visited.add(new_node)
        self._queue.append(new_node)

    def is_node_new(self, node_from: tuple, new_node: tuple):
        distance = np.sqrt((new_node[0]-node_from[0])**2 + (new_node[1]-node_from[1])**2)
        return distance > self._radius

    def get_next_node(self):
        return self._queue[-1]

    def path_to_next_node(self, arrive_node: tuple):
        visited = {self._actual_node}
        queue = [self._actual_node]
        tree = {}
        while len(queue) > 0:
            node_v = queue.pop(0)
            visited.add(node_v)
            for node_u in self._graph[node_v]:
                if node_u not in visited:
                    queue.append(node_u)
                    visited.add(node_u)
                    tree[node_u] = node_v
                    if node_u == arrive_node:
                        path = []
                        while node_u in tree:
                            path.insert(0, node_u)
                            node_u = tree[node_u]
                        path.insert(0, node_u)
                        return path
            return []
