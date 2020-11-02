class BallHandler(object):
    balls = []

    @classmethod
    def register(cls, ball):
        cls.balls.append(ball)

    @classmethod
    def clear(cls):
        cls.balls = []

    @classmethod
    def move(cls):
        for ball in cls.balls:
            ball.move()

    @classmethod
    def draw(cls, surface):
        for ball in cls.balls:
            ball.draw(surface=surface)

    @classmethod
    def world_collision(cls, world):
        for ball in cls.balls:
            ball.collision_world(world=world)

    @classmethod
    def paddle_collision(cls, paddle):
        for ball in cls.balls:
            ball.collision_paddle(paddle=paddle)
