import numpy as np
import json
class wwwof():
	def __init__(self):
		pass
	def matrix(self,min_,max_,size):
		self.min_ = min_
		self.max_ = max_
		self.size = size
		self.matrix = np.random.RandomState(100).uniform(self.min_,self.max_,self.size)
		self.matrix2 = np.random.RandomState(100).uniform(self.min_,self.max_,self.size)
		return self.matrix * self.matrix2
#class jsonfish():






