import pyrosim
import random
import math
import copy
import pickle
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL	
from population import POPULATION

parents = POPULATION(5)
parents.Evaluate()
parents.Print()

for g in range(1,100):
	children = copy.deepcopy(parents)
	children.Mutate()
	children.Evaluate()
	parents.ReplaceWith(children)
	print(g, end=' ')
	parents.Print()


