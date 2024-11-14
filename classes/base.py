# Imports
import pygame
from pygame import Surface
from config import *
from classes.bot import Bot
import random


class Base:
    # Class Variables
    __WIDTH,__HEIGHT = 40, 40
    __BASE_SPAWN_Y_RANGE = 200

    # Init Function
    def __init__(self, x, y, color : str, name : str):
        self.rect = pygame.Rect(x, y, self.__WIDTH, self.__HEIGHT)
        self.color = color
        self.armyStorage : list[Bot] = []
        self.deployedTroops : list[Bot] = []
        self.deploying : bool = False
        self.deploy_delay = 500  # Delay in milliseconds (e.g., 500 ms = 0.5 seconds)
        self.last_deploy_time = 0  # Time of the last deployment
        self.name = name
        
    # Draw Function
    def draw(self, targetSurface : Surface):
        pygame.draw.rect(targetSurface, self.color, self.rect)

    # Add To Storage Function
    def addToStorage(self, BotType : str, count : int):
        for x in range(count):
            if BotType == "debug":
                if self.name == "left":
                    self.armyStorage.append(Bot(self.rect.x + self.rect.width + 10, random.randrange(self.rect.y - self.__BASE_SPAWN_Y_RANGE, self.rect.y + self.__BASE_SPAWN_Y_RANGE), self))
                else:
                    self.armyStorage.append(Bot(self.rect.x - self.rect.width - 10, random.randrange(self.rect.y - self.__BASE_SPAWN_Y_RANGE, self.rect.y + self.__BASE_SPAWN_Y_RANGE), self))


        print (f" Added {count} troops to storage : {[n.__class__.__name__ for n in self.armyStorage]}")

    def moveAllBots(self) -> None:
        for bot in self.deployedTroops:
            bot.move()

    def toggleDeploying(self) -> None:
        self.deploying = not self.deploying

    def deployTroops(self) -> None:
        if self.deploying:
            current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
            if self.armyStorage and current_time - self.last_deploy_time >= self.deploy_delay:
                self.deployedTroops.append(self.armyStorage.pop(0))  # Add it to deployed troops
                self.last_deploy_time = current_time  # Update the last deploy time
            if not self.armyStorage:  # Stop deploying if there are no more troops
                self.toggleDeploying()
                print (f" Deployed Bots from storage : {[n.__class__.__name__ for n in self.armyStorage]} - {[n.__class__.__name__ for n in self.deployedTroops]}")