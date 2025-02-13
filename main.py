# main.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 Racing-Game/main.py
import pygame
from variables import *
from defineroad import *
from drawscreen import update_screen

def main():
	run = True
	Street.create_car()
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
			if event.type == pygame.QUIT:
				run = False
		update_screen()
	pygame.quit()
main()
