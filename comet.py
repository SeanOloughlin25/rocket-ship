import pygame
import random
from pygame.sprite import Sprite

class Comet(Sprite):
    """A class to represent a single comet falling"""
    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
       
        
        # Load comet image
        try:
            self.image = pygame.image.load("images/comet.bmp")
            self.image = pygame.transform.scale(self.image, (75,75)) # Resize 
        except pygame.error as e:
            print(f"Error loading comet image: {e}")
            self.image = pygame.Surface((75,75)) # Fallback
            self.image.fill((255, 255, 255))  
        
        # set the comet to the top middle of the screen
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.y = float(self.rect.y)

    def update(self):
        """Move Comet down the screen"""
        self.y += self.settings.comet_speed
        self.rect.y = self.y
        # Check if comet has gone off screen
        if self.rect.top > self.settings.screen_height:
            self.kill() # remove comet when off screen

    def draw_comet(self):
        """Draw comet to screen"""
        self.screen.blit(self.image, self.rect)

