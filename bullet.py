import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from rockets"""
    def __init__(self, ai_game, x_direction, y_direction):
        """Create a bullet objet at the ships position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.center = ai_game.rocket.rect.center

        # Store bullet position as floats for later updates        
        self.y = float(self.rect.y)        
        self.x = float(self.rect.x)

        # Initialize direction values        
        self.x_direction = x_direction       
        self.y_direction = y_direction       
  

    def update(self):        
        """Update the bullet's position based on direction"""        
        self.x += self.x_direction  # Move in the x-direction        
        self.y -= self.y_direction  # Move in the y-direction        
        self.rect.x = self.x  # Update the rect's x position        
        self.rect.y = self.y  # Update the rect's y position

        
        
    def draw_bullet(self):
        """Draw Bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


        

