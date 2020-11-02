class GameObject(object):
    @classmethod
    def create(cls, world, *args, **kwargs):
        raise NotImplementedError


class VisibleObject(GameObject):
    @classmethod
    def create(cls, world, *args, **kwargs):
        raise NotImplementedError

    def draw(self, surface) -> None:
        raise NotImplementedError


class MovableObject(GameObject):
    @classmethod
    def create(cls, world, *args, **kwargs):
        raise NotImplementedError

    def move(self) -> None:
        raise NotImplementedError
