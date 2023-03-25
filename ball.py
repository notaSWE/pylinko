from multis import *
from obstacles import *
from settings import *
import pygame, pymunk, random

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, space, board, delta_time):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.space = space
        self.board = board
        self.delta_time = delta_time
        self.body = pymunk.Body(body_type = pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, BALL_RAD)
        self.shape.elasticity = 0.9
        self.shape.density = 10000
        self.shape.mass = 1000
        self.shape.filter = pymunk.ShapeFilter(categories=BALL_CATEGORY, mask=BALL_MASK)
        self.space.add(self.body, self.shape)
        self.image = pygame.Surface((BALL_RAD * 2, BALL_RAD * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.body.position.x, self.body.position.y))

    def update(self):
        pos_x, pos_y = int(self.body.position.x), int(self.body.position.y)
        self.rect.centerx = pos_x
        self.rect.centery = pos_y

        # Check to see if ball hits obstacle
        for obstacle in self.board.obstacle_sprites:
            if pygame.sprite.collide_rect(self, obstacle):
                # Create animation and add to animation_group
                obstacle_centerx, obstacle_centery = obstacle.rect.centerx, obstacle.rect.centery
                obstacle_pos = (obstacle_centerx, obstacle_centery)

                for animating_obstacle in animation_group:
                    if obstacle_pos == animating_obstacle.coords:
                        animating_obstacle.kill()

                # Instantiate obstacle animation: params -> x, y, radius, color, delta_time
                obs_anim = AnimatedObstacle(obstacle_centerx, obstacle_centery, 16, (255, 255, 255), self.delta_time)
                animation_group.add(obs_anim)

        # Check to see if ball hits multi
        for multi in multi_group:
            if pygame.sprite.collide_rect(self, multi):
                multi.hit_sound()
                multipliers[str(multi.multi_amt)] += 1
                print(f"Total plays: {sum([val for val in multipliers.values()])} | {multipliers}")
                multi.animate(multi.color, multi.multi_amt)
                multi.is_animating = True

                # Display previous multi on right side of screen
                prev_rgb = multi.color
                prev_multi = PrevMulti(str(multi.multi_amt), prev_rgb)
                prev_multi_group.add(prev_multi)
                self.kill()
        
        # Draw red ball
        pygame.draw.circle(self.display_surface, (255, 0, 0), (pos_x, pos_y), BALL_RAD)