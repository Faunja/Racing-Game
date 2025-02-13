# main.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 Racing-Game/main.py
import pygame, random
from variables import *
from defineroad import *
from defineplayer import *
from drawscreen import update_screen

def main():
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
			if event.type == pygame.QUIT:
				run = False
		if random.randint(1, FPS) == 1:
			Street.create_car()
		Street.update_cars()
		update_screen()
	pygame.quit()
main()
