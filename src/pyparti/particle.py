from pygame import Color, Vector2, draw, Rect


class Particle:
    __slots__ = (
        "x",
        "y",
        "vx",
        "vy",
        "age",
        "lifetime",
        "gravity",
        "image",
        "width",
        "height",
        "alive",
    )

    def __init__(self):
        self.alive = False

        self.x = 0.0
        self.y = 0.0

        self.vx = 0.0
        self.vy = 0.0

        self.age = 0.0
        self.lifetime = 0.0
        self.gravity = 0.0

        self.image = None
        self.width = 0
        self.height = 0

    def reset(
        self,
        x,
        y,
        vx,
        vy,
        lifetime,
        gravity,
        image,
    ):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.age = 0.0
        self.lifetime = lifetime
        self.gravity = gravity

        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()

        self.alive = True

    def update(self, delta):
        self.vy += self.gravity * delta

        self.x += self.vx * delta
        self.y += self.vy * delta

        self.age += delta
