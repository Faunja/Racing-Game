# defineroad.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
from variables import *
from definecar import *

class Road:
	def __init__(self):
		# Don't do odd numbers
		self.lanes = 4
		self.lane_width = SCREEN_WIDTH / 16
		self.lane_border_width = self.lane_width / 16
		self.lane_border_height = SCREEN_HEIGHT / 8
		self.lane_centers = []
		self.speed_limit = SCREEN_HEIGHT / 16
		if self.lanes % 2 == 0:
			for lane in range(round(-self.lanes / 2), round(self.lanes / 2)):
				distance = lane + .5
				self.lane_centers.append((self.lane_width + self.lane_border_width) * distance + SCREEN_WIDTH / 2)
		self.cars = []
	
	def create_car(self):
		newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
		for information in range(len(self.cars)):
			if self.cars[information].color == newcolor:
				newcolor = (random.randint(60, 255), random.randint(60, 255), random.randint(60, 255))
				information = 0
		self.cars.append(Car(newcolor, self.speed_limit, self.lane_width))
		self.cars[len(self.cars) - 1].assign_position(self.cars, self.lane_centers)
	
	def update_cars(self):
		for car in self.cars:
			car.drive(self.cars)
			car.adjust_position(self.cars[0])

Street = Road()
