# Imports
import pygame
from config import *
from classes.base import Base
from classes.bot import Bot
from classes.game import Game


# Pygame Initialization 
pygame.init()

# Global Variables
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# Draw Function
def draw(game : Game):
    # Window
    WIN.fill((255,255,255))
    # Lanes
    pygame.draw.rect(WIN, "blue", (0,0, WIDTH, TOP_LANE_HEIGHT)) # Top Lane
    pygame.draw.rect(WIN, "green", (0, TOP_LANE_HEIGHT, WIDTH, BOTTOM_LANE_HEIGHT)) # Bottom Lane
    # Navigation
    game.cameraManager.draw(WIN)
    # Bases
    game.drawBases()
    # Bots
    game.drawBots()
    # Update Screen
    pygame.display.update()

# Main Definition
def main():
    # Game Variables
    CLOCK = pygame.time.Clock()
    run = True
    game = Game(WIN)
    # Game Loop
    while run:
        # Frame Rate Regulation
        CLOCK.tick(FPS)
        # Event Check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    game.test__deployTroopsLeft(5)
                elif event.key == pygame.K_g:
                    game.test__deployTroops(5)
                elif event.key == pygame.K_h:
                    game.test__deployTroopsRight(5)
                elif event.key == pygame.K_v:
                    game.cameraManager.trackMouse = not game.cameraManager.trackMouse
                    print(game.cameraManager.trackMouse)
                    pygame.mouse.set_pos((game.cameraManager.outlineBox.x + game.cameraManager.outlineBox.width), game.cameraManager.outlineBox.y + game.cameraManager.outlineBox.height) # just to set the position of the mouse at first

        game.cameraManager.handleNavInput()

        draw(game)
        # Bot Movement
        game.deployDeployableTroops()
        game.moveAllBots()
    # Exit Function
    pygame.quit()

if __name__ == "__main__":
    main()