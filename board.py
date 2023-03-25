from multis import *
from obstacles import *
from settings import *
import pygame, pymunk

class Board():
    def __init__(self, space):
        self.space = space
        self.display_surface = pygame.display.get_surface()

        # Obstacles
        self.curr_row_count = 3
        self.final_row_count = 18
        self.obstacles_list = []
        self.obstacle_sprites = pygame.sprite.Group()
        self.updated_coords = OBSTACLE_START

        while self.curr_row_count <= self.final_row_count:
            for i in range(self.curr_row_count):
                self.obstacles_list.append(self.spawn_obstacle(self.updated_coords, self.space))
                self.updated_coords = (int(self.updated_coords[0] + OBSTACLE_PAD), self.updated_coords[1])
            self.updated_coords = (int(WIDTH - self.updated_coords[0] + (.5 * OBSTACLE_PAD)), int(self.updated_coords[1] + OBSTACLE_PAD))
            self.curr_row_count += 1

    def draw_obstacles(self, obstacles):
        for obstacle in obstacles:
            pos_x, pos_y = int(obstacle.body.position.x), int(obstacle.body.position.y)
            pygame.draw.circle(self.display_surface, (255, 255, 255), (pos_x, pos_y), OBSTACLE_RAD)

    def spawn_obstacle(self, pos, space):
        body = pymunk.Body(body_type = pymunk.Body.STATIC)
        body.position = pos
        body.friction = 0.6
        shape = pymunk.Circle(body, OBSTACLE_RAD)
        shape.elasticity = 0.4
        shape.filter = pymunk.ShapeFilter(categories=OBSTACLE_CATEGORY, mask=OBSTACLE_MASK)
        self.space.add(body, shape)
        # obstacle = Obstacle(body.position.x, body.position.y)
        # self.obstacle_sprites(obstacle)
        return shape

    def update(self):
        self.draw_obstacles(self.obstacles_list)