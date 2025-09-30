# Load the bullet image and set its rect
self.image = pygame.image.load("images/bullet3.bmp")
# Adjust the size of the bullet
self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_width, self.settings.bullet_height))
self.rect = self.image.get_rect()

self.x += self.x_direction # Moves Horizontally based on direction
self.y += self.y_direction # Moves vertically based on direction
self.rect.x = self.x # Update Rect Position
self.rect.y = self.y # Update Rect Position

self.x_direction = 0 # Initialize x direction
self.y_direction = 0 # Initialize y direction
self.x = float(self.rect.x)

def draw_bullet(self):
"""Draw Bullet to screen"""
self.screen.blit(self.image, self.rect) # Draw bullet using the image

def fire_bullet(self):
"""Create a new bullet and add it to the bullet group"""
new_bullet = Bullet(self) # Create new bullet
# Set the positon at the rockets current position
new_bullet.rect.centerx = self.rocket.rect.centerx
new_bullet.rect.top = self.rocket.rect.top - 10
# Determine firing direction    
if self.rocket.moving_left:
new_bullet.x_direction = -self.settings.bullet_speed
elif self.rocket.moving_right:
new_bullet.x_direction = self.settings.bullet_speed    
else:
    new_bullet.x_direction = 0

if self.rocket.moving_up:        
new_bullet.y_direction = -self.settings.bullet_speed    
elif self.rocket.moving_down:        
new_bullet.y_direction = self.settings.bullet_speed
else:
    new_bullet.y_direction = 0   
self.bullets.add(new_bullet)  # Add it to the group of bullets

# Draw Bullets
for bullet in self.bullets.sprites():
        bullet.draw_bullet()

        self.y -= self.settings.bullet_speed  # move up
        self.y += self.settings.bullet_speed # move down
        self.x -= self.settings.bullet_speed # move left
        self.x += self.settings.bullet_speed # move right 


        
        # works for just shooting up
        #store Bullet position as a float for later updates
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        

    def update(self):
        """Update the bullets position based on direction"""
        # Update exact position of bullet moving up and down
        self.y -= self.settings.bullet_speed  
        self.rect.y = self.y


import random
# comet
# settingd
# Comet Settings
        self.comet_speed = 2

# run game
self.comets.update()
self._update_comets()

# Update comets in SR
def _update_comets(self):
         """Randomly generate comet at intervals every few seconds"""
         if random.randint(1, 100) < 2: # Randome chances to create comet
              new_comet = Comet(self)
              self.comets.add(new_comet)
         for comet in self.comets.copy():
              if comet.rect.rect.top > self.screen_rect.bottom:
                   self.comets.remove(comet)
         self._update_screen()

# update screen
# Draw comets with each updated screen
        for comet in self.comets.sprites():
             comet.update()
             comet.draw_comet()

# comet class
import pygame
import random
from pygame.sprite import Sprite

class Comet(Sprite):
    """A class to represent a single comet falling"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load comet image
        self.image = pygame.image.load("images/comet.bmp")
        self.image = pygame.transform.scale(self.image, (50,50)) # Resize 
        self.rect = self.image.get_rect()
        # Set comet to fall from the top of the screen at ranbdome locations
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = 0 # Start at the top of the sceen
        # Store comets position as a float for smoother movement
        self.y = float(self.rect.y)

    def update(self):
        """Move the comet down the screen"""
        self.y += self.settings.comet_speed # move down at the comet speed
        self.rect.y = self.y # Update the rect position

    def draw_comet(self):
        """Draw comet to screen"""
        self.screen.blit(self.image, self.rect)



# Full screen

        # update limits on where comets can drop
        for comet in self.comets:
            if self.settings.full_screen:
                

# Comet class
self.screen_rect = ai_game.screen.get_rect()










 self.screen_rect = ai_game.screen.get_rect()

self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = 0

if self.settings.full_screen == True:
    self.info = pygame.display.Info()     
    self.settings.screen_width = self.info.current_w
    self.settings.screen_height = self.info.current_h  
    self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)      
    self.settings.full_screen = True

    self.screen.fill(self.settings.bg_color)

    
    # Draw bullets with each updated screen
    for bullet in self.bullets.sprites():
        bullet.update()
        bullet.draw_bullet()
    # Draw the comet at the top middle position
    for comet in self.comets.sprites():
        comet.draw_comet()
    # Draw ship to screen with blitme()
    self.rocket.blitme() 