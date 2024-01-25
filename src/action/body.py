#!/usr/bin/env python3
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
from typing import Any, List

# MY_SIM_HOST = "localhost"  # in PyCharm


MY_SIM_HOST = "host.docker.internal"  # from the container


class SimulatedPioneerBody:
    _sim: Any
    _cSim_client: Any
    _my_actuators: dict

    def __init__(self, name: str):
        self._my_name = name
        # zmqRemoteApi connection
        print("Connecting to simulator...")
        self._cSim_client = RemoteAPIClient(host=MY_SIM_HOST)
        self._sim = self._cSim_client.getObject('sim')
        self._my_actuators = {"leftMotor": self._sim.getObject("./leftMotor"),
                              "rightMotor": self._sim.getObject("./rightMotor")}
        print("SIM objects referenced")

    def do_action(self, actuator_name, value):
        """
        :param actuator_name:
        :param actuator: simulator name reference
        :param value: scalar value to impose to the simulated actuator (speed, angle)
        :return:
        """

        actuator = self._my_actuators[actuator_name]
        # This is only for velocity values
        self._sim.setJointTargetVelocity(actuator, value)

    def start(self):
        self._sim.startSimulation()

    def stop(self):
        self._sim.stopSimulation()
