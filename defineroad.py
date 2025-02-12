# defineroad.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
from variables import *
from definecar import *

class Road:
	def __init__(self):
		self.width = SCREEN_WIDTH / 2
		self.lanes = 4
		self.lane_border = SCREEN_WIDTH / (self.width / self.lanes)
		self.lane_width = self.width / self.lanes - self.lane_border
		self.cars = []
	
	def create_car(self):
		newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
		for information in range(len(self.cars)):
			if self.cars[information].color == newcolor:
				newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
				information = 0
		self.cars.append(Car(newcolor))

Street = Road()