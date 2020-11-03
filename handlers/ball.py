class BallHandler(object):
    balls = list()

    def register(self, ball):
        self.balls.append(ball)

    def clear(self):
        self.balls = list()

    def move(self):
        for ball in self.balls:
            ball.move()

    def draw(self, surface):
        for ball in self.balls:
            ball.draw(surface=surface)

    def world_collision(self) -> bool:
        for ball in self.balls:
            if ball.collision_world():
                return True
        return False

    def paddle_collision(self, paddle):
        for ball in self.balls:
            if ball.instance.colliderect(paddle.instance):
                ball.collision(rect=paddle.instance)

    def blocks_collision(self, blocks) -> bool:
        for ball in self.balls:
            index = ball.instance.collidelist([block.instance for block in blocks])
            if index != -1:
                block = blocks[index]
                ball.collision(rect=block.instance)

                block_level = block.hit()
                if not block_level:
                    blocks.pop(index)
                return True
        return False
