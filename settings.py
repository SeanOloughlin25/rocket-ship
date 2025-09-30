
class Settings:
    """A class to store all setting of Space Rocket"""
    def __init__(self):
        """Initialize Game Settings"""
        # Screen Settings  (H&W set dynamically in SpaceRocket)
        self.bg_color = (69, 69, 69)
        # ship limit
        self.lives = 3 # starting lives
        # Rocket Settings
        self.rocket_speed = 5
        # Bullet Settings
        self.bullet_width = 2.0
        self.bullet_height = 5
        self.bullet_speed = 5
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3
        # Comet Settings
        self.comet_speed = 0.5


