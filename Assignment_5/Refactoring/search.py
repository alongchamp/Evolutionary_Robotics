import pyrosim
import random
import matplotlib.pyplot as plt
from robot import ROBOT

sim = pyrosim.Simulator(play_paused=True)
robot = ROBOT(sim, random.random()*2 - 1)
sim.start()
sim.wait_to_finish()

for i in range(0,2):
	sim = pyrosim.Simulator()
	robot = ROBOT(sim, random.random()*2 - 1)
	sim.start()
	sim.wait_to_finish()

# sensorData = sim.get_sensor_data(sensor_id=P2)
# print(sensorData)
# f = plt.figure()
# panel = f.add_subplot(111)
# panel.set_ylim(-5, +2)
# plt.plot(sensorData)
# plt.show()
