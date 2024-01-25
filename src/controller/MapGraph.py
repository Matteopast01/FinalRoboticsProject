from isrlab_project.ReadConfig import ReadConfig
import numpy as np


class MapGraph:
    _graph: dict
    _visited: set
    _queue: list
    _current_node: tuple
    _radius: float
    _node_distance_threshold: float

    def __init__(self, start_node):
        self._radius = ReadConfig().read_data("SPACE")/2
        self._node_distance_threshold = ReadConfig().read_data("NODE_DISTANCE_THRESHOLD")
        self._graph = {start_node: []}
        self._visited.add(start_node)
        self._queue.append(start_node)

    def add_node(self, node_from: tuple, new_node: tuple):
        self._graph[node_from].append(new_node)
        self._graph[new_node] = [node_from]
        self._visited.add(new_node)
        self._queue.append(new_node)

    def set_current_node(self, current_node):
        self._current_node = current_node

    def is_nodes_position_equals(self, node1, node2):
        distance = np.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)
        return distance < self._node_distance_threshold

    def is_node_new(self, node_from: tuple, new_node: tuple):
        distance = np.sqrt((new_node[0]-node_from[0])**2 + (new_node[1]-node_from[1])**2)
        return distance > self._radius*2

    def reset_priority_queue(self, new_goal):
        pass
        # TODO implement method (aggiungi tutti i nodi del grafo alla priority queue secondo la nuova priorità (distanza in linea d’aria rispetto all’obiettivo).

    def get_next_node(self):
        return self._queue.pop(-1)


    def get_priority_queue(self):
        return self._queue

    def path_to_next_node(self, arrive_node: tuple):
        visited = {self._current_node}
        queue = [self._current_node]
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
                        path.insert(0, node_u) # forse va tolto
                        return path
        return []
