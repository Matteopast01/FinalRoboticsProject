import json

from isrlab_project.ReadConfig import ReadConfig
import numpy as np
from isrlab_project.controller.MapGraph import MapGraph


class Knowledge:
    _map_graph: MapGraph
    _current_node: tuple
    _neighbors: dict
    _arrived: bool
    _goal: tuple
    _text_goal: str
    _arrived_data_json: str
    _end_game: bool
    _orientation: float

    def __new__(cls, goal):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Knowledge, cls).__new__(cls)
            cls.instance._map_graph = MapGraph((0, 0))
            cls._neighbors = {}
            cls.instance._goal = goal
            cls.instance._text_goal = ""
            cls.instance._arrived = False
        return cls.instance

    def get_arrived_data(self):
        return json.loads(self._arrived_data_json)

    def get_graph(self):
        return self._map_graph

    def get_end_game(self):
        return self._end_game

    def get_current_node(self):
        return self._current_node

    def get_goal(self):
        return self._goal

    def get_orientation(self):
        return self._orientation

    def set_orientation(self, orientation):
        self._orientation = orientation

    def set_current_node(self, new_current_node):
        self._current_node = new_current_node

    def set_arrived(self, arrived):
        self._arrived = arrived

    def set_goal(self, new_goal):
        self._goal = new_goal

    def set_end_game(self, end_game):
        self._end_game = end_game

    def set_arrived_data_json(self, json_str):
        self._arrived_data_json = json_str

    def reset_neighbors(self):
        self._neighbors = {}

    def add_neighbors(self, side, neighbor):
        self._neighbors[side] = neighbor
