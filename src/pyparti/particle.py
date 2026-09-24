import pygame as pg


class Particle:
    def __init__(
        self,
        position: pg.Vector2,
        velocityRange: (
            tuple[float, float] | tuple[tuple[float, float], tuple[float, float]]
        ),
        shape: str = "rect",
        size: tuple[float, float] = (0, 0),
        lifeTime: float = 3.0,
        color: str | tuple = "white",
        gravity: float = 0.0,
    ):
        self.position = position
        self.velocityRange = self._normalize_range(velocityRange)

        self.color = color
        self.lifeTime = lifeTime
        self.size = size
        self.gravity = gravity
        self.shape = shape
        self.age = 0.0

    @staticmethod
    def _normalize_range(value):
        if isinstance(value[0], (int, float)):
            return (
                (-value[0], value[0]),
                (-value[1], value[1]),
            )

        return value

    def update(self, delta):
        self.velocity.y += self.gravity * delta
        self.position += self.velocity * delta
        self.age += delta

    def draw(self, screen):
        width, height = self.size

        match self.shape:
            case "circle":
                pg.draw.circle(
                    screen,
                    self.color,
                    (self.position.x, self.position.y),
                    width,
                    height,
                )

            case "rect":
                pg.draw.rect(
                    screen,
                    self.color,
                    pg.Rect(
                        self.position.x,
                        self.position.y,
                        width,
                        height,
                    ),
                    border_radius=2,
                )

            case "ellipse":
                pg.draw.ellipse(
                    screen,
                    self.color,
                    pg.Rect(
                        self.position.x,
                        self.position.y,
                        width,
                        height,
                    ),
                )

            case _:
                raise ValueError(
                    f"Unknown shape: {self.shape!r}, "
                    "only shapes are ellipse, rect, and circle."
                )

    def is_alive(self):
        return self.age < self.lifeTime
