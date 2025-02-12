# definecar.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import random

class Car:
	def __init__(self, color):
		self.color = color
		self.type = random.randint(1, 3)
		self.position = 0
		self.speed = 0