import pygame

from defaults import PaddleConfig, WorldConfig, ScoreConfig


class Paddle(object):
    instance = None

    def __init__(self) -> None:
        self.width = PaddleConfig.width
        self.height = PaddleConfig.height

        self.speed = PaddleConfig.speed

        self.color = pygame.Color(PaddleConfig.color)

        self.max_left = PaddleConfig.max_left
        self.max_right = PaddleConfig.max_right

    @classmethod
    def create(cls) -> 'Paddle':
        paddle = cls()

        paddle.instance = pygame.Rect(
            WorldConfig.width // 2 - paddle.width // 2,
            WorldConfig.height - paddle.height - (ScoreConfig.height + 10),
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
