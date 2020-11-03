from .world import WorldConfig


class ScoreConfig:
    init_score = 0
    init_lives = 3

    size = 24
    color = 'white'

    height = WorldConfig.height // size
    offset = WorldConfig.width // (size * 2)

    score_coord = (offset, WorldConfig.height - height)
    lives_coord = (WorldConfig.width - (offset * 5), WorldConfig.height - height)
