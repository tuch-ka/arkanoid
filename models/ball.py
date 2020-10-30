from random import randrange

import pygame


class Ball(object):
    def __init__(self, radius: int = 20, speed: int = 6, color: str = 'white'):
        self.radius = radius
        self.speed = speed
        self.color = pygame.Color(color)

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

    def collision_paddle(self, paddle):
        if self.instance.colliderect(paddle) and self.dy > 0:
            self.dy = -self.dy

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
