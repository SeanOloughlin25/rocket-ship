from pathlib import Path
import json

class GameStats:
    """A class to manage game ststistics and persistent high score"""
    def __init__(self, ai_game):
        """Initialize game statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # open all time high score
        self.load_all_time_high_score()

    def reset_stats(self):
        """Reset stats for a new game"""
        self.lives = self.settings.lives
        self.score = 0 # current score 0

    def load_all_time_high_score(self):
        """Load All Time High Score If It Exist"""
        path = Path("high_score.json")
        if path.exists():
            try:
                contents = path.read_text()
                self.high_score = json.loads(contents)
            except json.JSONDecodeError:
                self.high_score = 0
                self.all_time_high_score()
        else:
            self.high_score = 0
            """Create File if none exist"""
            self.all_time_high_score()

        
    def all_time_high_score(self):
        """Save High Score"""
        path = Path("high_score.json")
        contents = json.dumps(self.high_score)
        path.write_text(contents)
