from settings import *
import pygame, pygame.gfxdraw

animation_group = pygame.sprite.Group()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = OBSTACLE_COLOR
        self.radius = OBSTACLE_RAD
        self.pos_x, self.pos_y = x, y
        self.image = pygame.Surface((BALL_RAD * 2, BALL_RAD * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

class AnimatedObstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, delta_time):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.x, self.y = x, y
        self.coords = (self.x, self.y)
        self.radius = radius
        self.color = color
        self.delta_time = delta_time
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

        # Calculate alpha value to decrement each frame
        self.alpha = 125
        self.fade_speed_second = 250
        self.fade_speed_frame = self.fade_speed_second * self.delta_time
        self.divisor = int(self.fade_speed_second / self.fade_speed_frame)
        self.fade_speed_frame = self.alpha / self.divisor

        # Calculate radius value to decrement each frame
        self.radius_dec_second = 32
        self.radius_dec_frame = self.radius_dec_second * self.delta_time
        self.divisor_rad = int(self.radius_dec_second / self.radius_dec_frame)
        self.radius_dec_frame = self.radius_dec_second / self.divisor_rad

    def fade(self, delta_time):
        self.alpha -= int(self.fade_speed_frame)
        if self.radius > 0:
            self.radius -= self.radius_dec_frame
        if self.alpha < 50 or self.radius < 2:
            self.kill()

    def update(self):
        self.fade(self.delta_time)
        self.draw(self.display_surface)

    def draw(self, surface):
        self.circle_surface = pygame.Surface((self.radius, self.radius), pygame.SRCALPHA)
        pygame.gfxdraw.filled_circle(self.display_surface, self.x, self.y, int(self.radius), (255, 255, 255, self.alpha))
        self.display_surface.blit(self.circle_surface, (0, 0))