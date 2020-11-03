from world.score import Score


class ScoreHandler(object):
    score = Score()

    def draw(self, surface):
        self.score.draw(surface=surface)

    def increase_score(self):
        self.score.increase_score()

    def decrease_lives(self):
        self.score.decrease_lives()

    def any_lives_left(self) -> bool:
        return bool(self.score.lives)
