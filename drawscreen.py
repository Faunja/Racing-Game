# drawscreen.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from defineroad import *

Grass = (60, 165, 60)

def draw_screen():
	screen.fill(Grass)
	
	for lane in Street.lane_centers:
		rect = (lane - Street.lane_width / 2, 0, Street.lane_width, SCREEN_HEIGHT)
		pygame.draw.rect(screen, Black, rect)
	yellow = (255, 255, 0)
	
	for lane in range(round(Street.lanes / 2) + 1):
		combined_width = Street.lane_width + Street.lane_border_width
		if lane == 0:
			rect = (SCREEN_WIDTH / 2 - Street.lane_border_width / 2, 0, Street.lane_border_width, SCREEN_HEIGHT)
			pygame.draw.rect(screen, yellow, rect)
		elif lane + round(Street.lanes / 2) == Street.lanes:
			rect = (SCREEN_WIDTH / 2 - Street.lane_border_width / 2 + combined_width * lane, 0, Street.lane_border_width, SCREEN_HEIGHT)
			pygame.draw.rect(screen, yellow, rect)
			rect = (SCREEN_WIDTH / 2 - Street.lane_border_width / 2 - combined_width * lane, 0, Street.lane_border_width, SCREEN_HEIGHT)
			pygame.draw.rect(screen, yellow, rect)
		else:
			rect = (SCREEN_WIDTH / 2 - Street.lane_border_width / 2 + combined_width * lane, 0, Street.lane_border_width, SCREEN_HEIGHT)
			pygame.draw.rect(screen, White, rect)
			rect = (SCREEN_WIDTH / 2 - Street.lane_border_width / 2 - combined_width * lane, 0, Street.lane_border_width, SCREEN_HEIGHT)
			pygame.draw.rect(screen, White, rect)
			
	for car in Street.cars:
		bottom_left = (car.position[0] - car.volume[0], car.position[1] + car.volume[1])
		bottom_right = (car.position[0] + car.volume[0], car.position[1] + car.volume[1])
		top_left = (car.position[0] - car.volume[0], car.position[1] - car.volume[1])
		top_right = (car.position[0] + car.volume[0], car.position[1] - car.volume[1])
		pygame.draw.polygon(screen, car.color, (top_right, bottom_right, bottom_left, top_left))

def update_screen():
	draw_screen()
	pygame.display.set_caption(f'{clock.get_fps() :.1f}')
	pygame.display.update()
