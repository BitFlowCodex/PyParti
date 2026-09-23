import pygame as pg
from collections.abc import Callable


class Particle:

    def __init__(
        self,
        shape: str,
        x: float = 0,
        y: float = 0,
        velocity: tuple[float, float] = (0, 0),
        lifeTime: float = 3.0,
        color: str | tuple = "white",
        size: tuple[float, float] = (0, 0),
        hasGravity: bool = False,
        delta: int | float = 0,
    ):

        self.x = x
        self.y = y
        self.color = color
        self.lifeTime = lifeTime
        self.size = size
        self.hasGravity = hasGravity
        self.delta = delta
        self.shape = shape

        self.velocity = pg.Vector2(velocity)

        self.age = 0.0

    # Updates movement, lifetime and gravity of the particle
    def update(self):
        self.x += self.velocity.x

        if self.hasGravity:
            self.velocity.y += 0.5  # Gravity acceleration
        self.y += self.velocity.y

        self.age += 0.1

    # Draw the particle onto the screen
    def draw(self, screen):
        width, height = self.size
        match self.shape:
            case "circle":
                pg.draw.circle(screen, self.color, (self.x, self.y), width, height)
            case "rect":
                pg.draw.rect(
                    screen,
                    self.color,
                    pg.Rect(self.x, self.y, width, height),
                    border_radius=2,
                )
            case "ellipse":
                pg.draw.ellipse(
                    screen,
                    self.color,
                    pg.Rect(self.x, self.y, width, height),
                )
            case _:
                raise ValueError(
                    f"Unknown shape: {self.shape!r}, only shapes are ellipse, rect, and circle."
                )

    # Check if particle lifetime is still active
    def is_alive(self):
        return self.age < self.lifeTime
