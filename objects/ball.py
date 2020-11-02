from random import randrange

import pygame


class Ball(object):
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
        if abs(delta_x - delta_y) < self.radius // 5:   # hitting a corner. 5px - rounding accuracy
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
