import pygame


class Paddle(object):
    def __init__(self, width: int = 330, height: int = 35, speed: int = 15, color: str = 'darkorange'):
        self.width = width
        self.height = height
        self.speed = speed

        self.instance = None
        self.color = pygame.Color(color)

    @classmethod
    def create(cls, world, *args, **kwargs):
        paddle = cls(*args, **kwargs)
        paddle.instance = pygame.Rect(
            world.width // 2 - paddle.width // 2,
            world.height - paddle.height - 10,
            paddle.width,
            paddle.height,
        )
        return paddle

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.instance)

    def move_left(self):
        self.instance.left -= self.speed

    def move_right(self):
        self.instance.right += self.speed
