import random

class Comparator():
	def __init__(self, noiseRate):
		self.noiseRate = noiseRate

	def lessThan(self, a, b):
		return (a < b) == (random.random() > self.noiseRate)

	def greaterThan(self, a, b):
		return self.lessThan(b, a)
		