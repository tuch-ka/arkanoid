from random import randrange

import pygame

from defaults import BallConfig, WorldConfig


class Ball(object):
    def __init__(self, **kwargs) -> None:
        self.radius = kwargs.get('radius') or BallConfig.radius
        self.speed = kwargs.get('speed') or BallConfig.speed

        color_name = kwargs.get('color') or BallConfig.color
        self.color = pygame.Color(color_name)

        self.instance = None

        self.dx, self.dy = 1, -1
        self.rect = int(self.radius * 2 ** 0.5)

    def move(self) -> None:
        self.instance.x += self.speed * self.dx
        self.instance.y += self.speed * self.dy

    def collision_world(self) -> None:
        if self.instance.centerx < self.radius or self.instance.centerx > WorldConfig.width - self.radius:
            self.dx = -self.dx
        if self.instance.centery < self.radius:
            self.dy = -self.dy
        if self.instance.bottom > WorldConfig.height:
            exit()

    def collision(self, rect) -> None:
        ball = self.instance

        # detecting direction
        if self.dx > 0:                                 # from left to right
            delta_x = ball.right - rect.left
        else:                                           # from right to left
            delta_x = rect.right - ball.left

        if self.dy > 0:                                 # from bottom to top
            delta_y = ball.bottom - rect.top
        else:                                           # from top to bottom
            delta_y = rect.bottom - ball.top

        # detecting surface
        if abs(delta_x - delta_y) < BallConfig.corner_accuracy:   # hitting a corner
            self.dx, self.dy = -self.dx, -self.dy

        elif delta_x > delta_y:                         # hit from top or bottom
            self.dy = -self.dy

            # handle direction of hit
            if ball.centerx < rect.centerx:             # hit in left section
                self.dx = -(abs(self.dx))

            elif ball.centerx > rect.centerx:           # hit in right section
                self.dx = abs(self.dx)

        elif delta_y > delta_x:                         # hit from side
            self.dx = -self.dx

    def draw(self, surface) -> None:
        pygame.draw.circle(surface, self.color, self.instance.center, self.radius)

    @classmethod
    def create(cls, **kwargs) -> 'Ball':
        ball = cls(**kwargs)
        ball.instance = pygame.Rect(
                randrange(ball.rect, WorldConfig.width - ball.rect),
                WorldConfig.height // 2,
                ball.rect,
                ball.rect
            )
        return ball
