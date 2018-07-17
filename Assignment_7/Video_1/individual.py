import random 
import pyrosim
import math
import numpy
from robot import ROBOT

class INDIVIDUAL:
	def __init__(self):
		self.genome = numpy.random.random(4) * 2 - 1
		self.fitness = 0

	def Evaluate(self, pb):
		sim = pyrosim.Simulator(play_blind = pb)
		robot = ROBOT(sim, self.genome)
		sim.start()
#		sim.wait_to_finish()
#		x = sim.get_sensor_data(sensor_id=robot.P4, svi = 0)
#		y = sim.get_sensor_data(sensor_id=robot.P4, svi = 1)
#		z = sim.get_sensor_data(sensor_id=robot.P4, svi = 2)
#		self.fitness = y[-1]
	
	def Mutate(self):
		geneToMutate = random.randint(0,3)
		self.genome[geneToMutate] = random.gauss(geneToMutate, math.fabs(geneToMutate))
	
	def Print(self):
		print(self.genome)
