import pygame

from defaults import ScoreConfig


class Score(object):
    def __init__(self):
        self.score = ScoreConfig.init_score
        self.lives = ScoreConfig.init_lives

        self.color = pygame.Color(ScoreConfig.color)

        pygame.font.init()
        self.font = pygame.font.Font(None, ScoreConfig.size)

    def increase_score(self):
        self.score += 1

    def decrease_lives(self):
        self.lives -= 1

    @property
    def score_message(self):
        text = f'Score: {self.score}'
        return self.font.render(text, True, self.color)

    @property
    def lives_message(self):
        text = f'Lives: {self.lives}'
        return self.font.render(text, True, self.color)

    def draw(self, surface):
        surface.blit(self.score_message, ScoreConfig.score_coord)
        surface.blit(self.lives_message, ScoreConfig.lives_coord)
