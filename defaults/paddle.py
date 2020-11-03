from .world import WorldConfig


class PaddleConfig:
    width = WorldConfig.width // 7
    height = WorldConfig.height // 60
    speed = 15
    color = 'orange'
    max_left = 0
    max_right = WorldConfig.width
