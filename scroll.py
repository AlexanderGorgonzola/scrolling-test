import pygame
import sys
from settings import Settings
from things import Player, Thing, Bg
class Scroll:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_length))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_length = self.screen.get_rect().height
        pygame.display.set_caption("Scrolling test")
        self.player = Player(self)
        self.thing = Thing(self)
        self.bg = Bg(self)

    def run_game(self):
        while True:
            self._check_events()
            self.bg.update()
            self.thing.update()
            self.player.update()
            self.update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
    
    def check_keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.thing.moving_right = True
            self.player.moving_right = True
            self.bg.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.thing.moving_left = True
            self.player.moving_left = True
            self.bg.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.thing.moving_down = True
            self.player.moving_down = True
            self.bg.moving_down = True
        elif event.key == pygame.K_UP:
            self.thing.moving_up = True
            self.player.moving_up = True
            self.bg.moving_up = True
    
    def check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.thing.moving_right = False
            self.player.moving_right = False
            self.bg.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.thing.moving_left = False
            self.player.moving_left = False
            self.bg.moving_left = False
        elif event.key == pygame.K_UP:
            self.thing.moving_up = False
            self.player.moving_up = False
            self.bg.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.thing.moving_down = False
            self.player.moving_down = False
            self.bg.moving_down = False
    
    def update_screen(self):
        self.screen.blit(self.settings.bg, (-500,-1500))
        self.bg.blitme()
        self.player.blitme()
        self.thing.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    Scrolling = Scroll()
    Scrolling.run_game()