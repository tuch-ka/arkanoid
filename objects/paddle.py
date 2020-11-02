import pygame


class Paddle(object):
    instance = None

    def __init__(self, width: int = 250, height: int = 15, **kwargs):
        self.width = width
        self.height = height

        self.speed = kwargs.get('speed') or 15

        color_name = kwargs.get('color') or 'darkorange'
        self.color = pygame.Color(color_name)

        self.max_left = kwargs.get('max_left') or 0
        self.max_right = kwargs.get('max_right') or float('inf')

    @classmethod
    def create(cls, world, **kwargs):
        paddle = cls(
            **kwargs,
            max_right=world.width,
            height=world.height // 60,
            width=world.width // 7,
        )

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
        if self.instance.left > self.max_left:
            self.instance.left -= self.speed

    def move_right(self):
        if self.instance.right < self.max_right:
            self.instance.right += self.speed