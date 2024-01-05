from src.body import SimulatedPioneerBody
import numpy as np

robot = SimulatedPioneerBody("prova")


robot.start()
robot.do_action("leftMotor",0)
robot.do_action("rightMotor",0)
#print (robot.read_orientation())
#we are printing the z euler angle in degree
print(np.degrees(robot.read_orientation())[2])

#robot.read_camera()

robot.do_action("leftMotor",0.1)
robot.do_action("rightMotor",0.1)
robot.stop()
"""
print(r_c_1)
print(r_c)
array = np.array(r_c_1)
# Use PIL to create an image from the new array of pixelsnew_image = Image.fromarray(array)
new_image = Image.fromarray(array)
new_image.show()
"""




