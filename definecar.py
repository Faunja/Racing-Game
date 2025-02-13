# definecar.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import random
from variables import *

class Car:
	def __init__(self, color, speed_limit, lane_width):
		self.color = color
		self.type = random.randint(1, 3)
		new_lane_width = lane_width * (3/8)
		if self.type == 1:
			self.volume = [new_lane_width, new_lane_width]
		elif self.type == 2:
			self.volume = [new_lane_width, new_lane_width * 2]
		else:
			self.volume = [new_lane_width, new_lane_width * 4]
		self.position = [0, 0]
		self.speed = speed_limit + random.randint(-15, 5)
	
	def detect_collision(self, position, other_car):
		if abs(position[0] - other_car.position[0]) < self.volume[0] + other_car.volume[0]:
			if abs(position[1] - other_car.position[1]) < self.volume[1] + other_car.volume[1]:
				return True
		return False
	
	def assign_position(self, cars, center_lanes):
		if len(cars) != 1:
			unset_position = True
			while unset_position:
				self.position[0] = center_lanes[random.randint(0, len(center_lanes) - 1)]
				self.position[1] = SCREEN_HEIGHT / random.randint(1, round(SCREEN_HEIGHT / self.volume[1]))
				for other_car in cars:
					if other_car.color != self.color:
						collision = False
						for space in range(round(SCREEN_HEIGHT / self.volume[1])):
							if self.detect_collision([self.position[0], self.position[1] + self.speed * space], other_car) == True:
								collision = True
								break
						if collision == False:
							unset_position = False
		else:
			self.position[0] = center_lanes[random.randint(0, len(center_lanes) - 1)]
			self.position[1] = SCREEN_HEIGHT - SCREEN_HEIGHT / random.randint(1, round(SCREEN_HEIGHT / self.volume[1]))

	def drive(self, cars):
		self.position[1] -= self.speed
		for other_car in cars:
			if self.color != other_car.color:
				if self.position[0] == other_car.position[0] and self.position[1] < other_car.position[1]:
					for space in range(round(SCREEN_HEIGHT / self.volume[1])):
						if self.detect_collision([self.position[0], self.position[1] + self.speed * space], other_car) == True:
							self.speed = other_car.speed

	def adjust_position(self, player):
		self.position[1] += player.speed
