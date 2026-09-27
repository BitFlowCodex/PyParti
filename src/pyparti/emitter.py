from .particle import Particle
from pygame import Vector2
from random import uniform


class Emitter:
    def __init__(
        self,
        particle_list: list,
        particle: object,
        amount: int = 5,
        delay: float = 0.0,
        spread: float = 0.0,
    ):
        self.particle = particle
        self.amount = amount
        self.particle_list = particle_list
        self.delay = delay
        self.spread = spread

        self.timer = 0

    def update(self, dt):
        self.timer -= dt

        if self.timer <= 0:
            self.emit()
            self.timer = self.delay

    def emit(self):
        width, height = self.particle.size

        for _ in range(self.amount):
            new_particle = Particle(
                position_range=self.particle.position_range,
                direction_range=self.particle.direction_range,
                speed_range=self.particle.speed_range,
                life_time=self.particle.life_time,
                color=self.particle.color,
                size=(width, height),
                gravity=self.particle.gravity,
                shape=self.particle.shape,
            )

            # Velocity's X and Y
            dir_x_range, dir_y_range = self.particle.direction_range
            # Position's X and Y
            pos_x_range, pos_y_range = self.particle.position_range

            direction = Vector2(
                uniform(*dir_x_range),
                uniform(*dir_y_range),
            ).normalize()

            angle = uniform(-self.spread, self.spread)

            direction = direction.rotate(angle)

            speed = uniform(*self.particle.speed_range)

            new_particle.velocity = direction * speed

            new_particle.position = Vector2(
                uniform(*pos_x_range), uniform(*pos_y_range)
            )

            self.particle_list.append(new_particle)
