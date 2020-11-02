class PaddleHandler(object):
    paddle = None

    @classmethod
    def register(cls, paddle):
        cls.paddle = paddle

    @classmethod
    def draw(cls, surface):
        cls.paddle.draw(surface=surface)

    @classmethod
    def move_left(cls):
        cls.paddle.move_left()

    @classmethod
    def move_right(cls):
        cls.paddle.move_right()
