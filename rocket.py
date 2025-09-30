import pygame


class Rocket:
    """A Class to Manage our Rocket"""
    def __init__(self, ai_game):
        """Initialize the Ship and Set Starting Position"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load image of rocket and get its rect
        self.image = pygame.image.load("images/rocket.bmp")
        # resize the image
        self.image = pygame.transform.scale(self.image, (70, 120))
        # Save the original image for rotations
        self.original_image = self.image  
        self.rect = self.image.get_rect()

        # set ship in the center of the screen
        self.rect.center = self.screen_rect.center

        # Store a float for new ships exact horizontal positon
        self.x = float(self.rect.x)
        # Store a float for new ships exact virtical position
        self.y = float(self.rect.y)

        # Movement Flag: Start with a Rocket thats not moving 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # set starting angle of image
        self.angle = 0

    def update(self):
        """Update Rockets Position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
            self.angle = 270
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
            self.angle = 90
        if self.moving_up and self.rect.top > 0: 
            self.y -= self.settings.rocket_speed
            self.angle = 0
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
            self.angle = 180

        # Make sure angle stays within 0-360 for consistent rotation
        self.angle %= 360

        
        # Update rect of object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Start the ship at its current location"""
        # Rotate the Image
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        self.screen.blit(rotated_image, rotated_rect.topleft)