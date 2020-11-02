from random import randrange

import pygame

from models.abc.abc_objects import VisibleObject, MovableObject


class Ball(VisibleObject, MovableObject):
    def __init__(self, radius: int = 10, speed: int = 6, **kwargs):
        self.radius = radius
        self.speed = speed
        
        color_name = kwargs.get('color') or 'white'
        self.color = pygame.Color(color_name)

        self.instance = None

        self.dx, self.dy = 1, -1
        self.rect = int(self.radius * 2 ** 0.5)

    def move(self):
        self.instance.x += self.speed * self.dx
        self.instance.y += self.speed * self.dy

    def collision_world(self, world):
        if self.instance.centerx < self.radius or self.instance.centerx > world.width - self.radius:
            self.dx = -self.dx
        if self.instance.centery < self.radius:
            self.dy = -self.dy
        if self.instance.bottom > world.height:
            exit()

    def collision(self, rect):
        if self.dx > 0:
            delta_x = self.instance.right - rect.instance.left
        else:
            delta_x = rect.instance.right - self.instance.left
        if self.dy > 0:
            delta_y = self.instance.bottom - rect.instance.top
        else:
            delta_y = rect.instance.bottom - self.instance.top

        if abs(delta_x - delta_y) < self.radius // 5:
            self.dx, self.dy = -self.dx, -self.dy
        elif delta_x > delta_y:
            self.dy = -self.dy
        elif delta_y > delta_x:
            self.dx = -self.dx

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.instance.center, self.radius)

    @classmethod
    def create(cls, world, *args, **kwargs):
        ball = cls(*args, **kwargs)
        ball.instance = pygame.Rect(
                randrange(ball.rect, world.width - ball.rect),
                world.height // 2,
                ball.rect,
                ball.rect
            )
        return ball
