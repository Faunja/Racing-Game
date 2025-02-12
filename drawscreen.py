# drawscreen.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from defineroad import *

def draw_screen():
	screen.fill(White)
	offset = (SCREEN_WIDTH - Street.width) / 2
	check = offset

	pygame.draw.rect(screen, (255, 0, 0), (check, 0, Street.lane_border, SCREEN_HEIGHT))
	pygame.draw.rect(screen, (255, 0, 0), (SCREEN_WIDTH / 2 - Street.lane_border / 2, 0, Street.lane_border, SCREEN_HEIGHT))
	pygame.draw.rect(screen, (255, 0, 0), (SCREEN_WIDTH - check, 0, Street.lane_border, SCREEN_HEIGHT))
	
def update_screen():
	draw_screen()
	pygame.display.set_caption(f'{clock.get_fps() :.1f}')
	pygame.display.update()