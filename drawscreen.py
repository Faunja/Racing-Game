# drawscreen.py
# By Kayden Campbell
# Copyright 2025
# Licensed under the terms of the GPL 3
import pygame
from variables import *
from defineroad import *

def draw_screen():
    screen.fill(Black)

def update_screen():
    draw_screen()
    pygame.display.set_caption(f'{clock.get_fps() :.1f}')
    pygame.display.update()