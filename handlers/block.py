class BlockHandler(object):
    blocks = []

    def register(self, block):
        self.blocks.append(block)

    def clear(self):
        self.blocks = []

    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface=surface)
