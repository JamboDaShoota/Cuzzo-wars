# Imports
import pygame
from pygame import Surface
from classes.camera import Camera
from config import *
from util.functions import map_value
from util.functions import clamp

# Camera Controller Class
class CameraManager:
    # Class Variables
    def __init__(self):
        self.camera = Camera()
        self.navBox = pygame.Rect((WIDTH - NAVBOX_WIDTH) // 2, TOP_LANE_HEIGHT - NAVBOX_HEIGHT - 15, NAVBOX_WIDTH, NAVBOX_HEIGHT)
        self.outlineBox = pygame.Rect(self.navBox.x + (self.navBox.width // 2) - ((NAVBOX_WIDTH // 6) // 2), self.navBox.y + (self.navBox.height // 2) - ((NAVBOX_HEIGHT / 2) // 2), NAVBOX_WIDTH // 6, NAVBOX_HEIGHT / 2)
        self.trackMouse = False

    def draw(self, targetSurface : Surface):
        surf = pygame.Surface((self.navBox.width, self.navBox.height), pygame.SRCALPHA)
        surf.fill((0,0,0,120))
        targetSurface.blit(surf, (self.navBox.x, self.navBox.y))
        pygame.draw.rect(targetSurface, "white", self.outlineBox)

    def handleNavInput(self):
        if self.trackMouse:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.outlineBox.x = clamp(mouse_x - self.outlineBox.width // 2 , self.navBox.x, self.navBox.x + self.navBox.width - self.outlineBox.width)
            self.outlineBox.y = clamp(mouse_y - self.outlineBox.height // 2, self.navBox.y, self.navBox.y + self.navBox.height - self.outlineBox.height)

            self.camera.rect.x = map_value(
                self.outlineBox.centerx,
                self.navBox.x,
                self.navBox.x + self.navBox.width,
                0,
                self.camera.batteFieldWidth - self.camera.rect.width
            )
            self.camera.rect.y = map_value(
                self.outlineBox.centery,
                self.navBox.y,
                self.navBox.y + self.navBox.height,
                0,
                self.camera.battleFieldHeight - self.camera.rect.height
            )

