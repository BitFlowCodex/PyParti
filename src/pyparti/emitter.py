from .particle import Particle
from pygame import Vector2
from random import uniform


class Emitter:
    def __init__(
        self,
        particle_list: list,
        particle: object,
        amount: int = 5,
        delay: float = 0,
    ):
        self.particle = particle
        self.amount = amount
        self.particle_list = particle_list
        self.delay = delay
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
                velocity_range=self.particle.velocity_range,
                life_time=self.particle.life_time,
                color=self.particle.color,
                size=(width, height),
                gravity=self.particle.gravity,
                shape=self.particle.shape,
            )

            # Velocity's X and Y
            vx_range, vy_range = new_particle.velocity_range
            # Position's X and Y
            px_range, py_range = new_particle.position_range

            new_particle.velocity = Vector2(
                uniform(*vx_range),
                uniform(*vy_range),
            )
            new_particle.position = Vector2(uniform(*px_range), uniform(*py_range))

            self.particle_list.append(new_particle)
