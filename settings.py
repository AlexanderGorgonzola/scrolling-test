import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_length = 800
        self.bg = pygame.image.load("images/background.jpg")
        
        self.player_speed = 0.4
        self.speed = 0.05