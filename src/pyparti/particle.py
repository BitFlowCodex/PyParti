import pygame as pg


class Particle:
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        velocity: tuple[float, float] = (0, 0),
        lifeTime: float = 3.0,
        color: str | tuple = "white",
        size: float = 10.0,
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
        size = max(1, int(self.size))

        surface = pg.Surface((size, size))
        surface.fill(self.color)
        screen.blit(surface, (self.x, self.y))

    # Check if particle lifetime is still active
    def is_alive(self):
        return self.age < self.lifeTime
