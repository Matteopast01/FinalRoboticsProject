import json

from isrlab_project.ReadConfig import ReadConfig
import numpy as np
from isrlab_project.controller.MapGraph import MapGraph
from time import time


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
    _start_action_time: float
    _configuration: ReadConfig
    _delta_pos_neighbors: dict
    _next_node: tuple
    _path: list
    _action: str

    def __new__(cls):
        # TODO initialize attributes in the constructor
        if not hasattr(cls, 'instance'):
            cls.instance = super(Knowledge, cls).__new__(cls)
            cls._neighbors = {}
            cls.instance._text_goal = ""
            cls.instance._arrived = False
            cls.instance._configuration = ReadConfig()
            cls.instance._current_node = (0, 0)
            start_goal = cls.instance._configuration.read_data("START_GOAL")
            cls.instance._goal = start_goal
            cls.instance._map_graph = MapGraph((0, 0), tuple(start_goal))
            cls.instance._delta_pos_neighbors = {}
            cls.instance._path = []
            cls.instance._end_game = False
            cls.instance._orientation = 0
            cls.instance._start_action_time = time()
            cls.instance._action = ""
            cls.instance._next_node = None
        return cls.instance

    def get_next_node(self):
        return self._next_node

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

    def get_start_action_time(self):
        return self._start_action_time

    def get_delta_pos_neighbors(self, side):
        return self._delta_pos_neighbors[side]

    def get_path(self):
        return self._path

    def get_text_goal(self):
        return self._text_goal

    def get_neighbor(self, side):
        return self._neighbors[side]

    def get_action(self):
        return self._action

    def set_next_node(self, new_next_node):
        self._next_node = new_next_node

    def set_path(self, new_path):
        self._path = new_path

    def set_start_action_time(self, start_action_time):
        self._start_action_time = start_action_time

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

    def set_action(self, action):
        self._action = action

    def set_arrived_data_json(self, json_str):
        self._arrived_data_json = json_str

    def set_text_goal(self, new_text_goal):
        self._text_goal = new_text_goal

    def reset_neighbors(self):
        self._neighbors = {}

    def reset_delta_neighbors(self):
        self._delta_pos_neighbors = {}

    def add_neighbors(self, side, neighbor):
        self._neighbors[side] = neighbor

    def add_delta_pos_neighbors(self, side, neighbor):
        self._delta_pos_neighbors[side] = neighbor

    def is_side_free(self, side):
        return side in self._delta_pos_neighbors

    def read_config_var(self, var_name):
        return self._configuration.read_data(var_name)

    def decode_text_qr(self, text):
        return text
        # TODO implement decode text passed has to be decoded
