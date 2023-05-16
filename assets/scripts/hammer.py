"""
Hammer.py contains the hammer class
"""
import pygame

class Hammer(pygame.sprite.Sprite):
    "The hammer class is used for playing the whack-a-mole game"
    def __init__(self, player, coords):
        # - First lets set the size of the hammer, it will always be this size:
        self.image = pygame.Surface([240, 420])
        match player:
            case 1:
                self.image.fill([255, 0, 0])
                self.key = 115
            case 2:
                self.image.fill([0, 0, 255])
                self.key = 1073741905

        # - Save the player variable
        self.player = player
        self.recharge = 0
        self.state = "up"

        # - Set the coordinates for the hammers starting position
        self.coord_x = coords[0]
        self.coord_y = coords[1]



    def events(self, event):
        "Hammer slam event"
        if event.type == 768:
            if event.key == self.key and self.state == "up":
                self.image = pygame.Surface([420, 240])
                match self.player:
                    case 1:
                        self.image.fill([255, 0, 0])
                        self.coord_x += 120
                        self.coord_y += 300
                        self.key = 115
                    case 2:
                        self.image.fill([0, 0, 255])
                        self.coord_x -= 320
                        self.coord_y += 300
                        self.key = 1073741905
                self.state = "down"
                self.recharge = 0



    def update(self, game):
        "Move the cube to the right at the speed provided, multiplied by delta time"
        if self.state == "down":
            self.recharge += 100 * game.delta_time
            if self.recharge >= 20:
                self.image = pygame.Surface([240, 420])
                match self.player:
                    case 1:
                        self.image.fill([255, 0, 0])
                        self.coord_x -= 120
                        self.coord_y -= 300
                        self.key = 115
                    case 2:
                        self.image.fill([0, 0, 255])
                        self.coord_x += 320
                        self.coord_y -= 300
                        self.key = 1073741905
                self.state = "up"




    def draw(self, surface):
        "Draw the cube to the surface provided"
        surface.blit(self.image, [self.coord_x, self.coord_y])