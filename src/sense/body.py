from coppeliasim_zmqremoteapi_client import RemoteAPIClient


from typing import Any, List
import numpy as np
from PIL import Image
import cv2

#MY_SIM_HOST = "localhost"  # in PyCharm


MY_SIM_HOST = "host.docker.internal"  # from the container


class SimulatedPioneerBody:
    _sim: Any
    _sim_vision: Any
    _cSim_client: Any
    _my_sensors_values: List
    _my_vision_sensor: Any
    _my_blob_camera: Any
    _my_actuators: dict
    _my_pioneer : Any


    def __init__(self, name: str):
        self._my_name = name
        # zmqRemoteApi connection
        print("Connecting to simulator...")
        self._cSim_client = RemoteAPIClient(host=MY_SIM_HOST)
        self._sim = self._cSim_client.getObject('sim')
        self._my_pioneer = self._sim.getObject("./PioneerP3DX")
        self._my_blob_camera = self._sim.getObject("./blobDetectionCamera")
        self._my_sensors_values = [
            self._sim.getObject("./ultrasonicSensor[0]"),
            self._sim.getObject("./ultrasonicSensor[1]"),
            self._sim.getObject("./ultrasonicSensor[2]"),
            self._sim.getObject("./ultrasonicSensor[3]"),
            self._sim.getObject("./ultrasonicSensor[4]"),
            self._sim.getObject("./ultrasonicSensor[5]"),
            self._sim.getObject("./ultrasonicSensor[6]"),
            self._sim.getObject("./ultrasonicSensor[7]"),
            self._sim.getObject("./ultrasonicSensor[8]"),
            self._sim.getObject("./ultrasonicSensor[9]"),
            self._sim.getObject("./ultrasonicSensor[10]"),
            self._sim.getObject("./ultrasonicSensor[11]"),
            self._sim.getObject("./ultrasonicSensor[12]"),
            self._sim.getObject("./ultrasonicSensor[13]"),
            self._sim.getObject("./ultrasonicSensor[14]"),
            self._sim.getObject("./ultrasonicSensor[15]")
        ]
        self._my_vision_sensor = self._sim.getObject("./Vision_sensor")
        print("SIM objects referenced")
        self._my_actuators = {"leftMotor": self._sim.getObject("./leftMotor"),
                              "rightMotor": self._sim.getObject("./rightMotor")}

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
        img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
        # In CoppeliaSim images are left to right (x-axis), and bottom to top (y-axis)
        # (consistent with the axes of vision sensors, pointing Z outwards, Y up)
        # and color format is RGB triplets, whereas OpenCV uses BGR:
        image = Image.fromarray(img)
        image.save("prova.png")
        self._sim.setStepping(False)
        # return self._sim.unpackUInt8Table(self._sim.getVisionSensorImg(self._my_vision_sensor)[0])



    def do_action(self, actuator_name, value):
        """
        :param actuator: simulator name reference
        :param value: scalar value to impose to the simulated actuator (speed, angle)
        :return:
        """

        actuator = self._my_actuators[actuator_name]
        # This is only for velocity values
        self._sim.setJointTargetVelocity(actuator, value)

    def read_sensors(self, i_from: int, i_to: int):
        try:
            # i = 0 : front sensors
            # i = 1 : back sensors
            assert 0 <= i_from <= i_to, "incorrect sensor array"
            assert i_from <= i_to <= len(self._my_sensors_values)
            values = []
            for sens in self._my_sensors_values[i_from:i_to]:
                _, dis, _, _, _ = self._sim.readProximitySensor(sens)
                values.append(dis)
            return values
        except Exception as e:
            print(i_from, i_to)
            print(e)

    def start(self):
        self._sim.startSimulation()

    def stop(self):
        self._sim.stopSimulation()
