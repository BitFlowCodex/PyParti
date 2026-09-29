from .particle import Particle
from pygame import Vector2
from random import uniform, choice


class Emitter:
    def __init__(
        self,
        particle_list: list,
        particle: object,
        amount: int = 5,
        burst_delay: float = 0.0,
        spawn_delay: float = 0.0,
        spread: float = 0.0,
    ):
        self.particle = particle
        self.amount = amount
        self.particle_list = particle_list
        self.burst_delay = burst_delay
        self.spawn_delay = spawn_delay
        self.spread = spread
        self.timer = 0.0

    def update(self, dt):
        self.timer -= dt

        if self.timer <= 0:
            self.emit()
            self.timer = self.burst_delay

    def emit(self):
        template = self.particle

        position = template.position_range
        if callable(position):
            position = position()
        else:
            pos_x_range, pos_y_range = position

            position = (
                uniform(*pos_x_range),
                uniform(*pos_y_range),
            )

        dir_x_range, dir_y_range = template.direction_range
        speed_range = template.speed_range
        color = template.color
        width, height = template.size

        for _ in range(self.amount):
            if self.timer <= 0:

                new_particle = Particle(
                    position_range=template.position_range,
                    direction_range=template.direction_range,
                    speed_range=speed_range,
                    life_time=template.life_time,
                    color=color,
                    size=(width, height),
                    gravity=template.gravity,
                    shape=template.shape,
                )

                direction = Vector2(
                    uniform(*dir_x_range),
                    uniform(*dir_y_range),
                )

                if direction.length_squared() == 0:
                    continue

                direction = direction.normalize()
                direction = direction.rotate(
                    uniform(-self.spread, self.spread),
                )

                speed = uniform(*speed_range)

                new_particle.velocity = direction * speed

                new_particle.position = Vector2(position)
                new_particle.color = choice(color)

                self.particle_list.append(new_particle)
                self.timer = self.spawn_delay
