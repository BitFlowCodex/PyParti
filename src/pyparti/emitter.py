from random import uniform, choice
import math


class Emitter:
    def __init__(
        self,
        system,
        position,
        direction,
        speed,
        size,
        lifetime,
        shape,
        color,
        amount,
        burst_delay,
        spawn_delay,
        spread,
        gravity,
    ):
        self.system = system

        self.position = self._normalize_range(position)
        self.direction = self._normalize_range(direction)

        self.speed = self._normalize_pair(speed)
        self.size = self._normalize_pair(size)

        self.lifetime = lifetime
        self.shape = shape
        self.color = self._normalize_colors(color)

        self.amount = amount

        self.burst_delay = burst_delay
        self.spawn_delay = spawn_delay
        self.spread = spread

        self.gravity = gravity

        self.timer = 0.0

    @staticmethod
    def _normalize_pair(value):
        if isinstance(value, (int, float)):
            return value, value

        return value

    @staticmethod
    def _normalize_range(value):
        return (
            Emitter._normalize_pair(value[0]),
            Emitter._normalize_pair(value[1]),
        )

    @staticmethod
    def _normalize_colors(color):
        if isinstance(color, str):
            return [color]

        if isinstance(color, tuple):
            if len(color) in (3, 4):
                return [color]

        return list(color)

    def _random_position(self):
        x_range, y_range = self.position

        return (
            uniform(*x_range),
            uniform(*y_range),
        )

    def _random_direction(self):
        x_range, y_range = self.direction

        x = uniform(*x_range)
        y = uniform(*y_range)

        length = math.sqrt(x * x + y * y)

        if length == 0:
            return 0.0, 0.0

        x /= length
        y /= length

        angle = uniform(
            -self.spread,
            self.spread,
        )

        radians = math.radians(angle)

        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        return (
            x * cos_a - y * sin_a,
            x * sin_a + y * cos_a,
        )

    def emit(self):
        for _ in range(self.amount):
            if self.timer <= 0:
                self._spawn_particle()
                self.timer = self.spawn_delay

    def update(self, dt):
        self.timer -= dt

        if self.timer <= 0:
            self.emit()

            if self.burst_delay > 0 and self.spawn_delay <= 0:
                self.timer = self.burst_delay
            else:
                self.timer = self.spawn_delay

    def _spawn_particle(self):
        x, y = self._random_position()
        dx, dy = self._random_direction()

        speed = uniform(*self.speed)
        color = choice(self.color)

        self.system.spawn(
            x=x,
            y=y,
            vx=dx * speed,
            vy=dy * speed,
            lifetime=self.lifetime,
            gravity=self.gravity,
            shape=self.shape,
            size=self.size,
            color=color,
        )
