from pygame import Color, Vector2, draw, Rect


class Particle:

    def __init__(
        self,
        position_range: (
            tuple[float, float]
            | tuple[tuple[float, float], float]
            | tuple[float, tuple[float, float]]
            | tuple[tuple[float, float], tuple[float, float]]
        ),
        direction_range: (
            tuple[float, float]
            | tuple[tuple[float, float], float]
            | tuple[float, tuple[float, float]]
            | tuple[tuple[float, float], tuple[float, float]]
        ),
        speed_range: tuple[float, float] | float | int,
        size: tuple[float, float] | float | int,
        shape: str = "rect",
        life_time: float = 3.0,
        color: str | tuple[int, int, int] | list[tuple[int, int, int]] = "white",
        gravity: float = 0.0,
    ):
        self.position_range = self._normalize_range(position_range)
        self.direction_range = self._normalize_range(direction_range)
        self.speed_range = self._normalize_pair(speed_range)
        self.size = self._normalize_pair(size)

        self.color = self._normalize_color(color)

        self.life_time = life_time
        self.gravity = gravity
        self.shape = shape
        self.age = 0.0

        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

    @staticmethod
    def _normalize_pair(value: float | int | tuple[float, float]):
        if isinstance(value, (float, int)):
            return (value, value)

        return value

    @staticmethod
    def _normalize_range(value):
        if callable(value):
            return value

        return (
            Particle._normalize_pair(value[0]),
            Particle._normalize_pair(value[1]),
        )

    @staticmethod
    def _normalize_color(color: str | tuple | list):
        if isinstance(color, Color):
            return [color]

        if isinstance(color, str):
            return [Color(color)]

        if isinstance(color, tuple) and len(color) in (3, 4):
            return [Color(color)]

        return [Color(c) for c in color]

    def update(self, delta):
        self.velocity.y += self.gravity * delta

        self.position += self.velocity * delta

        self.age += delta

    def draw(self, screen):
        width, height = self.size

        match self.shape:
            case "circle":
                draw.circle(
                    screen,
                    self.color,
                    (self.position.x, self.position.y),
                    width,
                )

            case "rect":
                draw.rect(
                    screen,
                    self.color,
                    Rect(
                        self.position.x,
                        self.position.y,
                        width,
                        height,
                    ),
                    border_radius=2,
                )

            case "ellipse":
                draw.ellipse(
                    screen,
                    self.color,
                    Rect(
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
