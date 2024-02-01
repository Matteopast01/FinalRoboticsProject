from isrlab_project.ReadConfig import ReadConfig
import numpy as np
from queue import PriorityQueue


class MapGraph:
    _graph: dict
    _visited: set
    _queue: PriorityQueue
    _radius: float
    _node_distance_threshold: float
    _position_goal: tuple

    def __init__(self, start_node, position_goal):
        self._radius = ReadConfig().read_data("SPACE") / 2
        self._node_distance_threshold = ReadConfig().read_data("NODE_DISTANCE_THRESHOLD")
        self._graph = {start_node: []}
        self._visited = set()
        self._visited.add(start_node)
        self._position_goal = position_goal
        self._queue = PriorityQueue()
        self._queue.put((self._compute_ptp_distance(start_node), start_node))

    def add_node(self, node_from: tuple, new_node: tuple):
        self._graph[node_from].append(new_node)
        self._graph[new_node] = [node_from]
        self._visited.add(new_node)
        self._queue.put((self._compute_ptp_distance(new_node), new_node))

    def _compute_ptp_distance(self, node, node_from=None):
        if node_from is None:
            node_from = self._position_goal
        return np.sqrt((node_from[0] - node[0]) ** 2 + (node_from[1] - node[1]) ** 2)

    def is_nodes_position_equals(self, node1, node2):
        distance = np.sqrt((node1[0] - node2[0]) ** 2 + (node1[1] - node2[1]) ** 2)
        return distance < self._node_distance_threshold

    def get_approximate_node(self, node):
        min_distance = np.inf
        result_node = None
        for graph_node in self._graph.keys():
            distance = self._compute_ptp_distance(node, graph_node)
            if distance < min_distance:
                min_distance = distance
                result_node = graph_node
        return result_node


    def is_node_new(self, node_from: tuple, new_node: tuple):
        distance = np.sqrt((new_node[0] - node_from[0]) ** 2 + (new_node[1] - node_from[1]) ** 2)
        return distance > self._radius * 2

    def reset_priority_queue(self):
        self._queue = PriorityQueue()
        for key in self._graph.keys():
            for node in self._graph[key]:
                self._queue.put((self._compute_ptp_distance(node), node))

    def get_next_node(self):
        if not self._queue.empty():
            return self._queue.get()[1]
        return None

    def is_priority_queue_empty(self):
        return self._queue.empty()

    def get_priority_queue(self):
        return self._queue

    def path_to_next_node(self, current_node: tuple, arrive_node: tuple):
        visited = {current_node}
        queue = [current_node]
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
                        # path.insert(0, node_u)  # forse va tolto
                        return path
        return []
