from .emitter import Emitter
from .particle import Particle


class ParticleSystem:
    def __init__(self):
        self.particles: list = []
        self.emitters: list = []

    def create_emitter(
        self,
        *,
        position: tuple,
        direction: tuple,
        speed: float | tuple[float, float],
        size: float | tuple[float, float],
        lifetime: float = 3.0,
        shape: str = "rect",
        color: str | tuple | list = "white",
        amount: int = 5,
        burstdelay: float = 0.0,
        spawndelay: float = 0.0,
        spread: float = 0.0,
        gravity: float = 0.0,
    ):
        particle = Particle(
            position_range=position,
            direction_range=direction,
            speed_range=speed,
            size=size,
            life_time=lifetime,
            shape=shape,
            color=color,
            gravity=gravity,
        )

        emitter = Emitter(
            particle_list=self.particles,
            particle=particle,
            amount=amount,
            burst_delay=burstdelay,
            spawn_delay=spawndelay,
            spread=spread,
        )

        self.emitters.append(emitter)

        return emitter

    # Updates all particles and removes dead ones
    def update(self, delta):
        for particle in self.particles:
            particle.update(delta)

        self.particles[:] = [
            particle for particle in self.particles if particle.is_alive()
        ]

        for emitter in self.emitters:
            emitter.update(delta)

    # Draws all particles onto the window
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
