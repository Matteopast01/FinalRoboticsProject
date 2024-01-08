from coppeliasim_zmqremoteapi_client import RemoteAPIClient

from typing import Any, List
import numpy as np
from PIL import Image
import cv2

# MY_SIM_HOST = "localhost"  # in PyCharm


MY_SIM_HOST = "host.docker.internal"  # from the container


class SimulatedPioneerBody:
    _sim: Any
    _sim_vision: Any
    _cSim_client: Any
    _my_sensors_values: dict
    _my_vision_sensor: Any
    _my_pioneer: Any

    def __init__(self, name: str):
        self._my_name = name
        # zmqRemoteApi connection
        print("Connecting to simulator...")
        self._cSim_client = RemoteAPIClient(host=MY_SIM_HOST)
        self._sim = self._cSim_client.getObject('sim')
        self._my_pioneer = self._sim.getObject("./PioneerP3DX")
        self._my_sensors_values = {
            "left": self._sim.getObject("./ultrasonicSensor[0]"),
            "center": self._sim.getObject("./ultrasonicSensor[4]"),
            "right": self._sim.getObject("./ultrasonicSensor[7]")
        }
        self._my_vision_sensor = self._sim.getObject("./Vision_sensor")
        print("SIM objects referenced")

    def read_orientation(self, axis=2, convert_to_degree=True):
        if convert_to_degree:
            return np.degrees(self._sim.getObjectOrientation(self._my_pioneer, self._sim.handle_world)[axis])
        else:
            return self._sim.getObjectOrientation(self._my_pioneer, self._sim.handle_world)[axis]

    """" this method works but we can't retrieve the position because we are cheating
    def read_position(self):

        return self._sim.getObjectPosition(self._my_pioneer, self._sim.handle_world)
        """

    def read_camera(self):
        self._sim.setStepping(True)
        self._sim.step()
        img, [resX, resY] = self._sim.getVisionSensorImg(self._my_vision_sensor)
        img_a = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
        # In CoppeliaSim images are left to right (x-axis), and bottom to top (y-axis)
        # (consistent with the axes of vision sensors, pointing Z outwards, Y up)
        # and color format is RGB triplets, whereas OpenCV uses BGR:
        image = Image.fromarray(img_a)
        image.save("prova.png")
        self._sim.setStepping(False)
        return img
        # return self._sim.unpackUInt8Table(self._sim.getVisionSensorImg(self._my_vision_sensor)[0])

    def read_proximity_sensor(self, sensor_name=None):
        try:
            # i = 0 : front sensors
            # i = 1 : back sensors
            assert sensor_name in self._my_sensors_values.keys() or sensor_name == None
            if sensor_name == None:
                values = {}
                for sensor, handler in self._my_sensors_values.items():
                    values[sensor] = _, dis, _, _, _ = self._sim.readProximitySensor(handler)
                return values
            else:
                handler = self._my_sensors_values[sensor_name]
                _, dis, _, _, _ = self._sim.readProximitySensor(handler)
                return dis
        except Exception as e:
           print("sensor_name must be one of left, center or right")

    def start(self):
        self._sim.startSimulation()

    def stop(self):
        self._sim.stopSimulation()
