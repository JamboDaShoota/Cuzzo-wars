# Imports
import pygame
from pygame import Surface
from classes.base import Base
from config import *
from classes.cameraController import CameraController

# Game Class
class Game:
    # Init Method
    def __init__(self, window : Surface):
        self.baseLeft = Base(LEFT_BASE_X, TOP_LANE_HEIGHT // 2, "purple", "left")
        self.baseRight = Base(RIGHT_BASE_X, TOP_LANE_HEIGHT // 2, "pink", "right")
        self.baseRight.rect.x -= self.baseRight.rect.width # This is just to align the base properly
        self.window = window

    # Methods
    def moveAllBots(self) -> None:
        self.baseLeft.moveAllBots()
        self.baseRight.moveAllBots()
    
    def drawBases(self) -> None:
        for base in [self.baseLeft, self.baseRight]:
            base.draw(self.window)

    def drawBots(self) -> None:
        for bot in self.baseLeft.deployedTroops + self.baseRight.deployedTroops:
            bot.draw(self.window)

    def deployDeployableTroops(self) -> None:
        self.baseRight.deployTroops()
        self.baseLeft.deployTroops()

    # Test Methods
    def test__deployTroopsLeft(self, count : int) -> None:
        print(" deployTroopsLeft Called ")
        self.baseLeft.addToStorage("debug", count)
        self.baseLeft.toggleDeploying()

    def test__deployTroopsRight(self, count : int) -> None:
        self.baseRight.addToStorage("debug", count)
        self.baseRight.toggleDeploying()

    def test__deployTroops(self, count : int) -> None:
        self.test__deployTroopsLeft(5)
        self.test__deployTroopsRight(5)