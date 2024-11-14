# Imports
import pygame
from config import *

# Camera Class
class Camera:
    
    # Init Function
    def __init__(self):
        self.rect = pygame.Rect(0, 0, WIDTH, TOP_LANE_HEIGHT) # This width and height is for the viewport maximum potential
        self.batteFieldWidth = VIEWPORT_MAX_WIDTH
        self.battleFieldHeight = VIEWPORT_MAX_HEIGHT
