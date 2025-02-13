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
		pygame.draw.rect(screen, Black, (lane - Street.lane_width / 2, 0, Street.lane_width, SCREEN_HEIGHT))
	
def update_screen():
	draw_screen()
	pygame.display.set_caption(f'{clock.get_fps() :.1f}')
	pygame.display.update()