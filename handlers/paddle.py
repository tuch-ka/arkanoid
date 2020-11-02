class PaddleHandler(object):
    paddle = None

    def register(self, paddle):
        self.paddle = paddle

    def draw(self, surface):
        self.paddle.draw(surface=surface)

    def move_left(self):
        self.paddle.move_left()

    def move_right(self):
        self.paddle.move_right()

    @property
    def instance(self):
        return self.paddle.instance
