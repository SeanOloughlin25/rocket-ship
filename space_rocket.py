import sys
import pygame
import random
from settings import Settings
from rocket import Rocket
from bullet import Bullet
from comet import Comet
from game_stats import GameStats

class SpaceRocket:
    """Overall class to manage game assets and behaviors"""
    def __init__(self):
        """Initialize the game and creat game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Call settings to set screen display
        info = pygame.display.Info()
        self.settings.screen_width = info.current_w
        self.settings.screen_height = info.current_h
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),
                                               pygame.FULLSCREEN)
        pygame.display.set_caption("Space Rocket") # Displays on top Window

        # Keep Track of screen dimensions
        self.screen_rect = self.screen.get_rect()

        self.rocket = Rocket(self) # call rocket
        self.bullets = pygame.sprite.Group()
        self.comets = pygame.sprite.Group()
        self.comet_spawn_count = 0 # Track number of comets spawned
        self.max_comets_first_level = 25
        

        # initialize game stats
        self.stats = GameStats(self)

        # Load and scale rocket image for lives display
        try:
             self.lives_icon = pygame.image.load("images/rocket.bmp")
             self.lives_icon = pygame.transform.scale(self.lives_icon, (35, 60))
        except pygame.error as e:
             print(f"Error loading rocket image for lives: {e}")
             self.lives_icon = pygame.Surface((35, 60))
             self.lives_icon.fill((255, 255, 255))

        # Initialize font for score display
        self.font = pygame.font.SysFont("arial", 36)
        self.score_text = self._render_score_text()
        
    def run_game(self):
        """Call Functions You Want Running While Playing Game"""
        while True:
            self._check_events()
            self.rocket.update()
            self.bullets.update()
            self.comets.update()
            self._update_comets()
            self._update_bullets()  
            self._check_bullet_comet_collisions()
            self._check_rocket_comet_collisions()
            self._update_screen()           
            self.clock.tick(60) # Add Frame Rate

    def _check_events(self):
        """Watch for keyword and mouse movements"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to Keydown Presses"""
        if event.key == pygame.K_RIGHT:
                self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
                self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
                self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
                self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
        elif event.key == pygame.K_q:
             sys.exit()
                
    def _check_keyup_events(self,event): 
        """Responds to KeyUp releases"""               
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        x_direction = 0
        y_direction = 0
        # While Rocket is moving
        if self.rocket.moving_up:
            y_direction = self.settings.bullet_speed
        elif self.rocket.moving_down:
            y_direction = -self.settings.bullet_speed
        if self.rocket.moving_left:
            x_direction = -self.settings.bullet_speed
        elif self.rocket.moving_right:
            x_direction = self.settings.bullet_speed
        # While rocket is stationary
        if not (self.rocket.moving_up or self.rocket.moving_down or 
                self.rocket.moving_left or self.rocket.moving_right):
            # By default, you may want to fire based on the last known rocket angle        
            if self.rocket.angle == 0:            
                y_direction = self.settings.bullet_speed  # Fire up        
            elif self.rocket.angle == 180:            
                y_direction = -self.settings.bullet_speed  # Fire down        
            elif self.rocket.angle == 90:            
                x_direction = -self.settings.bullet_speed  # Fire left        
            elif self.rocket.angle == 270:            
                x_direction = self.settings.bullet_speed  # Fire right
        if len(self.bullets) < self.settings.bullets_allowed:    
            new_bullet = Bullet(self, x_direction, y_direction) # Create new bullet
            self.bullets.add(new_bullet)
        
    def _update_bullets(self):
         """Remove Bullets when they leave the screen"""
         # Update Bullets Position
         for bullet in self.bullets.copy(): # Iterate over a copy of the bullet group            
            # Check if the bullet is out of screen bounds            
            if (bullet.rect.bottom < 0 or  # Bullet is above the top                
                bullet.rect.top > self.screen_rect.bottom or  # Bullet is below the bottom                
                bullet.rect.right < 0 or  # Bullet is left of the screen                
                bullet.rect.left > self.screen_rect.right):  # Bullet is right of the screen                
                self.bullets.remove(bullet)  # Remove bullet from the group 

    def _update_comets(self):
         """Randomly generate comets and update their positions"""
         # random chance to create a new comet
         if self.comet_spawn_count < self.max_comets_first_level:
            if random.randint(1,100) < 2:
                new_comet = Comet(self)
                new_comet.rect.x = random.randint(0, self.settings.screen_width - new_comet.rect.width)        
                new_comet.rect.y = 0  # Start from the top of the screen
                self.comets.add(new_comet)
                self.comet_spawn_count += 1


    def _check_bullet_comet_collisions(self):
         """Check for collisions between bullets and comets"""
         #detect collisions, removing both bullet and comet if they collide
         collisions = pygame.sprite.groupcollide(
              self.bullets, self.comets, True, True
         )
         if collisions:
              destroyed_comets = sum(len(comets_list) for comets_list in collisions.values())
              self.stats.score += 10 * destroyed_comets
              if self.stats.score > self.stats.high_score:
                   self.stats.high_score = self.stats.score
                   self.stats.all_time_high_score()
              self.score_text = self._render_score_text()

    def _check_rocket_comet_collisions(self):
         """Check for collisions between rocket and comets"""
         collisions = pygame.sprite.spritecollide(
              self.rocket, self.comets, True
         )
         if collisions:
              self.stats.lives -= 1
              if self.stats.lives <= 0:
                   self.stats.all_time_high_score()
                   self.stats.reset_stats()
                   self.comet_spawn_count = 0
                   self.comets.empty()
                   self.bullets.empty()
                   self.rocket.rect.center = self.screen_rect.center
                   self.score_text = self._render_score_text()
        
    def _render_score_text(self):
         """Render the score and high score as text"""
         score_str = f"Score: {self.stats.score} High Score: {self.stats.high_score}"
         return self.font.render(score_str, True, (255, 255, 255))

    def _update_screen(self):
         """Update images on screen and flip to new screen"""
         self.screen.fill(self.settings.bg_color)
         for bullet in self.bullets.sprites():
              bullet.draw_bullet()
         for comet in self.comets.sprites():
              comet.draw_comet()
         self.rocket.blitme()
         # Draw lives as rocket icons in top-left corner
         for i in range(self.stats.lives):
              self.screen.blit(self.lives_icon, (10 + i * 45, 10)) # spaces icons 45 pixels apart
        # Draw score in top-right corner
         score_rect = self.score_text.get_rect()
         score_rect.topright = (self.settings.screen_width - 10, 10)
         self.screen.blit(self.score_text, score_rect)
         pygame.display.flip()


if __name__ == '__main__':
    # Make game instance and run game.
    ai = SpaceRocket()
    ai.run_game()       