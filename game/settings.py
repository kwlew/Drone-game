import json
import os
import pygame

DATA_DIR = 'data'
SETTINGS_FILE = os.path.join(DATA_DIR, 'settings.json')


class Settings:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.fullscreen = False
        self.surface = None

    def load(self):
        if not os.path.exists(SETTINGS_FILE):
            return

        with open(SETTINGS_FILE, 'r') as f:
            data = json.load(f)

        self.width = data.get('width', self.width)
        self.height = data.get('height', self.height)
        self.fullscreen = data.get('fullscreen', self.fullscreen)

    def save(self):
        # 🔹 Ensure data folder exists
        os.makedirs(DATA_DIR, exist_ok=True)

        with open(SETTINGS_FILE, 'w') as f:
            json.dump(
                {
                    'width': self.width,
                    'height': self.height,
                    'fullscreen': self.fullscreen
                },
                f,
                indent=4
            )

    def apply_display(self):
        flags = pygame.FULLSCREEN if self.fullscreen else 0
        self.surface = pygame.display.set_mode(
            (self.width, self.height),
            flags
        )
        pygame.display.flip()


settings = Settings()
