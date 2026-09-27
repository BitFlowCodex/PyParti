from .emitter import Emitter
from .particle import Particle


class ParticleSystem:
    def __init__(self):
        self.particles: list = []
        self.emitters: list = []

    def create_emitter(
        self, *, position, velocity, speed, size, lifetime, shape, color, amount, delay
    ):
        particle = Particle(
            position_range=position,
            velocity_range=velocity,
            speed_range=speed,
            size=size,
            life_time=lifetime,
            shape=shape,
            color=color,
        )

        emitter = Emitter(
            particle_list=self.particles,
            particle=particle,
            amount=amount,
            delay=delay,
        )

        self.emitters.append(emitter)

        return emitter

    # Updates all particles and removes dead ones
    def update(self, delta):
        for particle in self.particles[:]:
            particle.update(delta)

            if not particle.is_alive():
                self.particles.remove(particle)

        for emitter in self.emitters[:]:
            emitter.update(delta)

    # Draws all particles onto the window
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
