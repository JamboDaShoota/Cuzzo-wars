# Imports
import pygame
from pygame import Surface
from config import BOT_TEST_CONFIG as BTC

# Bot Class
class Bot:
    # Class Variables
    __WIDTH, __HEIGHT = 20,20
    __COLOR = "black"
    # Init Function
    def __init__(self, x : int, y : int, base): # Not going to infer base type since it will cause circular import
        self.rect = pygame.Rect(x, y, self.__WIDTH, self.__HEIGHT)
        self.health = BTC["health"]
        self.damage = BTC["damage"]
        self.speed = BTC["speed"]
        self.base = base

    # Draw Functino
    def draw(self, targetSurface : Surface) -> None:
        pygame.draw.rect(targetSurface, self.__COLOR, self.rect)
    
    def move(self):
        if self.base.name == "left":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        #TODO : Test this
    def takeDamage(self, damage : int) -> None:
        self.health -= damage

    def die(self) -> None:
        raise NotImplementedError("Gotta write this function to kill the player when they die")
    
    def __str__(self):
        return self.__class__.__name__