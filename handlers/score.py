from world.score import Score


class ScoreHandler(object):
    score = Score()

    def draw(self, surface):
        self.score.draw(surface=surface)
