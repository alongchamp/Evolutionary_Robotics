import random 
import pyrosim
import math
import numpy
from robot import ROBOT

class INDIVIDUAL:
	def __init__(self, i):
		self.genome = numpy.random.random(4) * 2 - 1
		self.fitness = 0
		self.ID = i

	def Start_Evaluation(self, pb):
		self.sim = pyrosim.Simulator(play_blind = pb)
		self.robot = ROBOT(self.sim, self.genome)
		self.sim.start()

	def Compute_Fitness(self):
		self.sim.wait_to_finish()
		x = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi = 0)
		y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi = 1)
		z = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi = 2)
		self.fitness = y[-1]
		del self.sim
	
	def Mutate(self):
		geneToMutate = random.randint(0,3)
		self.genome[geneToMutate] = random.gauss(geneToMutate, math.fabs(geneToMutate))
	
	def Print(self):
		print('[',self.ID,self.fitness,']', end=' ')
