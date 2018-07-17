import pyrosim
import random
import math
import copy
import pickle
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL	

parent = INDIVIDUAL()	
parent.Evaluate(False)
print(parent.fitness)

for i in range(0,100):
	child = copy.deepcopy(parent)
	child.Mutate()
	child.Evaluate(True)
	print('[g: ' , i + 1 , ' ] [pw: ' , parent.genome , ' ] [p: ' , parent.fitness, ' ] [c: ' , child.fitness , ' ]')
	if(child.fitness > parent.fitness):
		child.Evaluate(False)
		parent = child
		f = open('robot.p','wb')
		pickle.dump(parent, f)
		f.close()

# f = plt.figure()
# panel = f.add_subplot(111)
# panel.set_ylim(-5, +2)
# plt.plot(sensorData)
# plt.show()
