class BallHandler(object):
    balls = []

    def register(self, ball):
        self.balls.append(ball)

    def clear(self):
        self.balls = []

    def move(self):
        for ball in self.balls:
            ball.move()

    def draw(self, surface):
        for ball in self.balls:
            ball.draw(surface=surface)

    def world_collision(self, world):
        for ball in self.balls:
            ball.collision_world(world=world)

    def paddle_collision(self, paddle):
        for ball in self.balls:
            ball.collision_paddle(paddle=paddle)
