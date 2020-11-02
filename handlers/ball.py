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
            if ball.instance.colliderect(paddle.instance) and ball.dy > 0:
                self.collision(ball=ball, rect=paddle)

    def blocks_collision(self, blocks):
        for ball in self.balls:
            index = ball.instance.collidelist([block.instance for block in blocks])
            if index != -1:
                block = blocks.pop(index)
                self.collision(ball=ball, rect=block)

    @staticmethod
    def collision(ball, rect):
        if ball.dx > 0:
            delta_x = ball.instance.right - rect.instance.left
        else:
            delta_x = rect.instance.right - ball.instance.left
        if ball.dy > 0:
            delta_y = ball.instance.bottom - rect.instance.top
        else:
            delta_y = rect.instance.bottom - ball.instance.top

        if abs(delta_x - delta_y) < 10:
            ball.dx, ball.dy = -ball.dx, -ball.dy
        elif delta_x > delta_y:
            ball.dy = -ball.dy
        elif delta_y > delta_x:
            ball.dx = -ball.dx
