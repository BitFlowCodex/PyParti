import pygame as pg


class Particle:

    def __init__(
        self,
        position_range: (
            tuple[float, float]
            | tuple[tuple[float, float], float]
            | tuple[float, tuple[float, float]]
            | tuple[tuple[float, float], tuple[float, float]]
        ),
        velocity_range: (
            tuple[float, float]
            | tuple[tuple[float, float], float]
            | tuple[float, tuple[float, float]]
            | tuple[tuple[float, float], tuple[float, float]]
        ),
        size: tuple[float, float] | tuple[float],
        shape: str = "rect",
        life_time: float = 3.0,
        color: str | tuple = "white",
        gravity: float = 0.0,
    ):
        self.position_range = self._normalize_range(position_range)
        self.velocity_range = self._normalize_range(velocity_range)
        self.size = self._normalize_size(size)

        self.color = color
        self.life_time = life_time
        self.gravity = gravity
        self.shape = shape
        self.age = 0.0

    @staticmethod
    def _normalize_range(value):
        def normalize(v):
            if isinstance(v, float | int):
                return (v, v)
            return v

        return normalize(value[0]), normalize(value[1])

    @staticmethod
    def _normalize_size(size: float | tuple[float, float]):
        if isinstance(size, (int, float)):
            return (size, size)
        return size

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
        return self.age < self.life_time
