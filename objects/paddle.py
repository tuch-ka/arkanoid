import pygame

from defaults import PaddleConfig, WorldConfig


class Paddle(object):
    instance = None

    def __init__(self, **kwargs) -> None:
        self.width = kwargs.get('width') or PaddleConfig.width
        self.height = kwargs.get('height') or PaddleConfig.height

        self.speed = kwargs.get('speed') or PaddleConfig.speed

        color_name = kwargs.get('color') or PaddleConfig.color
        self.color = pygame.Color(color_name)

        self.max_left = kwargs.get('max_left') or PaddleConfig.max_left
        self.max_right = kwargs.get('max_right') or PaddleConfig.max_right

    @classmethod
    def create(cls, **kwargs) -> 'Paddle':
        paddle = cls(**kwargs)

        paddle.instance = pygame.Rect(
            WorldConfig.width // 2 - paddle.width // 2,
            WorldConfig.height - paddle.height - 10,
            paddle.width,
            paddle.height,
        )

        return paddle

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.color, self.instance)

    def move_left(self) -> None:
        if self.instance.left > self.max_left:
            self.instance.left -= self.speed

    def move_right(self) -> None:
        if self.instance.right < self.max_right:
            self.instance.right += self.speed
