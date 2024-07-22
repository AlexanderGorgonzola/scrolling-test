import pygame
from pygame.sprite import Sprite

class Player:
    def __init__(self, scroll):
        super().__init__()
        self.screen = scroll.screen
        self.settings = scroll.settings
        self.screen_rect = scroll.screen.get_rect()

        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.speed
        if self.moving_left:
            self.x -= self.settings.speed
        if self.moving_up:
            self.y -= self.settings.speed
        if self.moving_down:
            self.y += self.settings.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Thing(Sprite):
    def __init__(self, scroll):
        super().__init__()
        self.screen = scroll.screen
        self.settings = scroll.settings
        self.screen_rect = scroll.screen.get_rect()

        self.image = pygame.image.load('images/thing.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right:
            self.x -= self.settings.player_speed
        if self.moving_left:
            self.x += self.settings.player_speed
        if self.moving_up:
            self.y += self.settings.player_speed
        if self.moving_down:
            self.y -= self.settings.player_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)