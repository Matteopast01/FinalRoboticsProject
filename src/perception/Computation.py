from ..ReadConfig import ReadConfig
import numpy as np


class Computation:

    _orientation: float
    _position: tuple
    _config: ReadConfig
    _angle_side = {"left": -np.pi/2, "right": np.pi/2, "center": 0}

    def __init__(self, start_orientation):
        self._config = ReadConfig()
        self._orientation = start_orientation
        self._position = (0, 0)

    def set_position(self, new_x, new_y):
        self._position = (new_x, new_y)

    def get_position(self):
        return self._position

    def set_orientation(self, orientation):
        self._orientation = orientation

    def compute_position(self, space, orientation):
        x = self._position[0] + space * np.cos(orientation)
        y = self._position[1] + space * np.sin(orientation)
        return x, y

    def is_side_free(self, proximity_val):
        threshold = self._config.read_data("FREE_SIDE_THRESHOLD")
        if proximity_val == 0 or proximity_val < threshold:
            return True

    def compute_position_robot(self):
        space = self._config.read_data("MOTION_WAIT")*self._config.read_data("SPEED")
        self._position = self.compute_position(space, self._orientation)

    def compute_position_node(self, free_side):
        space = self._config.read_data("SPACE")
        return self.compute_position(space, self._angle_side[free_side])









